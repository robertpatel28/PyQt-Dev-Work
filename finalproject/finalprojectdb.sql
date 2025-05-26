use finalprojectdb;
	
create table book_sales(
	transactionid int primary key,
    customername varchar(100),
    booktitle varchar(100),
    quantity int,
    total int
)
    