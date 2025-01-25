## Wissen Infotech

### Coding
Find all permutations of an array
(Sol uses backtracking recursion was the hint)
Didnt solve for shit
* Input [1,2,3]
* Output [[1,2,3], [1,3,2], [2,3,1], [2,1,3], [3,1,2], [3,2,1]]

### Questions
* How does MVC architecture in rails work? How would you handle complex business logic which does not fit this model
    * Logic which cannot be placed in controller, where would you place that logic (I answered helpers and concerns)

* How does rails handle db migration and how you manage complex migrations in production db environment?

* How does rails handle background job and when would you choose different background processing tools like sidekiq Resque or delayed job

* How does rails manage and render Partial end layouts and how would you optimize rendering for complex or highly dynamic views

* How does rails handle session authentication management and how would implement a custom authentication if needed?

* How does rails handle RESTful routing and how do you structure route for an api with both public and private endpoints, can you explain how would you setup custom routing constraints/throttling for different types of endpoints

* How does active record work in rails and how would you optimize it to handle complex queries or large datasets

## Thoughtfocus

### Questions

* Did you work on monolithic or microservice, have you worked on frontend technologies
* Have you heard about elixir, pheonix? Any JS experience, Python experience, Vuejs, Heroku or AWS, database used, postgresql, Kafka
* How object oriented concepts works in RoR (What are oops concepts)
* Why everything is an object in Ruby
* Do you know ancestral hierarchy (include, extend, prepend)
* How encapsulation works in Ruby
* Is multiple inheritance supported in Ruby?
* How can we use modules(Difference between prepend, include)
* Have you worked with any associations? Any idea on has_many, belongs_to_many
* has_many:through vs has_and_belongs_to_many
* Polymorphic associations
* You know how REST services work(microservice), how authentication is being done in that(how exactly is the authentication working). When SignUp happens how does it work, when the same user logs in later, how does authentication happen then
    * Same token you can use for login later?
* Difference between put and patch
* Have you worked with background jobs? Follow up: Sidekiq
* Solar 27:26
* What is database indexing
* I have huge database with millions of records, I have 6 columns, 5 of them are important(excluding id which is the 6th), can we improve performance by indexing all of them?
    * Is it good or bad? Indexing multiple columns
* Difference between collection and member (member in routes)
* What is strong parameters
* Associative capabilities can we add in strong parameters
* What is attribute accessor
* You worked with callbacks right, what is diff between before_commit and before_save
* Any idea on scope (in ActiveRecord)
* What is ORM, how is it working
* SOLID principles
* Do you know CI/CD
* Unit testing
* Went to coding part and questions after that
    * Do you know about metaprogramming
    * Do you know about singleton class
    * For performance improvement was any tool used, (to identify or log) and how will you solve that issue
    * Have you done any code optimization
    * Difference between includes and joins (this is Rails)
    * Left outer join vs inner join
    * What rails version did you work on? So have you worked with multiple database
    * What type of work did you? Requirements or priority work (Only working on fixing issues?)
    * Microservice architecture right? what is tech stack used in your product? (Frontend? React - did you get a chance to work on it?)

### Coding
Didnt solve for shit again
* Count elements and convert into hash
    * Input: [1,nil,2,5,5,7,2,1,9]
    * Output: {1 => 2, 2=> 2, 5 => 2, 7 => 1, 9 => 1}
* Write a query to get the employee with second highest salary from employees and salaries table
    * employee: id, name
    * salaries: id, employee_id, salary
