tarefas = []

def adicionar_tarefa(nome, descricao, categoria, prioridade):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "status": "pendente"
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa registrada.")
    else:
        for tarefa in tarefas:
            print(f"\nNome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nCategoria: {tarefa['categoria']}\nPrioridade: {tarefa['prioridade']}\nStatus: {tarefa['status']}\n")

def listar_por_categoria(categoria):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['categoria'].lower() == categoria.lower()]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"\nNome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nCategoria: {tarefa['categoria']}\nPrioridade: {tarefa['prioridade']}\nStatus: {tarefa['status']}\n")
    else:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")

def listar_por_prioridade(prioridade):
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['prioridade'].lower() == prioridade.lower()]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"\nNome: {tarefa['nome']}\nDescrição: {tarefa['descricao']}\nCategoria: {tarefa['categoria']}\nPrioridade: {tarefa['prioridade']}\nStatus: {tarefa['status']}\n")
    else:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")

def marcar_como_concluida(nome):
    for tarefa in tarefas:
        if tarefa['nome'].lower() == nome.lower():
            tarefa['status'] = 'concluída'
            print(f"Tarefa '{nome}' marcada como concluída!")
            return
    print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['nome'].lower() != nome.lower()]
    print(f"Tarefa '{nome}' removida com sucesso.")

def menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Listar tarefas por categoria")
    print("4. Listar tarefas por prioridade")
    print("5. Marcar tarefa como concluída")
    print("6. Remover tarefa")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome da tarefa: ")
        descricao = input("Digite a descrição da tarefa: ")
        categoria = input("Digite a categoria da tarefa: ")
        prioridade = input("Digite a prioridade (baixa, média, alta): ")
        adicionar_tarefa(nome, descricao, categoria, prioridade)
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        categoria = input("Digite a categoria para filtrar: ")
        listar_por_categoria(categoria)
    elif opcao == '4':
        prioridade = input("Digite a prioridade para filtrar (baixa, média, alta): ")
        listar_por_prioridade(prioridade)
    elif opcao == '5':
        nome = input("Digite o nome da tarefa para marcar como concluída: ")
        marcar_como_concluida(nome)
    elif opcao == '6':
        nome = input("Digite o nome da tarefa para remover: ")
        remover_tarefa(nome)
    elif opcao == '7':
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    print("Bem-vindo ao Gerenciador de Tarefas (modo temporário - sem salvamento)")
    while True:
        menu()
