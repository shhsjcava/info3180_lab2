
CREATE TABLE users(
        userid varchar(5),
        fname varchar(15), 
        lname varchar (15), 
        email varchar(25),
        sex varchar(6),
        location varchar(50), 
        bio text,
        joined date,
        photo varchar(20),
        primary key(userid)); 
        
INSERT INTO peoples  VALUES ('as123', 'Amy', 'Santiago', 'aaammmayyy@nine-nine.com', 'Female','Brooklyn, NY', 'hey..its me', '2017-09-13');
insert into peoples VALUES ('jp124','Jake', 'Peralta', 'jakebaby@mail.com','Male', 'Miami, Fl', 'wazzzuupp', '2017-05-27');
insert into peoples VALUES('rd125','Rosa', 'Diaz', 'rosa.diaz@nine-nine.com','Female', 'Kingston, Jamaica','Now you have the last hidden treasures to carve your own path to success. If you put these principles into action, there is no way you can fail. May your journey be a pleasant and safe one.', '2018-03-12');
insert into peoples VALUES('cb126','Charles', 'Boyle','sircharles@mail.com', 'Male', 'London, England', 'cheerio!', '2018-02-14');