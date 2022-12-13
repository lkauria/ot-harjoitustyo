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

3. Käynnistä sovellus hyödyntäen valmiita Invoke-taskeja
```zsh
poetry run invoke start
```

## Kirjautuminen ja rekisteröinti

Ensimmäisessä näkymässä voit kirjautua olemassa olevalla käyttäjätunnuksella ja salasanalla. Jos sinulla ei ole vielä käyttäjätunnusta, paina "Luo uusi käyttäjätunnus". Tästä pääset näkymään, jossa voit syöttää käyttäjättunnuksen ja salasanan samaan tapaan kuin kirjautuessa. 

Jos rekisteröinti onnistuu eli kukaan muu ei ole valinnut samaa käyttäjätunnustä, pääset kirjautuneen näkymään.

