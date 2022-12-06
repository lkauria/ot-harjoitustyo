# Arkkitehtuurikuvaus

## Rakenne
- Tähän kuva kerrosarkkitehtuurista

## Käyttöliittymä
- Lisätään, kun valmiimpi 


## Sovelluslogiikka 


#### Kerroskuvaus

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
