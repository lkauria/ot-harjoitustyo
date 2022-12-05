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

Tähän sekvenssikaavioina käyttäjätarinoiden läpikäynti