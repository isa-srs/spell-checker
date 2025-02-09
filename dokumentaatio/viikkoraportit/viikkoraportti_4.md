# Viikkoraportti 4

Damerau-Levenshtein -etäisyysmitta huomioi kahden vierekkäisen kirjaimen päittäisyyden (transposition) yhtenä virheenä, esimerkiksi merkkijonoissa "abcd" ja "abdc". En ollut tehnyt tätä aiemmin, joten tällä viikolla päivitin ```damerau_levenshtein``` -metodin siten, että tämä transposition huomioidaan myös.

Otin tällä viikolla lisäksi käyttöön invoke-taskit sekä pylintin laaduntarkastusta varten. 

Minulla oli aluksi paljon vaikeuksia täysin ymmärtää etäisyysmitan vierekkäisten kirjainten vaihto ja miten toteuttaisin sen. Sain sen lopulta toteutettua ja koen nyt ymmärtäväni etäisyysmitan täysin. Ainakin paremmin kuin aiemmin kurssin aikana.

Seuraavaksi lähden ainakin etsimään jotakin kunnollista laajaa sanastoa ja rakennan trie-tietorakenteen, joka oli tämän viikon tavoite, mutta jäi. Haluan myös kehittää hieman käyttöliittymää, vähintään siten, mikä uusien ominaisuuksien myötä on triviaalia (esim. mitä käyttäjältä pyydetään syöttämään). Aion myös edistää dokumentaatiota ja aloittaa testauksen.

Käytetyt tunnit: 8