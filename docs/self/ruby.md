# Topics

## Rails resources
* https://github.com/fpsvogel/learn-ruby#rails-codebases-to-study
* https://github.com/solidusio/solidus
## bundler

## rvm

## rake tasks

## bundle commands

```
bundle install
bundle update 'gem'
bundle audit update && bundle audit
bundle exec brakeman
bundle exec rubocop
```
```
bundle exec rails s -p 3001
bundle exec rails db:create
bundle exec rails db:migrate
bundle exec rails db:drop
```

frozen_string_literal: true
freezes string literals
* improves performance by allocating required memory
* removes any accidental changes/modifies to string

require: false in gemfile
gem 'database_cleaner', '~> 2.0', require: false
* Specifies bundler to require the gem or not, if false the gem is not loaded on boot(for RoR app) and only loaded when required explicitely in a file (rake task for example, prevent heavy gems to load which is not required in the app code, only lazy load them)

source 'https://rubygems.org' in gemfile
prefernce for gems is from last written source to the first. Or better specify the source when specifying the gem
gem 'gemfromourrepo', source: "http://our.own.gem.repo.com/the/path/to/it"
source "http://our.own.gem.repo.com/the/path/to/it" do
  gem 'gemfromourrepo'
end

__dir__: Returns the path to the directory from which the current method is called

__FILE__ : Returns file name(relative path) https://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-__FILE__

Procfile specifies user defined names with services and using foreman we can start the services
```procfile.dev
thin: bundle exec thin start -e development -p 8080
unicorn: bundle exec unicorn -c config/unicorn.vagrant.rb
```
```
foreman start thin
foreman start unicorn
```

Rake task example - https://github.com/solidusio/solidus/blob/main/tasks/linting.rake

Symbols are immutable strings, easier for comparison, can save on memory, usually used in hash keys

Indexing in sql tables - https://www.atlassian.com/data/sql/how-indexing-works
* indexing is done on a column specified by user (non clustered indexes) which stores them sorted order for b-search to be done
* clustered index is the primary key which is created automatically when a table is created
* use binary search for reduced and optimized searches in a table
* query plan uses indexes when querying

Ror migration file example - https://github.com/solidusio/solidus/blob/main/api/db/migrate/20131017162334_add_index_to_user_spree_api_key.rb

routes is under config folder

attr_reader 
attr_writer 
attr_accessor - (both getter and setter done auto, instance variable assigned)

class_attribute (RoR specific) (Children do not inherit the value, ie changing at child object will not change the parent value)
class_attribute :klass_atr

modules are usally just specifying and using methods at varying levels in the app (basically sharing throughout)

self keyword used within a method, refers to the object which called the method
self in a module is used to directly use the method without mixing it in(include, extend..)
In a class, it refers to the class object itself. Meaning the instances of this class cant use that method, the method can only be called directly from class. Bottom 3 are pretty much the same (Understand singleton)
```
class A
    def self.some_method
        puts "Self check"
    end
end

Class A
    def A.some_method
        puts "Self check"
    end
end

A = Class.new
def A.some_method
    puts "Self check"
end
```

delayed jobs
database.yml
Sidekiq worker