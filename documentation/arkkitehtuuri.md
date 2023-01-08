# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmikerroksista kerrosarkkitehtuuria ja sen pakkauskaavio on seuraava:

<img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/package.png" width="300">

## Käyttöliittymä
 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/create_user_and_login.png" width="300">
 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/transactions.png" width="300">


## Sovelluslogiikka 


#### Kerroskuvaus

<img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/package_diagram.drawio.png" width="500">

###### Tietomalli, Luokat

Luokat 'User' ja 'Transaction'

```mermaid
 classDiagram
      Transaction "*" --> "1" User
      class User{
          username
          password
      }
      class Transaction{
          user_id
          subject
          amount
      }
```


###### Database: SQLite3

Tietokanta alustetaan README.md:n mukaisesti.

## Päätoiminnallisuudet

#### Käyttäjätilin luominen

Käyttäjätilin luominen näyttää sekvenssikaaviona tältä. 

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
    database-->>UserRepository: result OK
    UserRepository->>UserService: {authenticated}
    UserService-->>UI: redirect /transactionView
    UI-->User: see TransactionView (when successful)
```


Käyttäjätilille kirjautuminen:

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepository
    participant database
    User->>UI: Click "Login user"
    UI->>UserService: login("username1", "passw1")
    UserService->>UserRepository: login(user)
    UserRepository->>database: SELECT * FROM users WHERE username=username1
    database-->>UserRepository: result
    UserRepository->>UserService: {authenticated}
    UserService-->>UI: redirect /transactionView
    UI-->User: see Transaction view
```

Budjettinäkymän näyttäminen:

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant TransactionService
    participant TransactionRepository
    participant database
    UI->>TransactionService: _show_transaction_view(self)
    UI->>TransactionService: _handle_get_transactions(self, user)
    TransactionService->>TransactionRepository: get_transactions(self, username)
    TransactionRepository->>database: SELECT * FROM transactions WHERE user_id = username
    database-->>TransactionRepository: return transactions (successful)
    TransactionRepository->>TransactionService: return transactions
    TransactionService-->>UI: return transactions
    UI-->User: show Transaction view
```

Uuden menon tai tulon tallennus: