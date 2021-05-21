# WATER DROPS

Installazione interattiva pensata per la giornata mondiale dell'acqua (30 marzo). 
L'idea è quella di *captare* delle gocce d'acqua che si infrangono su una superficie innescando degli eventi audio e dei segnali luminosi.

## Panoramica 

La struttura di base (che chiamiamo *cascata*) è costituita da un deflussore sospeso su un'asta microfonica che genera delle gocce d'acqua con una frequenza di caduta regolabile. 

Le gocce, contattando la superficie di caduta, mettono in azione le membrane di un microfono piezoelettrico che genera un segnale elettrico elaborato da una scheda arduino, al fine di gestire la luminosità di un diodo e di innescare degli eventi audio che risiedono su un computer: si tratta di voci registrate (per l'occasione), *field recordings* (oceani, fiumi, pioggia) e suoni di sintesi (*synthetic drops*).

## Tecnologie

Le aree tecnologiche coinvolte nella realizzazione del sistema sono state molteplici:
- meccaniche:
  - deflussore
- acustiche:
  - speaker
  - mixer
  - microfoni
- digitali:
  - computer
    - software di registrazione/riproduzione audio
    - software di gestione algoritmica di eventi audio
  - physical computing
    - arduino
    - sensori piezoelettrici
    - diodi luminosi
    - comunicazione seriale


## Realizzazione

L'installazione è stata realizzata durante tutto il corso e ha previsto le seguenti fasi realizzative:

- Concezione
  - scelta delle voci
  - scelta delle *frasi* (non utilizzate)
  - proposta di registrare anche dei suoni strumentali da utilizzare (non concretizzata perché entrati in zona rossa) 
- Registrazione:
  - registrazione delle voci in aula 40:
    - microfono a condensatore AKG C414B (gentilmente offerto da conservatorio)
    - frequenza di campionamento: 44100 hz
    - depth: 16 bit
    - software: Logic Pro
    - la registrazione è avvenuta in due sessioni separate (causa distanziamento)
  - pulizia delle registrazioni (riduzione del rumore, e minima compressione)
  - posizionamento delle parole a distanza di 88200 campioni (2 secondi) l'una dall'altra (software ocenaudio)
  - unificazione delle voci in un unico file
- Arduino:
  - panoramica della piattaforma
  - accensione di un led
  - accensione di due led
  - comunicazione con il computer tramite trasmissione seriale (oggetto **Serial**)
  - uso di un pulsante per gestire l'accensione di un led
  - il microfono a contatto (piezoelettrico)
  - implementazione dello **sketch** (così viene chiamato il codice sorgente di un programma per arduino):
    - gestione del piezoelettrico
    - gestione del led bianco (che si accende quando il piezoelettrico *sente* la goccia d'acqua e *sfuma* grazie al PWM)
- Pure Data
  - panoramica del software di gestione delle voci e dei suoni
  - panoramica sulla **patch** (così si chiama un programma per Pure Data):
    - gestione del file audio con le voci (un *puntatore* si sposta casualmente su multipli di 2 secondi per scegliere la parola da eseguire)
    - gestione dei suoni ambientali
    - spazializzazione del suono (in base alla posizione delle 3 postazioni)
- Struttura fisica:
  - Cascata di gocciolamento:
    - asta microfonica di sostegno
    - *deflussore* con regolazione della frequenza di gocciolamento
    - scatola trasparente di raccolta acqua
    - piastra di sostegno per i microfoni
  - Montaggio in aula 40 il giorno 15 Maggio 2021
    - sono state realizzate 3 cascate, ognuna con la sua arduino e il suo microfono a contatto
    - i microfoni a contatto sono stati (lungamente) tarati per captare le gocce e non i rumori interferenti
- Ripresa Video
  - il giorno della realizzazione sono state fatte riprese video dell'installazione
  - ...e montate in un video di *testimonianza* 