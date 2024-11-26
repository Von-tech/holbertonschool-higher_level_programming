# SQL - Introduction

This is a basic guide to introduce you to SQL (Structured Query Language) and MySQL, a popular relational database management system. In this document, we'll cover the fundamentals of SQL and how to perform various operations using MySQL.

## Table of Contents
- [SQL - Introduction](#sql---introduction)
  - [Table of Contents](#table-of-contents)
  - [1. What's a Database?](#1-whats-a-database)
  - [2. What's a Relational Database?](#2-whats-a-relational-database)
  - [3. What Does SQL Stand For?](#3-what-does-sql-stand-for)
  - [4. What's MySQL?](#4-whats-mysql)
  - [5. How to Create a Database in MySQL](#5-how-to-create-a-database-in-mysql)
  - [6. DDL and DML](#6-ddl-and-dml)
  - [7. How to CREATE or ALTER a Table](#7-how-to-create-or-alter-a-table)
  - [8. How to SELECT Data from a Table](#8-how-to-select-data-from-a-table)
  - [9. How to INSERT, UPDATE, or DELETE Data](#9-how-to-insert-update-or-delete-data)
  - [10. What are Subqueries?](#10-what-are-subqueries)
  - [11. How to Use MySQL Functions](#11-how-to-use-mysql-functions)
    - [**Authors**](#authors)

## 1. What's a Database?
A database is a structured collection of data that is organized and stored for easy retrieval and manipulation. It serves as a repository for various types of information.

## 2. What's a Relational Database?
A relational database is a type of database that uses a tabular structure to store data, organized into rows and columns. It establishes relationships between tables using keys to maintain data integrity and facilitate efficient queries.

## 3. What Does SQL Stand For?
SQL stands for Structured Query Language. It is a powerful programming language used to interact with databases. SQL allows users to manage, retrieve, and manipulate data stored in a relational database.

## 4. What's MySQL?
MySQL is an open-source and widely-used Relational Database Management System (RDBMS) based on SQL. It provides a platform for creating and managing databases, making it a popular choice for web applications and various software systems.

## 5. How to Create a Database in MySQL
To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE database_name;
```

## 6. DDL and DML
- DDL stands for Data Definition Language. It is used to define and manage the structure of database objects such as tables, indexes, etc.
- DML stands for Data Manipulation Language. It is used to retrieve, insert, update, and delete data within the database.

## 7. How to CREATE or ALTER a Table
To create a new table in MySQL, you can use the following SQL command:

```sql
CREATE TABLE table_name (
  column1 datatype constraints,
  column2 datatype constraints,
  ...
);
```

To alter an existing table to add a new column, you can use the following SQL command:

```sql
ALTER TABLE table_name
ADD column_name datatype constraints;
```

## 8. How to SELECT Data from a Table
To retrieve data from a table, you can use the SELECT statement:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## 9. How to INSERT, UPDATE, or DELETE Data
To insert new records into a table, you can use the INSERT INTO statement:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

To update existing records in a table, you can use the UPDATE statement:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

To delete records from a table, you can use the DELETE FROM statement:

```sql
DELETE FROM table_name
WHERE condition;
```

## 10. What are Subqueries?
Subqueries, also known as nested queries, are queries embedded within another SQL statement. They allow you to retrieve data based on the results of another query.

## 11. How to Use MySQL Functions
MySQL provides a variety of built-in functions to perform calculations, manipulate strings, dates, and more. Here's an example of using the `COUNT` function to count the number of records in a table:

```sql
SELECT COUNT(column_name)
FROM table_name;
```

Feel free to explore the official MySQL documentation for more functions and their usage.

This concludes our brief introduction to SQL and MySQL. Happy querying!


### **Authors**
---

Vonzell S. Carson
