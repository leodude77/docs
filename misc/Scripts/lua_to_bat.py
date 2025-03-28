import aiofiles
import asyncio
import sys
from pathlib import Path
import os
import re

# Usage: python lua_to_bat.py <app_id>
app_id = sys.argv[1]
if not app_id:
    print("Provide AppID")
    sys.exit()

async def generate_key_from_lua():
    lua_file_path = Path(os.getcwd()) / f"{app_id}.lua"
    luafile = await aiofiles.open(lua_file_path, 'r', encoding="utf-8")
    content = await luafile.read()
    await luafile.close()

    keyfile = await aiofiles.open(Path(os.getcwd()) / f"{app_id}.key", 'w', encoding="utf-8")
    addappid_pattern = re.compile(r'addappid\(\s*(\d+)\s*(?:,\s*\d+\s*,\s*"([0-9a-f]+)"\s*)?\)')
    setmanifestid_pattern = re.compile(r'setManifestid\(\s*(\d+)\s*,\s*"(\d+)"\s*(?:,\s*\d+\s*)?\)')

    for match in addappid_pattern.finditer(content):
        depot_id = match.group(1)
        decrypt_key = match.group(2) if match.group(2) else None
        if decrypt_key:
            await keyfile.write(f'{depot_id};{decrypt_key}\n')

    await keyfile.close()
    
    depot_dict = {}
    for match in setmanifestid_pattern.finditer(content):
        depot_id = match.group(1)
        manifest_id = match.group(2)
        depot_dict[depot_id] = manifest_id

    try:
        await generate_bat(depot_dict)
    except Exception as e:
        print(e)
            

DEPOTDOWNLOADER = "dotnet DepotDownloaderMod.dll"
DEPOTDOWNLOADER_ARGS = "-max-downloads 256 -verify-all"

async def generate_bat(depot_manifest_dict):
    try:
        depots = []
        decrypt_keys = []
        async with aiofiles.open(f'{app_id}.bat', mode="w", encoding="utf-8") as bat_file:
            async with aiofiles.open(Path(os.getcwd()) / f"{app_id}.key", 'r', encoding="utf-8") as f:
                async for line in f:
                    depots.append(line.strip().split(';')[0])
                    decrypt_keys.append(line.strip().split(';')[1])
            for ind, depot_id in enumerate(depots):
                await bat_file.write(f'{DEPOTDOWNLOADER} -app {app_id} -depot {depot_id} -manifest {depot_manifest_dict[depot_id]} -manifestfile {depot_id + "_" + depot_manifest_dict[depot_id]+ ".manifest"} -depotkeys {app_id}.key {DEPOTDOWNLOADER_ARGS}\n')
    except Exception as e:
        print(e)
        return False

asyncio.run(generate_key_from_lua())
