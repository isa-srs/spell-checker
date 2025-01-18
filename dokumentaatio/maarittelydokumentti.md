# Vaatimusmäärittely

Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma

Aiheena on kirjoitusvirheiden korjaaja. Työ toteutetaan Pythonilla ja dokumentaatio suomeksi. Pystyn vertaisarvioimaan myös englanninkielisiä projekteja.

Lähtökohtana on toteuttaa materiaalissa ehdotetut trie-tietokanta ja Damerau-Levenshtein -etäisyysmitta.

Ohjelmalle annetaan väärinkirjoitettu sana, minkä jälkeen sitä verrataan trie-rakenteeseen tallennettuihin oikeinkirjoitettuihin sanoihin. Ohjelma etsii syötettyyn sanaan verrattuna lyhimmällä etäisyydellä olevan sanan, joka sitten palautetaan käyttäjälle. Ohjelman ydin on etäisyyden mittaaminen syötteen ja tallennettujen sanojen välillä.

Pahimmassa tapauksessa trie-tietorakenteen aika- ja tilavaativuudet ovat O(n). Damerau-Levenshtein -etäisyyden mittaamisen vaativuudet ovat taas O(M*N).

Lähteet: 

- [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [Damerau-Devenshtein distance, Wikipedia](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)