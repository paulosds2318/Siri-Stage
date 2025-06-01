def listar_vagas(): # Lista todas as vagas cadastradas
    return carregar_vagas() # Retorna a lista de vagas carregadas do arquivo JSON

def remover_vaga(vaga_id): # Remove uma vaga específica pelo ID
    vagas = carregar_vagas() # Carrega as vagas existentes
    vagas_filtradas = [vaga for vaga in vagas if str(vaga.get("id")) != str(vaga_id)] # Filtra as vagas que não têm o ID fornecido

    if len(vagas) == len(vagas_filtradas): # Verifica se alguma vaga foi removida
        return False
    
    salvar_vagas(vagas_filtradas) # Salva as vagas filtradas no arquivo JSON
    return True

def editar_vaga(vaga_id, novos_dados): # Edita os dados de uma vaga específica pelo ID
    vagas = carregar_vagas() # Carrega as vagas existentes
    vaga_encontrada = False # Variável para verificar se a vaga foi encontrada

    for vaga in vagas: # Itera sobre as vagas para encontrar a vaga com o ID fornecido
        if vaga["id"] == vaga_id: # Verifica se o ID da vaga corresponde ao ID fornecido
            vaga_encontrada = True # Marca que a vaga foi encontrada
            vaga.update(novos_dados) # Atualiza os dados da vaga com os novos dados fornecidos
            break
    
    if vaga_encontrada: # Se a vaga foi encontrada, salva as alterações
        salvar_vagas(vagas)
        return True
    else:
        return False