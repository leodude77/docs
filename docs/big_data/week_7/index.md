# Welcome to week 7

## Day 1
* Date - 20250104
* Video - 13 serialized deep dive file formats parquet

## Serialization simple explaination

![RSS logo](../../assets/big_data/Week%207/dataserializationsimpleexample.jpeg "Subscribe to our RSS")

## Origin of Serialization

![](../../assets/big_data//Week%207/serialization_founding.jpeg)

## Data Serialization

![RSS logo](../../assets/big_data//Week%207/data_serialization_illustration.jpeg "Subscribe to our RSS")

## Advantages of Data Serialization

![RSS logo](../../assets/big_data//Week%207/advantages_of_data_serialization.jpeg "Subscribe to our RSS")

## File formats

![RSS logo](../../assets/big_data//Week%207/java_serialization_base.jpeg "Subscribe to our RSS")
![RSS logo](../../assets/big_data//Week%207/serialization_format_info.jpeg "Subscribe to our RSS")

|  Text File Format  |      *Parquet*     |   ORC (Optimized Row Columnar)    |
| -------- |-------------| --------- |
| Readable <br> Huge in size <br>  Row file  Format <br> Queries takes lot of time because row file format | COLUMNAR FILE FORMAT <br> Queries faster results because of columnar file formats <br> 60-80% Compression <br> Predicate Pushdown <br> FREQUENTLY USED DATA | COLUMNAR FILE FORMAT <br> 90-95 % Compression Ratio <br> Because of Over Compression  -- ZLIB Internal Compression <br> Queries are faster but not good as parquet -- OVER COMPRESSION RATE <br> HISTORICAL DATA STORAGE |

#### Size comparison
![RSS logo](../../assets/big_data//Week%207/serialization_format_size_comparison.jpeg "Subscribe to our RSS")

## Task
* What is predicate pushdown
* Sqoop import data as avro
