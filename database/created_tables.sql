CREATE TABLE IF NOT EXISTS book_store.books (
    isbn CHAR(10) PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL,
    subject VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS book_store.members (
    userid INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(30) NOT NULL,
    zip INT NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(40) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS book_store.orders (
    userid INT,
    ono INT PRIMARY KEY,
    created DATE,
    shipaddress VARCHAR(50),
    shipcity VARCHAR(30),
    shipzip INT,
    FOREIGN KEY (userid) REFERENCES book_store.members(userid)
);

CREATE TABLE IF NOT EXISTS book_store.cart (
    userid INT,
    isbn CHAR(10),
 cart   qty INT NOT NULL,
    PRIMARY KEY (userid, isbn),
    FOREIGN KEY (userid) REFERENCES book_store.members(userid),
    FOREIGN KEY (isbn) REFERENCES book_store.books(isbn)
);


CREATE TABLE IF NOT EXISTS book_store.odetails (
    ono INT,
    isbn CHAR(10),
    qty INT NOT NULL,
    amount FLOAT NOT NULL,
    PRIMARY KEY (ono, isbn),
    FOREIGN KEY (ono) REFERENCES book_store.orders(ono),
    FOREIGN KEY (isbn) REFERENCES book_store.books(isbn)
);