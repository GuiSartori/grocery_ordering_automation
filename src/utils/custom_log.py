from datetime import datetime
import os

# Function for Log Creation
def log_create(nome_arquivo_py):
    global nome_arquivo_log
    # Get the current date and time
    datetime_atual = datetime.now()

    # Creates the folder where the log will be stored
    os.makedirs(f"logs/{nome_arquivo_py}", exist_ok=True)

    # Format the date of log name
    data_hora_formatada = datetime_atual.strftime("%d-%m-%y_%H-%M-%S")

    # Save the name of the log file
    nome_arquivo_log = f"logs/{nome_arquivo_py}/{data_hora_formatada}.txt"

    # Create log with Datetime as a file name
    log = open(nome_arquivo_log, "a")
    log.close()  # Close the file after creation

# Function for append in log
def log_append(message):
    global nome_arquivo_log
    # Format Datetime to Timestamp on Log
    datetime_stamp = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

    # Log message with Timestamp
    mensagem = f"({datetime_stamp}) - {message}"

    # Add the message to the log
    with open(nome_arquivo_log, "a") as log:
        log.write(mensagem + '\n')