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
* Solr 27:26
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

## Airtel

### Questions
* RDD, DR diff
* Hadoop and components (hdfs,mapreduce, YARN)
* How is spark different
* Jobs, stages, tasks
* What optimizations have you done in spark
* What airflow operators have you used
* What is DAG
* Some questions which I dont remember
* What OS are you working on
* What linux commands have you use
* Do you awk, top, chmod .txt 777
* Do you know git, what is merge vs rebase
* Have you used hdfs commands on linux (edge node)

### Coding
* Do you know stack & queue
* Implement a stack
* Below first i/p o/p Question - give better than O(n)2 complexity (Utilizes a stack appraently, hint was read data from the right)
* Next i/p o/p Questions - give better than O(n) complexity
* What is binary search, time complexity, pseudo code for it
* Write spark initilization code, read csv from hdfs and get the required output

```
public static void main(){
    
}

Class Stack{
    void Stack(int[] array_s){
        
        
    }
}

create array
    add elements into array

Input:  {6, 4, 12, 5, 2, 10}
Output: {12, 12, -1, 10, 10, -1}
 
Input:  {1, 3, 2, 4}
Output: {3, 4, 4, -1}

for(i=0; i<list.length(); i++)
    for j = i+1; j <list.length(); j++
        if[list]

stack = [4,12,5,2,10]

input: nums = [8, 11, 13, 15, 1, 4, 6], target = 1
Output: 4
Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], target = 3
Output: 8
Input: nums = [4,5,6,7,0,1,2], target = 0 
Output: 4

    get mid element of list
        check if target element is > or < mid element
            use the half part of the list where element would exist

id, user1, user2
1, Sushovan, Abhishek
2, Rohit, Sushovan
3, Sunil, Sushovan
4, Rohan, Sunil
5, Manish, Rohit
 
these is the log of linkedin views.
treat it like:
Sushovan has seen the profile of Abhishek
Rohit has seen the profile of Sushovan
Sunil has seen the profile of Sushovan
Rohan has seen the profile of Sunil

output:
------
Abhishek - 1
Sushovan - 2
Rohit - 1
Rohan - 0
Sunil - 1
Manish - 0

   df =  spark.read.format("csv").load("hdfs://log.csv")
    df1 = df.select(col("user1")).union(df.select(col("user2"))).dropDuplicates()
    df_likes = df.groupBy("user2").agg(count(lit(1)))
    df1.join(df_likes, df1.user1 == df_likes.user2).fi
```

### My questions to them
* What is job about, E2E Data engineering
    * Stack used:
        * Migrated from oozie to airflow
        * YARN to Kubernetes
        * Iceberg on top of s3, Hive catalouge
        * Use Java spark with multithreading
        * Around 20TB of data processed in a day
* Do you have data governance, Yes we do but can't talk about it out openly
* You said iceberg, where is the data and what catalouge do you use. Said to uncover about Iceberg more

### Round 2
* Say an array, list has 0s and 1s, smartest way to sort it. (Told brute force approach, 1 way is break into 2 subarrays and shuffle 0s and 1s back and forth - not the smartest way)
* Say you have list of different languages characters and numbers in list, how will you sort them, (Told using unicode but didnt really go anywhere)
* Employee table with your_id,name,boss_id get me the names of bosses into the table(used inner join, doesnt work completely but told later left join since CEO will be missed)
```
["eng", "hindi";

for (i = 0; i<arr.size(); i++)

public static void main(String [] args){
    String[] arr =  ["eng", "hindi"];
    map <string, int>  unicode_map[][];

    for (i = 0; i<arr.size(); i++){
        int uni_code = arr[i][0] -- unicode value
        unicode_map[arr[i]] = uni_code
        got nothing...
    }
}

empid, name, boss_id - emp

select a.empid, a.name, a.boss_id, b.name from
    emp a inner join emp b on a.boss_id = b.empid (Should be left join)
```
