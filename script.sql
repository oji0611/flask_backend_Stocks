CREATE TABLE product(
  productid INTEGER NOT NULL,
  category VARCHAR(50) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  libele VARCHAR(50) NOT NULL,
  PRIMARY KEY (productid)
);

CREATE TABLE entry(
  entryid INTEGER NOT NULL,
  entrydate DATETIME NOT NULL,
  product INTEGER NOT NULL,
  quantity REAL NOT NULL,
  mov_type VARCHAR(10),
  PRIMARY KEY (entryid),
  FOREIGN KEY(product) REFERENCES product(productid)
);
