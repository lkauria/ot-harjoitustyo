# ot-harjoitustyo
Sovellus auttaa käyttäjää budjetoimaan esimerkiksi projektinsa. Sovellukseen luodaan käyttäjätili ja kirjautunut käyttäjä näkee oman budjetin menonsa ja tulonsa.

- [Viimeisin release](https://github.com/lkauria/ot-harjoitustyo/releases/tag/loppupalautus)

## Python-versio

Sovellus on ohjelmoitu Python-versiota 3.8 käyttäen ja sitä ei ole testattu muilla Python-versioilla. Poetrysta on käytössä versio 1.2.2. Python ja Poetry pitää molemmat olla asennettuna ennen tämän sovelluksen asennusohjeita.

## Dokumentaatio

- [Vaatimusmäärittely](./documentation/vaatimusmaarittely.md)
- [Changelog](./documentation/changelog.md)
- [Työaikakirjanpito](./tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](./documentation/arkkitehtuuri.md) 
- [Käyttöohje](./documentation/kayttoohje.md) 
- [Testaus](./documentation/testaus.md) 

## Asennus

1. Kloonaa repositorio gitistä
```zsh
git clone git@github.com:lkauria/ot-harjoitustyo.git
```

2. Asenna projektin riippuvuudet, kun olet projektin juuressa
```zsh
poetry install
```

3. Tietokannan alustus (SQLite)
```zsh
poetry run invoke database 
```

4. Käynnistä sovellus hyödyntäen valmiita Invoke-taskeja
```zsh
poetry run invoke start
```

## Komentorivitoiminnot 

Ohjelman käynnistäminen

 ```bash
poetry run invoke start
```

#### Testaus

Testien ajaminen

```bash
poetry run invoke test
```

#### Testikattavuus

Testikattavuusraportin luonti. Luonnin jälkeen näet, mistä voit html-raportin avata.

```bash
poetry run invoke coverage-report
```

#### Koodin siisteys

Pylintillä tarkistetaan koodin siisteys määritellyillä säännöillä [.pylintrc](./.pylintrc)

```bash
poetry run invoke pylint
```
