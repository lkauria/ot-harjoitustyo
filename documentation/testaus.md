# Testausdokumentti

Ohjelmaa on testattu kevyesti unitest-yksikkötesteillä. Yksikkötestejä oli suunnitelmissa tehdä enemmän ja monipuolisesti, mutta testaus jäi hyvin vähäiseksi.

### Sovelluslogiikka

Sovelluslogiikka luokalle User service ja Transaction ovat testattu. Testejä on vain kahdeksan kappaletta.

Testit voi ajaa seuraavalla skriptillä:

```zsh
poetry run invoke test
```

### Testauskattavuus

Testauskattavuus raportin mukaan on hyvin korkea, jopa 99 %. Epäilen tätä tulosta, koska testini eivät ole omasta mielestäni kovin kattavia.

Testikattavuuden voi ajaa seuraavalla skriptillä:

```zsh
poetry run invoke coverage-report
```