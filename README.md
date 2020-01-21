# Sistemi, tecnologie, applicazioni e linguaggi di programmazione per la multimedialità

# Apertura di Anaconda:

Aprire il programma *Anaconda Navigator* con la seguente icona:

<img src="/immagini/01_navigator.png" width="200" class="center">

Una volta all'interno, aprire il programma *Jupyter*, premendo il pulsante ***Launch*** sotto la rispettiva icona:

<img src="/immagini/02_jupyter.png" width="200">

Nella nuova finestra cercare e aprire con un click la cartella **Documents** e successivamente cercare e aprire la cartella **sistemi_slides**. A questo punto dovreste trovarvi all'interno della cartella suddetta, che contiene il file **slides_01.ipynb**, come in figura:

<img src="/immagini/03_file_ipynb.png" width="200">

Aprite il file e vi troverete nell'ambiente per scrivere le slides.

<img src="/immagini/04_ambiente_jupyter.png" width="200">

Attivate la modalità **slideshow** dal menu **View/Cell Toolbar/Slideshow**:

<img src="/immagini/08_slideshow.png" width="200">

La modalità **slideshow** vi consente di scegliere il tipo di slide da generare, tramite il menu a tendina sulla destra:

<img src="/immagini/10_slides.png" width="200">

Le *celle*, cioè gli spazi che conterranno le slides, sono gli elementi fondamentali dell'ambiente jupyter. Una cella può trovarsi in uno dei seguenti stati:
- *edit mode* (varde) che si attiva col tasto **INVIO**
- *command mode* (blu) che si attiva col tasto **ESC**

Per poter scrivere all'interno delle celle usando il linguaggio **markdown** è necessario che la cella sia abilitata alla scrittura in markdown, scegliendo la voce omonima dal menu a tendina come in foto:

<img src="/immagini/05_markdown.png" width="200">

N.B. si può abilitare il markdown sulla cella anche con il tasto **m** quando la cella è in *command mode*

Scrivete un testo all'interno di una cella (in *edit mode*), magari preceduto da un segno #:

<img src="/immagini/06_testo.png" width="200">

poi **eseguite** la cella premendo **CTRL**+**INVIO**, vedrete la cella con il comando markdown *eseguito*:

<img src="/immagini/07_testo_exec.png" width="200">

Premete **b** per creare una nuova cella e scrivete nuovo testo ed eseguite, e così via...

Infine create il file Html attraverso tramite il menu **File/Download as/Reveal.js slides**

<img src="/immagini/09_export_html.png" width="200">









## Download e installazione del software

### Chromium

[https://download-chromium.appspot.com/](https://download-chromium.appspot.com/)

### Anaconda

[https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)

### MuseScore

[https://musescore.org/it/download](https://musescore.org/it/download)

### Reaper

[https://www.reaper.fm/download.php](https://www.reaper.fm/download.php)

### Purr Data

[https://github.com/agraef/purr-data/releases](https://github.com/agraef/purr-data/releases)

### Arduino

[https://www.arduino.cc/en/Main/Software](https://www.arduino.cc/en/Main/Software)

```
jupyter nbconvert name.ipynb --to slides
```
