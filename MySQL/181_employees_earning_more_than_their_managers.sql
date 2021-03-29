SELECT emp.Name as 'Employee'
FROM Employee emp, Employee mgr
WHERE emp.ManagerId = mgr.Id
AND emp.Salary > mgr.Salary;
