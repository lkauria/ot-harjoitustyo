# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kolmikerroksista kerrosarkkitehtuuria ja sen pakkauskaavio on seuraava:

<img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/package.png" width="800">

UI sisältää käyttöliitymästä vastaavan koodin, services sisältää sovelluslogiikasta ja repositories tiedon tallennuksesta vastaavan koodin. Kerroskuvauskohdassa kuvataan kerrosten luokat ja sisältö tarkemmin.

## Käyttöliittymä

Käyttöliittymä sisältää kolme eri näkymää: kirjautuminen, käyttäjätilin luominen ja budjettinäkymä.

 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/create_user_and_login.png" width="300">
 <img src="https://github.com/lkauria/ot-harjoitustyo/blob/main/documentation/pictures/transactions.png" width="300">

Jokaiselle näistä on tehty omat luokat: Login_view.py, create_user_view.py ja transaction_view.py. Käyttöliittymä on eriytetty sovelluslogiikasta ja tallennuslogiikasta.

## Sovelluslogiikka 

Sovelluksen loogisen tietomallin muodostavat käyttäjään ja tuloihin/menoihin jakautuvat luokat, User- ja Transaction-luokat. Myös sovelluslogiikan jako on tehty näiden kahden luokan mukaisesti. 

User service -luokka pitää sisällään käyttäjään liittyvän logiikan, kuten käyttäjätilin luominen ja kirjautuminen. Transaction service -luokka taas huolehtii tulojen ja menojen lisäyksestä budjettiin sekä niiden näyttämisestä käyttäjäkohtaisesti.

Nämä Service-luokat eli sovelluslogiikasta huolehtivat luokat ovat yhteydessä Repository-luokkiin eli luokkiin, jotka huolehtivat tiedon pysyväistalletuksesta.

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

Tietokanta alustetaan README.md:n mukaisesti. Repositories-luokat UserRepository ja TransactionRepository tallettavat tietokantaan tiedot. Molempien repositorioiden tallennus tapahtuu SQLite-tietokantaan, jossa on kaksi erillistä tietokantataulua, users ja transactions.


## Päätoiminnallisuudet

Sovelluksen päätoiminnallisuuksia ovat kirjautuminen, käyttäjätilin luominen sekä tulojen ja menojen näyttäminen sekä kirjaus.

### Käyttäjätilin luominen

Käyttäjä luo käyttäjätilin käyttäjätilin luomissivulla syöttämällä käyttäjätunnuksen ja salasanan. Tässä sekvenssikaaviossa kuvataan käyttäjätilin luonti


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


### Käyttäjän kirjautuminen

Käyttäjä kirjautuu kirjautumissivulla syöttämällä käyttäjätunnuksen ja salasanan. Tässä sekvenssikaaviossa kuvataan kirjautuminen.

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

### Budjettinäkymän näyttäminen:

Käyttäjä kirjauduttuaan sovellukseen näkee hänen kirjaamansa menot ja tulot sekä niiden summan. 

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

## Ohjelmaan jääneet heikkoudet

### Käyttöliittymä

Menon tai tulon kirjaamisessa ei näy käyttöliittymässä virhetilannetta, vaikka sovellus ei suostukaan tallentamaan summaa, joka ei ole kokonaisluku tai jos summa tai aihe on tyhjä. 

Tkinterissä ei saisi käyttää grid() ja pack() -metodeita samassa ikkunassa yhtä aikaa, mutta taulukon näyttäminen tässä ajassa ei onnistunut ilman, että molempia on käytetty. Tästä syystä taulukko on väärässä sijainnissa suunnitteluun nähden.