--select "7", count(*) from type_test_values group by "7"

--select min("8.1"),max("8.1"),avg("8.1") from type_test_values where "8.1" != ""

--select * from type_test_values where "8.1" = 353

select  "2" ,"5","7" as kw,"8.1" as "co2", count(*) from type_test_values where "8.1" != "" and substr([5],1,1) = '7' group by "2" ,"5","7","8.1"
