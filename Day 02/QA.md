# Domande per il quiz finale

## Domande vero/falso

*Scegliere un po' di queste domande, ho cercato di crearle attingendo dai miei riassunti, così i ragazzi rispondono a cose che ho ripetuto almeno una volta nel corso della lezione*.

1. Scattare una fotografia equivale ad effettuare una proiezione da 3 dimensioni in 2 dimensioni
2. La codifica delle immagini RGB è acronimo di Rosso Giallo Blu, i 3 colori base
3. I monitor sono in grado di combinare i 3 colori base della codifica RGB a formare una buona parte dei colori dello spettro del visibile
4. Si può pensare a una correlazione o convoluzione come far scorrere una finestrella (filtro) su un'immagine pixel per pixel
5. La correlazione o convoluzione sostituisce un pixel con un prodotto dei pixel del suo vicinato
6. Il filtro mediano è particolarmente indicato per la riduzione di rumore
7. L'ideale per l'individuazione dei punti chiave è che questi vengano riconosciuti solo in particolari condizioni d'illuminazione
8. La tecnica di individuazione dei punti chiave "SIFT" si basa sull'individuazione di detti punti chiave, a cui viene aggiunta una descrizione del vicinato per ogni punto
9. Una relazione lineare fra due variabili non è esprimibile geometricamente con una retta
10. L'obiettivo della classificazione è, in parole povere, di trovare una "forma" che separi i punti delle varie classi
11. Nelle reti neurali, l'input e l'output sono inframmezzati da strati intermedi detti strati nascosti
12. Lo strato di output di una rete neurale è composto sempre e solo da un singolo neurone
13. La scelta della funzione di attivazione non è importante al fine del successo della rete neurale
14. L'obiettivo dell'addestramento delle reti neurali è la massimizzazione di una funzione detta di perdita
15. La discesa del gradiente garantisce sempre l'identificazione dei migliori parametri possibili per la rete neurale
16. Il fatto che le reti neurali convoluzionali hanno questo nome è fuorviante: non esiste infatti alcun collegamento con le convoluzioni che venivano usate nella visione artificiale storica per identificare le *feature*
17. Le reti neurali convoluzionali sono in grado di identificare *feature* di basso livello e a combinare queste ultime in *feature* di più alto livello utili alla classificazione di un'immagine
18. Le reti generative avversarie (GAN) sono composte da due reti neurali in competizione l'una con l'altra

## Lettura di un diagramma di rete neurale

![rete neurale](NN.png)

Dato lo schema di una rete neurale sopra, indica

1. Quanti neuroni contiene lo strato di input
2. Quanti neuroni contiene lo strato di output
3. Quanti strati intermedi sono presenti nella rete neurale

Indica la risposta corretta alle domande qui sotto:

4. La rete neurale in figura
   - [ ] può essere utilizzata per un problema di classificazione a 3 classi
   - [ ] è una rete neurale convoluzionale
   - [ ] produce un output più piccolo dell'input
   - [ ] è una GAN
5. Nel secondo strato nascosto della rete in figura
   - [ ] ogni neurone ha 5 connessioni in ingresso e 4 in uscita
   - [ ] non è specificata la funzione di attivazione
   - [ ] non è indicata la presenza di termini di *bias*
   - [ ] tutte le opzioni di cui sopra