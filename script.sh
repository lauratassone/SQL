#!/bin/sh
echo " 
Veuillez chosir l'option que vousvoulez exécuter:

1- Créer une base de données vide
2- Créer les tables de la base de données
3- Migrer les données de l'ancienne base de données vers la nouvelle
4- Créer et migrer la base de données
5- Récupérer des informations précises dans la base de données
6 - Supprimer toutes les informations "
read choix
if [ $choix = 1 ]
then 
    sqlite3 newdatabase.db < createdatabase.sql      
    echo " Vous venez de creer une base de données vide"
fi

if [ $choix = 2 ]
then 
    sqlite3 newdatabase.db < createtable.sql      
    echo " Vous venez de creer les tables de la  base de données"
fi
if [ $choix = 3 ]
then 
      sqlite3 newdatabase.db < migration.sql  
      echo " Vous venez de migrer les informations de l'anciene base de données vers la nouvelle"
fi
if [ $choix = 4 ]
then
    sqlite3 newdatabase.db < createtable.sql 
    sqlite3 newdatabase.db < migration.sql  
    echo "Vous venez de creer et remplir la base de données, en migrant les informations de l'anciene base de données vers la nouvelle "
fi
if [ $choix = 5 ]
then 
    echo "Voici qu'elques informations plus précises:"
    sqlite3 newdatabase.db < queries.sql  
fi
if [ $choix = 6 ]
then 
     sqlite3 newdatabase.db < deletetable.sql 
    echo "Vous venez de suprimer la base de données ainsi que toutes les informations qu'elle possède"
fi
