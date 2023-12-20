import datetime
def obter_data_hoje():
    data_hoje = datetime.date.today()
    return data_hoje
data_hoje = obter_data_hoje()

print( "Data hoje:", data_hoje )
