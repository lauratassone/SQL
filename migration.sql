ATTACH DATABASE 'projectSQL.db' AS old_db;
ATTACH DATABASE 'newdatabase.db' AS new_db;


INSERT INTO new_db.Place(Name, Address, City) SELECT PlaceName, Address, City 
FROM old_db.Tournament;

INSERT INTO new_db.Game( Name) SELECT  Name 
FROM old_db.Game;

INSERT INTO new_db.Employee_Data(Lastname, Firstname, Gender, Age, Wage)SELECT Lastname, Firstname, Gender, Age, Wage  
FROM old_db.Staff;

INSERT INTO new_db.Employee_Data(Lastname, Firstname, Gender, Age, Wage)SELECT Lastname, Firstname, Gender, Age, Wage  
FROM old_db.Player;

INSERT INTO new_db.Employee_Data(Lastname, Firstname, Gender, Age, Wage)SELECT Lastname, Firstname, Gender, Age, Wage  
FROM old_db.Coach;

INSERT INTO new_db.Tournament (IdPlace, IdGame, Date, Duration) 
SELECT new_db.Place.IdPlace, new_db.Game.IdGame, Date, Duration
FROM old_db.Tournament, new_db.Place, new_db.Game 
WHERE old_db.Tournament.PlaceName = new_db.Place.Name AND old_db.Tournament.IdGame = new_db.Game.IdGame;

INSERT INTO new_db.Staff(IdEmployeeData) SELECT new_db.Employee_Data.IdEmployee FROM new_db.Employee_Data, old_db.Staff
WHERE old_db.Staff.Lastname = new_db.Employee_Data.Lastname;

INSERT INTO new_db.Player(IdGame, Ranking, IdEMployeeData)
SELECT  new_db.Game.IdGame, Ranking, new_db.Employee_Data.IdEmployee
FROM old_db.Player, new_db.Game, new_db.Employee_Data
WHERE old_db.Player.IdGame = new_db.Game.IdGame AND old_db.Player.Lastname = new_db.Employee_Data.Lastname;

INSERT INTO new_db.Coach(IdGame, LicenseDate, IdEMployeeData)
SELECT new_db.Game.IdGame,old_db.Coach.LicenseDate, new_db.Employee_Data.IdEmployee
FROM new_db.Game, old_db.Coach, new_db.Employee_Data
WHERE old_db.Coach.IdGame = new_db.Game.IdGame AND old_db.Coach.Lastname = new_db.Employee_Data.Lastname;


DETACH DATABASE old_db;
DETACH DATABASE new_db;
