# Käyttöohje

Projektinhallinta on toteutettu Poetryn avulla ja sovellusta on testattu Pythonin versiolla 3.10, joten vanhempien versioiden kanssa saattaa esiintyä ongelmia.


## Komentorivikomennot

Ohjelma käynnistyy komennolla:

```poetry run invoke start```

Koodin laadun voi tarkistaa komennolla:

```poetry run invoke lint```

Testikattavuusraportin voi generoida komennolla:

```poetry run invoke coverage-report```

...ja testikattavuusraportin voi avata komennolla:

```xdg-open htmlcov/index.html```


## Sovelluksen käyttöohjeet

Ohjelma on täysin komentorivisovellus ja kaikki toiminnallisuus tapahtuu komentoriviltä. Jokaisen toiminnon käyttäminen toimii kirjoittamalla toimintoa vastaavan syötteen ja painamalla enteriä.

Ohjelman käynnistyksen jälkeen käyttäjälle esitetään kolme toimintoa, jotka voi valita syöttämällä toimintoja vastaavan numeron (1, 2, 3 tai tyhjä syöte).

Syöttämällä numeron 1 käyttäjä pääsee kirjoittamaan sanan, jolloin ohjelma tarkistaa sen oikeinkirjoituksen ja ilmoittaa sanan joko olevan oikeinkirjoitettu tai ehdottaa toista sanaa.

Syöttämällä numeron 2 käyttäjä pääsee lisäämään sanastoon uuden sanan.

Syöttämällä numeron 3 tai tyhjän syötteen (painaa pelkkää enter-nappia), ohjelma sulkeutuu.