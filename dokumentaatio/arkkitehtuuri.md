# Arkkitehtuurikuvaus

## Rakenne
- Tähän kuva kerrosarkkitehtuurista

## Käyttöliittymä
 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/create_user_and_login.png" width="300">
 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/transactions.png" width="300">


## Sovelluslogiikka 


#### Kerroskuvaus

<img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package_diagram_drawio.png" width="500">

###### Tietomalli, Luokat

Luokat 'User' ja 'Transaction'

```mermaid
 classDiagram
      Transaction "*" --> "1" User
      class User{
          id
          username
          password
      }
      class Transaction{
          id
          user_id
          subject
          sum
          date_of_transaction
      }
```


###### Database: SQLite3



## Päätoiminnallisuudet

#### Käyttäjätilin luominen

Käyttäjätilin luominen näyttää sekvenssikaaviona tältä. Viimeistä LoginView'hun uudelleenohjausta ei ole vielä toteutettu.

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    participant database
    User->>UI: Click "Create user"
    UI->>UserService: create_user("username1", "passw1")
    UserService->>UserRepository: create_user(user)
    UserRepository->>database: INSERT INTO users
    database-->>UserRepository: result
    UserRepository->>UserService: {authenticated}
    UserService-->>UI: redirect /loginView
    UI-->User: see LoginView 
```
