sqlite3 htmltable.db
SQLite version 3.25.2 2018-09-25 19:08:10
Enter ".help" for usage hints.
sqlite> create table student(sid varchar(4) primary key,sname varchar(30) not null,dob date not null,class varchar(3) not null);
sqlite> insert into student values('1001','hari','1996-12-20','X');
sqlite> insert into student values('1002','vidhya','1996-11-24','X');
sqlite> insert into student values('1003','kavya','1997-10-12','X');
sqlite> insert into student values('1004','sandya','1997-08-02','X');
sqlite> insert into student values('1005','rohan','1996-04-08','X');
sqlite> create table marks(sid varchar(4),exam_date date not null,tamil varchar(3),english varchar(3),maths varchar(3),science varchar(3),social varchar(3), foreign key(sid) references student(sid));
sqlite> insert into marks values("1001","1996-01-02","56","67","78","76","52");
sqlite> insert into marks values("1002","1996-01-18","67","65","79","52","89");
sqlite> insert into marks values("1003","1996-01-10","56","67","87","56","85");
sqlite> insert into marks values("1004","1996-01-20","59","98","56","67","67");
sqlite> insert into marks values("1005","1996-01-25","58","78","66","69","97");
sqlite> insert into marks values("1001","1996-02-02","67","87","65","72","81");
sqlite> insert into marks values("1002","1996-02-15","87","97","75","78","61");
sqlite> insert into marks values("1003","1996-02-20","86","77","65","78","91");
sqlite> insert into marks values("1004","1996-02-25","56","57","65","78","91");
sqlite> insert into marks values("1005","1996-02-30","66","85","75","68","78");
sqlite> select * from student;
1001|hari|1996-12-20|X
1002|vidhya|1996-11-24|X
1003|kavya|1997-10-12|X
1004|sandya|1997-08-02|X
1005|rohan|1996-04-08|X
sqlite> select * from marks;
1001|1996-01-02|56|67|78|76|52
1002|1996-01-18|67|65|79|52|89
1003|1996-01-10|56|67|87|56|85
1004|1996-01-20|59|98|56|67|67
1005|1996-01-25|58|78|66|69|97
1001|1996-02-02|67|87|65|72|81
1002|1996-02-15|87|97|75|78|61
1003|1996-02-20|86|77|65|78|91
1004|1996-02-25|56|57|65|78|91
1005|1996-02-30|66|85|75|68|78
