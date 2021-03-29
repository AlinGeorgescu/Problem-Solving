SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.Email = p2.Email and p1.Id != p2.Id;

-- alternative

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;
