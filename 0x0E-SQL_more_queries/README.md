# MySQL User Management and Database Basics

## Project Overview

This project serves as a comprehensive guide to MySQL user management and fundamental database concepts. Whether you're a beginner looking to set up users, manage privileges, or understand key database constraints, this repository covers essential topics to empower you in building robust MySQL databases.

## Table of Contents

- [How to Create a New MySQL User](#how-to-create-a-new-mysql-user)
- [How to Manage Privileges for a User to a Database or Table](#how-to-manage-privileges-for-a-user-to-a-database-or-table)
- [What's a PRIMARY KEY](#whats-a-primary-key)
- [What's a FOREIGN KEY](#whats-a-foreign-key)
- [How to Use NOT NULL and UNIQUE Constraints](#how-to-use-not-null-and-unique-constraints)
- [How to Retrieve Data from Multiple Tables in One Request](#how-to-retrieve-data-from-multiple-tables-in-one-request)
- [What Are Subqueries](#what-are-subqueries)
- [What Are JOIN and UNION](#what-are-join-and-union)

## How to Create a New MySQL User

To create a new MySQL user, use the following SQL command:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```

## How to Manage Privileges for a User to a Database or Table

Grant privileges to a user:

```sql
GRANT privilege_type ON database_name.table_name TO 'username'@'localhost';
```

Revoke privileges from a user:

```sql
REVOKE privilege_type ON database_name.table_name FROM 'username'@'localhost';
```

## What's a PRIMARY KEY

A PRIMARY KEY is a column or a set of columns that uniquely identifies each record in a table. It ensures data integrity and allows for efficient data retrieval.

## What's a FOREIGN KEY

A FOREIGN KEY is a field in a table that refers to the PRIMARY KEY in another table. It establishes a link between the two tables, enforcing referential integrity.

## How to Use NOT NULL and UNIQUE Constraints

- **NOT NULL Constraint:**

```sql
CREATE TABLE table_name (
    column1 datatype NOT NULL,
    column2 datatype,
    ...
);
```

- **UNIQUE Constraint:**

```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype UNIQUE,
    ...
);
```

## How to Retrieve Data from Multiple Tables in One Request

Use JOIN operations to retrieve data from multiple tables:

```sql
SELECT column1, column2, ...
FROM table1
JOIN table2 ON table1.column = table2.column;
```

## What Are Subqueries

A subquery is a query nested within another query. It can be used to retrieve data that will be used by the main query as a condition or to perform operations.

## What Are JOIN and UNION

- **JOIN:**

JOIN is used to combine rows from two or more tables based on a related column between them.

```sql
SELECT *
FROM table1
JOIN table2 ON table1.column = table2.column;
```

- **UNION:**

UNION is used to combine the result sets of two or more SELECT statements.

```sql
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
```

Explore the project to gain in-depth insights and hands-on examples for each of these topics. Happy coding!