import sqlite3
def createdatabase(name):
    connexion= sqlite3.connect(name)
    c = connexion.cursor()
    c.executescript('''ATTACH DATABASE '{}' AS DB;
        '''
          .format(name)
    )
    connexion.commit()
    c.close()
    connexion.close()
        

def createschema(name):
    connexion= sqlite3.connect(name)
    c = connexion.cursor()
    c.executescript('''CREATE  TABLE IF NOT EXISTS  Place  (
    IdPlace INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR2(30),
    Address VARCHAR2(30),
    City VARCHAR2(30)
);
CREATE  TABLE IF NOT EXISTS  Tournament  (
    IdTournament INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    IdPlace INTEGER NOT NULL, 
    IdGame  INTEGER NOT NULL,
    Date VARCHAR2(30) NOT NULL,
    Duration INTEGER,
    FOREIGN KEY (IdPlace) REFERENCES Place(IdPlace),
    FOREIGN KEY (IdGame) REFERENCES Game(IdGame)
);
CREATE  TABLE IF NOT EXISTS  Game  (
    IdGame INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR2(30)
);
CREATE  TABLE IF NOT EXISTS  Player  (
    IdPlayer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      IdGame  INTEGER NOT NULL,
      Ranking INTEGER,
      IdEmployeeData INTEGER NOT NULL,
    FOREIGN KEY (IdGame) REFERENCES Game(IdGame),
    FOREIGN KEY (IdEmployeeData) REFERENCES Employee_Data(IdEmployee)
);

CREATE  TABLE IF NOT EXISTS  Coach (
    IdCoach INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   IdGame INTEGER NOT NULL, 
   LicenseDate  VARCHAR2(30),
   idEmployeeData INTEGER NOT NULL,
    FOREIGN KEY (IdGame) REFERENCES Game(IdGame),
    FOREIGN KEY (idEmployeeData) REFERENCES Employee_Data(IdEmployee)
);
CREATE  TABLE IF NOT EXISTS  Staff (
  IdStaff INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
  idEmployeeData INTEGER NOT NULL, 
    FOREIGN KEY (idEmployeeData) REFERENCES Employee_Data(IdEmployee)
);

CREATE  TABLE IF NOT EXISTS  Employee_Data (
    IdEmployee INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT,
    Lastname VARCHAR2(30),
    Firstname  VARCHAR2(30),
    Gender  VARCHAR2(30),
    Age INTEGER,
    Wage  INTEGER
);
    ''')
    connexion.commit()
    c.close()
    connexion.close()

def migration(newname, oldname):
    connexion= sqlite3.connect(newname)
    c = connexion.cursor()
    c.executescript('''
    ATTACH DATABASE '{}' AS old_db;
ATTACH DATABASE '{}' AS new_db;


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
    '''
    .format(oldname, newname)
    )

    connexion.commit()
    c.close()
    connexion.close()
def recuperation():
    connexion= sqlite3.connect('newdatabase.db')
    c = connexion.cursor()
    c.executescript('''
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

    ''')

    connexion.commit()
    c.close()
    connexion.close()
def delete():
    connexion= sqlite3.connect('newdatabase.db')
    c = connexion.cursor()
    c.executescript('''
    DROP TABLE IF EXISTS Game;

DROP TABLE IF EXISTS Tournament;

DROP TABLE IF EXISTS Place;

DROP TABLE IF EXISTS Employee_Data;


DROP TABLE IF EXISTS Staff;

DROP TABLE IF EXISTS Player;

DROP TABLE IF EXISTS Coach;
    ''')
    connexion.commit()
    c.close()
    connexion.close()




def menu():
    print ("Veuillez chosir l'option que vousvoulez exécuter:")
    print ("1- Créer une base de données vide")
    print ("2- Créer les tables de la base de données")
    print ("3- Migrer les données de l'ancienne base de données vers la nouvelle")
    print("4- Créer et migrer la base de données")
    print("5- Récupérer des informations précises dans la base de données")
    print("6 - Supprimer toutes les informations")
    choice = input(" ")
    if choice == '1':
        name = input("veuillez choisir un nom pour créer la de base de données:")
        createdatabase(name)
        input("vous venez de creer une base de données vide")

    if  choice == '2': 
        name = input("veuillez choisir un nom de base de données:")
        print(" Le nom de votre base de données est :" + name)
        createschema(name)  
        print(" Vous venez de creer les tables de la  base de données")
    if  choice == '3': 
        newname = input ("veuillez chisir le nom de la base de donnéees que vous voulez remplir ")
        oldname = input("veuillez choisir la base de données depuis laquelle prendre les données")
        migration(newname, oldname)  
      
        print("Vous venez de migrer les informations de l'anciene base de données vers la nouvelle")
    if  choice == '4': 
        name = input("veuillez choisir un nom de base de données:")
        print(" Le nom de votre base de données est :" + name)
        createschema(name)
        newname = input ("veuillez chisir le nom de la base de donnéees que vous voulez remplir ")
        oldname = input("veuillez choisir la base de données depuis laquelle prendre les données")
        migration(newname, oldname)   
        print("Vous venez de creer et remplir la base de données, en migrant les informations de l'anciene base de données vers la nouvelle ")
    if  choice == '5': 
        print("Voici quelques informations plus précises:")
        recuperation()    
    if  choice == '6':
        delete()  
        print("Vous venez de suprimer la base de données ainsi que toutes les informations qu'elle possède")
        
      
def main():
    menu()
main()