# Käyttöohje

Projektin viimeisin julkaisu löytyy täältä: [release](https://github.com/lkauria/ot-harjoitustyo/releases) lähdekoodi

## Ohjelman lataaminen Githubista ja käynnistäminen

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

## Kirjautuminen ja käyttäjätilin luonti

Ensimmäisessä näkymässä voit kirjautua olemassa olevalla käyttäjätunnuksella ja salasanalla. Jos sinulla ei ole vielä käyttäjätunnusta, paina "Luo uusi käyttäjätunnus". Tästä pääset näkymään, jossa voit syöttää käyttäjättunnuksen ja salasanan samaan tapaan kuin kirjautuessa. 

Jos tilin rekisteröinti onnistuu eli kukaan muu ei ole valinnut samaa käyttäjätunnustä, pääset kirjautuneen näkymään.

## Budjettinäkymä ja tulon tai menon lisäys

Kirjauduttuasi sovellukseen, näet oman budjettisi. Tähän voit lisätä joko menoja tai tuloja syötekenttiä käyttäen. Huomioi, että summan pitää olla kokonaisluku ja et syötä etumerkkiä, koska valitset syöttämiseen joko tulon tai menon. Molempien kenttien täytyy sisältää arvo tai tallentaminen ei tapahdu.
