---
theme: "white"
---

<style>
    .reveal h1 {
        font-size: 1.25em;
        color: #666666;
    }

    .reveal li {
        font-size: 0.8em;
    }

    .reveal code {
        background-color: #66b3ff;
        color: #000000;
        padding: 0.2em 0.25em 0.2em 0.25em;
    }

    .language-bash {
        background-color: #000000;
        color: #00ff00;
    }
</style>

# INSTALLAZIONE

---

# forma artistica in cui `MEDIA` diversi occupano uno spazio comune

---

# costruiremo un dispositivo in grado di `SENTIRE` delle gocce d'acqua cadere su una ` SUPERFICIE `...

--

![](acqua01/01_goccia.jpg)

---

# ...E DI `INNESCARE` DEGLI `EVENTI` OGNI VOLTA CHE UNA GOCCIA VIENE CAPTATA

---

# GLI EVENTI SARANNO `SUONI` E `VOCI` REGISTRATE...
# ...CHE LEGGONO E RECITANO PAROLE E FRASI SUL TEMA DELL'`ACQUA` {: .fragment}

---

# <div style="text-align: right"> liquido </div>
## <div style="text-align: left"> bere </div>
### <div style="text-align: center"> limpida </div>
# <div style="text-align: justify"> sommergere </div>
##### <div style="text-align: center; padding: 2em 3em 0.2em 0.25em;"> potabile </div>
### <div style="text-align: right; padding: 2em 3em 0.2em 0.25em;"> lavare </div>
# <div style="text-align: left"> ... </div>

---

# COSTRUIREMO DIVERSE `POSTAZIONI` NELLO SPAZIO

---

# OGNUNA DELLE QUALI COMPOSTA DA UN `DEFLUSSORE`
<img src=acqua01/03_deflussore.jpg width=250 height=250 /> {: .fragment}

--

# CHE PERMETTERA' ALL'ACQUA DI UNA BOTTIGLIA DI PLASTICA DI SCENDERE A `GOCCE`

---

# LE GOCCE CADRANNO SU UNA SUPERFICIE COLLEGATA A UN `MICROFONO A CONTATTO`
<img src=\acqua01/04_piezo.jpg width=300 height=400 /> {: .fragment}

---

# CHE ATTRAVERSO UNA SCHEDA `ARDUINO` INVIERA' UN SEGNALE AL COMPUTER
<img src=\acqua01/05_wemos.jpg width=350 height=400 /> {: .fragment}

---

# DOVE `PUREDATA` SI OCCUPERA' DI GESTIRE LE NOSTRE VOCI E I NOSTRI SUONI

--

<img src=\acqua01/07_tutto_b.png />

---

# FLUSSO DI LAVORO

---

# Testi 
1. scelta e compilazione {: .fragment}
2. registrazione {: .fragment}
3. editing e pulizia {: .fragment}
4. sequencing {: .fragment}

---

# Arduino
1. Costruzione del dispositivo (cavi, piezo, led, *inscatolamento*) {: .fragment}
2. Scrittura del codice (Arduino IDE) {: .fragment}

---

# Suoni
1. Che suoni? (suoni d'acqua, sintesi per modelli fisici, etc...) {: .fragment}
2. Costruzione della *patch* con **puredata** {: .fragment}

---

# Parte meccanica e assemblaggio
1. Costruzione {: .fragment} 
2. Collegamento di tutte le parti {: .fragment}
3. Messa in moto! {: .fragment}