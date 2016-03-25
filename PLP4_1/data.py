s_emp = (('ID','LAST_NAME','FIRST_NAME','USERID','START_DATE','COMMENTS','TITLE','SALARY','COMMISSION','DEPT_ID','MANAGER_ID'),
(1, 'Martin', 'Carmen', 'martincu', '1990-05-03 00:00:00', ' ', 'President', 4500, ' ', 50, ' '),
(10	, 'Jackson', 'Marta', 'jacksomt', '1991-02-27 00:00:00', ' ', 'Warehouse Manager', 1507, ' ', 45, 2),
(11, 'Henderson', 'Colin', 'hendercs', '1990-05-14 00:00:00', ' ', 'Sales Representative', 1400, 10, 31, 3),
(12, 'Gilson', 'Sam', 'gilsonsj', '1992-01-18 00:00:00', ' ', 'Sales Representative', 1490, 12.5, 32, 3),
(13, 'Sanders', 'Jason', 'sanderjk', '1991-02-18 00:00:00', ' ', 'Sales Representative', 1515, 10, 33, 3),
(14, 'Dameron', 'Andre', 'dameroap', '10-09-1991 00:00:00', ' ', 'Sales Representative', 1450, 17.5, 35, 3),
(15, 'Hardwick', 'Elaine', 'hardwiem', '02-07-1992 00:00:00', ' ', 'Stock Clerk', 1400, ' ', 41, 6),
(16, 'Brown', 'George', 'browngw', '03-08-1990 00:00:00', ' ', 'Stock Clerk', 940, ' ', 41, 6),
(17, 'Washington', 'Thomas', 'washintl', '02-09-1991 00:00:00', ' ', 'Stock Clerk', 1200, ' ', 42, 7),
(18, 'Patterson', 'Donald', 'patterdv', '08-06-1991 00:00:00', ' ', 'Stock Clerk', 795, ' ', 42, 7),
(19, 'Bell', 'Alexander', 'bellag', '05-26-1991 00:00:00', ' ', 'Stock Clerk', 850, ' ', 43, 8),
(2, 'Smith', 'Doris', 'smithdj', '03-08-1990 00:00:00', ' ', 'VP, Operations', 2450, ' ', 41, 1),
(20, 'Gantos', 'Eddie', 'gantosej', '11-30-1990 00:00:00', ' ', 'Stock Clerk', 800, ' ', 44, 9),
(21, 'Stephenson', 'Blaine', 'stephebs', '03-17-1991 00:00:00', ' ', 'Stock Clerk', 860, ' ', 45, 10),
(22, 'Chester', 'Eddie', 'chesteek', '11-30-1990 00:00:00', ' ', 'Stock Clerk', 800, ' ', 44, 9),
(23, 'Pearl', 'Roger', 'pearlrg', '10-17-1990 00:00:00', ' ', 'Stock Clerk', 795, ' ', 34, 9),
(24, 'Dancer', 'Bonnie', 'dancerbw', '03-17-1991 00:00:00', ' ', 'Stock Clerk', 860, ' ', 45, 7),
(25, 'Schmitt', 'Sandra', 'schmitss', '05-09-1991 00:00:00', ' ', 'Stock Clerk', 1100, ' ', 45, 8),
(3, 'Norton', 'Michael', 'nortonma', '06-17-1991 00:00:00', ' ', 'VP, Sales', 2400, ' ', 31, 1),
(4, 'Quentin', 'Mark', 'quentiml', '04-07-1990 00:00:00', ' ', 'VP, Finance', 2450, ' ', 10, 1),
(5, 'Roper', 'Joseph', 'roperjm', '03-04-1990 00:00:00', ' ', 'VP, Administration', 2550, ' ', 50, 1),
(6, 'Brown', 'Molly', 'brownmr', '01-18-1991 00:00:00', ' ', 'Warehouse Manager', 1600, ' ', 41, 2),
(7, 'Hawkins', 'Roberta', 'hawkinrt', '05-14-1990 00:00:00', ' ', 'Warehouse Manager', 1650, ' ', 42, 2),
(8, 'Burns', 'Ben', 'burnsba', '04-07-1990 00:00:00', ' ', 'Warehouse Manager', 1500, ' ', 43, 2),
(9, 'Catskill', 'Antoinette', 'catskiaw', '02-09-1992 00:00:00', ' ', 'Warehouse Manager', 1700, ' ', 44, 2))

s_dept = (('ID','NAME','REGION_ID'),
(10, 'Finance', 1),
(31, 'Sales', 1),
(32, 'Sales', 2),
(33, 'Sales', 3),
(34, 'Sales', 4),
(35, 'Sales', 5),
(41, 'Operations', 1),
(42, 'Operations', 2),
(43, 'Operations', 3),
(44, 'Operations', 4),
(45, 'Operations', 5),
(50, 'Administration', 1))


print ''
print 'select * from s_dept;'
print ([[i[0], i[1], i[2]] for i in s_dept[1::]])

print ''
print 'select last_name, first_name, title, salary from s_emp;'
print([[i[1], i[2], i[6], i[7]] for i in s_emp[1::]])

print ''
print 'select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40;'
print([[i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 if i[9] > 40])

print ''
print 'select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name;'
print(sorted([[i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 if i[9] > 40], key = lambda x : x[0]))

print ''
print 'select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc;'
print(sorted([[i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 if i[9] > 40], key = lambda x : int(x[3]), reverse =True))

print''
print 'select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id);'
print([[i[1], i[2], i[6], i[7], j[1]] for i in s_emp[1::] for j in s_dept[1::] if i[9] == j[0]])


print''
print 'select dept_id, avg(salary) from s_emp group by dept_id order by dept_id;'
result = [];
for department in { d[9] for d in s_emp[1::] }: result.append((department,(lambda l: round(sum(l) / len(l), 2))(map(float, [ e[7] for e in s_emp[1::] if e[9] == department]))))
print(sorted(result, key = lambda x: x[0]))


print ''
print 'select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500;'
#for department in { d[9] for d in s_emp[1::] }: print (lambda deptid, avgSal: (deptid, avgSal) if avgSal > 2000 else '')(department, lambda l: round(sum(l) / len(l), 2))(map(float, [ e[9] for e in s_emp[1::] if e[9] == department ]))
result2 = [];
for department in { d[9] for d in s_emp[1::] }: result2.append((lambda deptno, avgSal: [deptno, avgSal] if avgSal < 1500 else '')(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ]))))
while '' in result2:
    result2.remove('')
print result2