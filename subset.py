def elabora_dati(input_file):
    # Inizializza una lista vuota per contenere i risultati
    risultati = []

    # Apri il file in modalità di lettura
    with open(input_file, 'r') as file:
        # Leggi ogni riga nel file
        for riga in file:
            # Dividi la riga in una lista di numeri
            numeri = [int(numero) for numero in riga.split()]

            # Esegui qui la tua logica di elaborazione dei dati
            # Puoi usare la variabile 'numeri' per accedere ai dati di ogni riga
            # Esempio: risultato = sum(numeri)

            # Aggiungi il risultato alla lista dei risultati
            # risultati.append(risultato)

    # Restituisci la lista dei risultati
    return risultati

# Sostituisci 'input.txt' con il tuo percorso e nome file effettivo
percorso_file_input = 'input.txt'
risultati = elabora_dati(percorso_file_input)

# Stampa i risultati (modifica questo secondo le tue esigenze)
for risultato in risultati:
    print(risultato)
