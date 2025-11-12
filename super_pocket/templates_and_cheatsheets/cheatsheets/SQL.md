# **Cheat Sheet Complète MySQL (Version Étendue)**

Ce guide couvre les commandes et concepts essentiels de MySQL, des opérations de base à la gestion avancée, avec des exemples détaillés pour une meilleure compréhension.

### **1\. Connexion et Commandes de Base**

* **Se connecter à MySQL via le terminal :**  
  \-- Connexion standard  
  mysql \-u nom\_utilisateur \-p

  \-- Spécifier un hôte (serveur distant) et une base de données  
  mysql \-h nom\_d\_hote \-u nom\_utilisateur \-p nom\_de\_la\_base

  *(Le système vous demandera ensuite le mot de passe.)*  
* **Afficher les informations de la session :**  
  \-- Voir l'utilisateur et la base de données actuels  
  SELECT USER(), DATABASE();

  \-- Afficher la version du serveur MySQL  
  SELECT VERSION();

* **Afficher toutes les bases de données :**  
  SHOW DATABASES;

* **Sélectionner une base de données pour l'utiliser :**  
  USE nom\_de\_la\_base;

* **Afficher toutes les tables de la base de données actuelle :**  
  SHOW TABLES;

* **Décrire la structure d'une table :**  
  \-- Informations de base sur les colonnes  
  DESCRIBE nom\_de\_la\_table;  
  \-- ou  
  DESC nom\_de\_la\_table;

  \-- Informations plus détaillées (moteur de stockage, etc.)  
  SHOW TABLE STATUS LIKE 'nom\_de\_la\_table';

* **Afficher la commande CREATE TABLE qui a créé la table :**  
  SHOW CREATE TABLE nom\_de\_la\_table;

* **Quitter le client MySQL :**  
  EXIT; \-- ou QUIT;

### **2\. Manipulation des Données (LMD \- Langage de Manipulation de Données)**

* **SELECT : Interroger des données**  
  \-- Sélectionner toutes les colonnes de la table  
  SELECT \* FROM nom\_de\_la\_table;

  \-- Sélectionner des colonnes spécifiques avec des alias  
  SELECT colonne1 AS 'Nom', colonne2 AS 'Email' FROM nom\_de\_la\_table;

  \-- Sélectionner avec une condition et trier  
  SELECT \* FROM nom\_de\_la\_table WHERE age \> 25 ORDER BY nom ASC;

  \-- Limiter les résultats et définir un point de départ (pour la pagination)  
  SELECT \* FROM nom\_de\_la\_table LIMIT 10 OFFSET 20; \-- Affiche 10 résultats en commençant après le 20ème

  \-- Utilisation de sous-requêtes  
  SELECT nom FROM utilisateurs WHERE id IN (SELECT utilisateur\_id FROM commandes WHERE montant \> 100);

  \-- Instruction CASE pour la logique conditionnelle  
  SELECT nom,  
         CASE  
             WHEN age \>= 18 THEN 'Majeur'  
             ELSE 'Mineur'  
         END AS statut\_legal  
  FROM utilisateurs;

* **INSERT INTO : Insérer de nouvelles lignes**  
  \-- Insérer une ligne en spécifiant les colonnes  
  INSERT INTO nom\_de\_la\_table (colonne1, colonne2) VALUES ('valeur1', 123);

  \-- Insérer plusieurs lignes en une seule commande  
  INSERT INTO nom\_de\_la\_table (colonne1, colonne2) VALUES  
  ('valeurA1', 456),  
  ('valeurB1', 789);

  \-- Insérer les résultats d'une requête SELECT  
  INSERT INTO archives\_clients (id, nom, email)  
  SELECT id, nom, email FROM clients WHERE est\_actif \= 0;

* **UPDATE : Mettre à jour des lignes existantes**  
  \-- Mettre à jour avec une condition  
  UPDATE nom\_de\_la\_table  
  SET colonne1 \= 'nouvelle\_valeur', colonne2 \= colonne2 \+ 1  
  WHERE id \= 42;  
  \-- ATTENTION : Oublier la clause WHERE mettra à jour TOUTES les lignes de la table \!

  \-- Mettre à jour plusieurs tables avec une jointure  
  UPDATE commandes c  
  JOIN clients cl ON c.client\_id \= cl.id  
  SET c.statut \= 'Archivé'  
  WHERE cl.date\_dernier\_achat \< '2022-01-01';

* **DELETE : Supprimer des lignes**  
  \-- Supprimer avec une condition  
  DELETE FROM nom\_de\_la\_table WHERE statut \= 'inactif';  
  \-- ATTENTION : Oublier la clause WHERE supprimera TOUTES les lignes de la table \!

  \-- Supprimer en utilisant une jointure  
  DELETE p FROM produits p  
  JOIN categories c ON p.categorie\_id \= c.id  
  WHERE c.nom \= 'Obsolète';

### **3\. Définition des Données (LDD \- Langage de Définition de Données)**

* **CREATE : Créer des objets**  
  \-- Créer une base de données avec un jeu de caractères spécifique  
  CREATE DATABASE nom\_de\_la\_base CHARACTER SET utf8mb4 COLLATE utf8mb4\_unicode\_ci;

  \-- Créer une table avec un moteur de stockage et des contraintes  
  CREATE TABLE nom\_de\_la\_table (  
      id INT AUTO\_INCREMENT PRIMARY KEY,  
      nom VARCHAR(100) NOT NULL,  
      email VARCHAR(100) UNIQUE,  
      date\_creation DATETIME DEFAULT CURRENT\_TIMESTAMP,  
      age INT,  
      categorie\_id INT,  
      CHECK (age \>= 18),  
      FOREIGN KEY (categorie\_id) REFERENCES categories(id)  
  ) ENGINE=InnoDB;

* **ALTER TABLE : Modifier la structure d'une table**  
  \-- Ajouter une colonne à une position spécifique  
  ALTER TABLE nom\_de\_la\_table ADD COLUMN prenom VARCHAR(50) AFTER nom;

  \-- Supprimer une colonne  
  ALTER TABLE nom\_de\_la\_table DROP COLUMN nom\_colonne;

  \-- Modifier le type et les contraintes d'une colonne  
  ALTER TABLE nom\_de\_la\_table MODIFY COLUMN nom\_colonne VARCHAR(255) NOT NULL;

  \-- Renommer une colonne  
  ALTER TABLE nom\_de\_la\_table CHANGE COLUMN ancien\_nom nouveau\_nom VARCHAR(120);

  \-- Ajouter/Supprimer une clé primaire ou étrangère  
  ALTER TABLE nom\_de\_la\_table DROP PRIMARY KEY;  
  ALTER TABLE nom\_de\_la\_table ADD PRIMARY KEY (id);  
  ALTER TABLE nom\_de\_la\_table DROP FOREIGN KEY nom\_contrainte\_fk;

* **DROP : Supprimer des objets**  
  \-- Supprimer une table en vérifiant son existence  
  DROP TABLE IF EXISTS nom\_de\_la\_table;

  \-- Supprimer une base de données en vérifiant son existence  
  DROP DATABASE IF EXISTS nom\_de\_la\_base;

* **TRUNCATE TABLE : Vider une table**  
  \-- Plus rapide que DELETE sans WHERE, car elle ne logue pas chaque suppression de ligne.  
  TRUNCATE TABLE nom\_de\_la\_table;

### **4\. Clauses et Opérateurs Courants**

* **WHERE** : Filtre les résultats.  
  * Opérateurs : \=, \!= ou \<\>, \>, \<, \>=, \<=  
  * AND, OR, NOT : Combiner des conditions.  
  * BETWEEN a AND b : Dans un intervalle (inclusif).  
  * IN ('val1', 'val2') : Dans une liste de valeurs.  
  * LIKE : Recherche de motifs (\_ pour un caractère, % pour zéro ou plusieurs).  
  * IS NULL / IS NOT NULL : Vérifier les valeurs NULL.  
  * REGEXP : Recherche par expression régulière. WHERE nom REGEXP '^J';  
* **JOIN** : Combiner des lignes de plusieurs tables.  
  \-- INNER JOIN (seulement les correspondances)  
  SELECT u.nom, c.produit FROM utilisateurs u INNER JOIN commandes c ON u.id \= c.utilisateur\_id;

  \-- LEFT JOIN (tous les utilisateurs, même sans commande)  
  SELECT u.nom, c.produit FROM utilisateurs u LEFT JOIN commandes c ON u.id \= c.utilisateur\_id;

  \-- RIGHT JOIN (toutes les commandes, même sans utilisateur correspondant)  
  SELECT u.nom, c.produit FROM utilisateurs u RIGHT JOIN commandes c ON u.id \= c.utilisateur\_id;

  \-- FULL OUTER JOIN (simulé en MySQL avec UNION)  
  SELECT \* FROM table1 LEFT JOIN table2 ON table1.id \= table2.id  
  UNION  
  SELECT \* FROM table1 RIGHT JOIN table2 ON table1.id \= table2.id;

* **GROUP BY** : Regrouper des lignes pour appliquer des fonctions d'agrégation.  
  SELECT categorie, AVG(prix), COUNT(\*) FROM produits GROUP BY categorie;

* **HAVING** : Filtrer les groupes après l'agrégation.  
  SELECT categorie, AVG(prix) FROM produits GROUP BY categorie HAVING AVG(prix) \> 50;

* **UNION & UNION ALL** : Combiner les résultats de plusieurs SELECT.  
  SELECT nom, email FROM clients UNION SELECT nom, email FROM prospects;

  *(UNION supprime les doublons, UNION ALL les conserve et est plus rapide.)*  
* **DISTINCT** : Retourner uniquement les valeurs uniques.  
  SELECT DISTINCT pays FROM utilisateurs;

### **5\. Fonctions d'Agrégation et Scalaires**

* **Agrégation :**  
  * COUNT() : Compte le nombre de lignes.  
  * SUM() : Somme des valeurs.  
  * AVG() : Moyenne des valeurs.  
  * MIN() / MAX() : Valeur minimale / maximale.  
  * GROUP\_CONCAT() : Concatène les chaînes d'un groupe. SELECT categorie, GROUP\_CONCAT(nom) FROM produits GROUP BY categorie;  
* **Chaînes de caractères :**  
  * CONCAT() : Concatène des chaînes.  
  * LENGTH() : Longueur d'une chaîne.  
  * UPPER() / LOWER() : Met en majuscules / minuscules.  
  * SUBSTRING() : Extrait une sous-chaîne.  
  * TRIM() : Supprime les espaces en début et fin.  
* **Numériques :**  
  * ROUND() : Arrondit un nombre.  
  * CEIL() / FLOOR() : Arrondit au supérieur / inférieur.  
  * ABS() : Valeur absolue.  
* **Dates :**  
  * NOW() / CURDATE() / CURTIME() : Date/heure, date, heure actuelles.  
  * DATE\_FORMAT() : Formate une date.  
  * DATEDIFF() : Différence en jours entre deux dates.

### **6\. Types de Données Courants**

| Catégorie | Type | Description |
| :---- | :---- | :---- |
| **Numérique** | INT, BIGINT | Entiers de différentes tailles. |
|  | DECIMAL(p, s) | Nombre à virgule fixe, idéal pour la finance. p=précision, s=échelle. |
|  | BOOLEAN ou TINYINT(1) | Valeur booléenne (0 pour faux, 1 pour vrai). |
| **Chaîne** | VARCHAR(n) | Chaîne de longueur variable, efficace en espace. |
|  | TEXT | Pour les textes longs comme des articles de blog. |
|  | JSON | Stocke des documents JSON, permet des requêtes sur les clés. |
|  | ENUM | Permet de choisir une valeur parmi une liste prédéfinie. |
| **Date/Heure** | DATETIME | Stocke date et heure. |
|  | TIMESTAMP | Similaire à DATETIME, mais se met à jour automatiquement avec ON UPDATE CURRENT\_TIMESTAMP. |

### **7\. Gestion des Utilisateurs et Permissions (LCD)**

* **Créer un utilisateur :**  
  CREATE USER 'nouvel\_utilisateur'@'localhost' IDENTIFIED BY 'mot\_de\_passe\_solide';

* **Donner des permissions :**  
  \-- Donner tous les privilèges sur une base de données  
  GRANT ALL PRIVILEGES ON nom\_de\_la\_base.\* TO 'utilisateur'@'localhost';

  \-- Donner des privilèges granulaires  
  GRANT SELECT, INSERT, UPDATE ON nom\_de\_la\_base.nom\_de\_la\_table TO 'utilisateur'@'localhost';

* **Retirer des permissions :**  
  REVOKE UPDATE ON nom\_de\_la\_base.\* FROM 'utilisateur'@'localhost';

* **Afficher les permissions d'un utilisateur :**  
  SHOW GRANTS FOR 'utilisateur'@'localhost';

* **Appliquer les changements de privilèges :**  
  FLUSH PRIVILEGES;

* **Supprimer un utilisateur :**  
  DROP USER 'utilisateur'@'localhost';

* **Changer le mot de passe d'un utilisateur :**  
  ALTER USER 'utilisateur'@'localhost' IDENTIFIED BY 'nouveau\_mot\_de\_passe';

### **8\. Transactions**

Les transactions garantissent l'atomicité, la cohérence, l'isolation et la durabilité (ACID). Essentiel pour les opérations financières ou critiques.

* **Démarrer une transaction :**  
  START TRANSACTION;

* **Définir un point de sauvegarde :**  
  SAVEPOINT mon\_point\_de\_sauvegarde;

* **Valider la transaction :**  
  COMMIT;

* **Annuler la transaction :**  
  ROLLBACK;

* **Annuler jusqu'à un point de sauvegarde :**  
  ROLLBACK TO mon\_point\_de\_sauvegarde;

### **9\. Index**

Les index sont des structures de données qui améliorent la vitesse des opérations de récupération de données sur une table de base de données.

* **Créer un index :**  
  \-- Index simple pour accélérer les recherches et les jointures  
  CREATE INDEX idx\_nom ON nom\_de\_la\_table (nom);

  \-- Index unique pour garantir l'unicité des valeurs  
  CREATE UNIQUE INDEX uidx\_email ON nom\_de\_la\_table (email);

  \-- Index composite sur plusieurs colonnes  
  CREATE INDEX idx\_nom\_prenom ON nom\_de\_la\_table (nom, prenom);

* **Afficher les index d'une table :**  
  SHOW INDEX FROM nom\_de\_la\_table;

* **Supprimer un index :**  
  DROP INDEX idx\_nom ON nom\_de\_la\_table;

### **10\. Vues, Procédures Stockées et Triggers**

* **Vues (Views) :** Une table virtuelle basée sur le jeu de résultats d'une instruction SQL.  
  \-- Créer une vue  
  CREATE VIEW vue\_clients\_actifs AS  
  SELECT id, nom, email FROM clients WHERE est\_actif \= 1;

  \-- Interroger la vue comme une table normale  
  SELECT \* FROM vue\_clients\_actifs;

* **Procédures Stockées (Stored Procedures) :** Un ensemble d'instructions SQL précompilées qui peuvent être exécutées en un seul appel.  
  DELIMITER //  
  CREATE PROCEDURE ObtenirClientsParPays(IN pays\_nom VARCHAR(100))  
  BEGIN  
      SELECT \* FROM clients WHERE pays \= pays\_nom;  
  END //  
  DELIMITER ;

  \-- Appeler la procédure  
  CALL ObtenirClientsParPays('France');

* **Déclencheurs (Triggers) :** Une procédure stockée qui s'exécute automatiquement lorsqu'un événement (INSERT, UPDATE, DELETE) se produit sur une table.  
  DELIMITER //  
  CREATE TRIGGER avant\_update\_produit  
  BEFORE UPDATE ON produits  
  FOR EACH ROW  
  BEGIN  
      INSERT INTO log\_produits(produit\_id, ancien\_prix, nouveau\_prix, date\_modif)  
      VALUES(OLD.id, OLD.prix, NEW.prix, NOW());  
  END //  
  DELIMITER ;  
