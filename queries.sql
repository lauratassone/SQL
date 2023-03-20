SELECT * FROM Tournament INNER JOIN Game ON 
Tournament.IdGame= Game.IdGame 
WHERE Game.Name =  'SuperSmashBros';

SELECT AVG(Wage) AS 'Average wage' FROM Employee_Data
INNER JOIN Player 
ON Employee_Data.IdEmployee = Player.IdEmployeeData
INNER JOIN Game ON Player.IdGame = Game.IdGame
WHERE Game.Name = 'Apex';

SELECT * FROM Tournament 
INNER JOIN Place
ON Place.IdPlace = Tournament.IdPlace;
SELECT * FROM Tournament 
INNER JOIN Place
ON Place.IdPlace = Tournament.IdPlace
WHERE Place.Name = 'Stadium';

SELECT COUNT(IdPlayer) AS 'Nbr Player by gender' FROM Player 
INNER JOIN Employee_Data 
ON Player.IdEmployeeData = Employee_Data.IdEmployee
GROUP BY Gender;



