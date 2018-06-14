-------------------------------------
--
--@file: Good vs Evil.py
--@time: 2018/06/{DAY}

--Title: GROCERY STORE: Support Local Products
--描述:SQL Basics: Create a FUNCTION (DATES)
/*
        For this challenge you need to create a basic Age Calculator
    function which calculates the age in years on the age field of
    the peoples table.
        The function should be called agecalculator, it needs to take 1
    date and calculate the age in years according to the date NOW
    and must return an integer.

        You may query the people table while testing but the query must
    only contain the function on your final submit.

    people table schema
        id
        name
        age
    NOTE: Your solution should use pure SQL. Ruby is used within the test
    cases to do the actual testing.





results = run_sql

describe "tests" do
  describe "should contain keywords" do
    it "should contain CREATE" do
      expect($sql.upcase).to include("CREATE")
    end

    it "should contain FUNCTION" do
      expect($sql.upcase).to include("FUNCTION")
    end

    it "should contain AGECALCULATOR" do
      expect($sql.upcase).to include("AGECALCULATOR")
    end

    it "should not query people table" do
      expect($sql.upcase).not_to include("PEOPLE")
    end
  end
end



*/


-- Create your FUNCTION statement here


create function agecalculator(v_date in DATE,v_id in NUMBER ) return number
as
  v_age number;
begin
  SELECT floor(TO_NUMBER(sysdate - v_date)/365) INTO v_age FROM people WHERE id = v_id;
return v_age;
end;



create function agecalculator(v_date in DATE ) return number
as
  v_age number;
begin
  v_get = floor(TO_NUMBER(sysdate - v_date)/365);
return v_age;
end;






--带有IN参数的函数
create or replace function get_empname(v_id in number) return varchar2 as
  v_name varchar2(50);
begin
  select name into v_name from employee where id = v_id;
   return v_name;
exception
  when no_data_found then
    raise_application_error(-20001, '你输入的ID无效！');
end get_empname;