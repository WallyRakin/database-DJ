### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is an open-source relational database management system (RDBMS).

- What is the difference between SQL and PostgreSQL?

  SQL (Structured Query Language) is a domain-specific language used to manage and manipulate relational databases. PostgreSQL is a specific RDBMS that uses SQL as its query language.

- In `psql`, how do you connect to a database?

  In psql, you can connect to a database using the command psql -h hostname -U username -d databasename.

- What is the difference between `HAVING` and `WHERE`?

  WHERE is used to filter records before any groupings are made. HAVING is used to filter groups after the GROUP BY clause has been applied.

- What is the difference between an `INNER` and `OUTER` join?

  An INNER JOIN returns rows when there is a match in both tables. An OUTER JOIN returns all rows from one table and the matched rows from the second table, filling in with NULLs if there is no match.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

  A LEFT OUTER JOIN returns all rows from the left table and the matched rows from the right table. A RIGHT OUTER JOIN returns all rows from the right table and the matched rows from the left table.

- What is an ORM? What do they do?

  ORM stands for Object-Relational Mapping. It is a programming technique that allows you to interact with your database, like you would with SQL, but using objects.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?

  AJAX requests are made from the client side (browser) and are typically used to update parts of a web page without reloading the entire page. Server-side requests using libraries like requests are made from the server and can be used for a variety of tasks, including fetching data from another server.

- What is CSRF? What is the purpose of the CSRF token?

  CSRF stands for Cross-Site Request Forgery. It is an attack that tricks the victim into submitting a malicious request. A CSRF token is used to protect against CSRF attacks by ensuring that every form submission is accompanied by a unique token that is verified by the server.

- What is the purpose of `form.hidden_tag()`?

  form.hidden_tag() is used in Flask-WTF forms to generate a hidden field that includes a CSRF token, which helps protect against CSRF attacks.