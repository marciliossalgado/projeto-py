def adicionar_tarefa(tarefas, nome, descricao, categoria, prioridade):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "categoria": categoria,
        "prioridade": prioridade,
        "status": "pendente"
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas.")
    else:
        for t in tarefas:
            print(f"\nNome: {t['nome']}\nDescrição: {t['descricao']}\nCategoria: {t['categoria']}\nPrioridade: {t['prioridade']}\nStatus: {t['status']}\n")

def listar_por_categoria(tarefas, categoria):
    filtradas = [t for t in tarefas if t['categoria'].lower() == categoria.lower()]
    if filtradas:
        for t in filtradas:
            print(f"\nNome: {t['nome']}\nDescrição: {t['descricao']}\nCategoria: {t['categoria']}\nPrioridade: {t['prioridade']}\nStatus: {t['status']}\n")
    else:
        print(f"Nenhuma tarefa na categoria '{categoria}'.")

def listar_por_prioridade(tarefas, prioridade):
    filtradas = [t for t in tarefas if t['prioridade'].lower() == prioridade.lower()]
    if filtradas:
        for t in filtradas:
            print(f"\nNome: {t['nome']}\nDescrição: {t['descricao']}\nCategoria: {t['categoria']}\nPrioridade: {t['prioridade']}\nStatus: {t['status']}\n")
    else:
        print(f"Nenhuma tarefa com prioridade '{prioridade}'.")

def marcar_como_concluida(tarefas, nome):
    for t in tarefas:
        if t['nome'].lower() == nome.lower():
            t['status'] = 'concluída'
            print(f"Tarefa '{nome}' marcada como concluída!")
            return
    print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(tarefas, nome):
    tarefas[:] = [t for t in tarefas if t['nome'].lower() != nome.lower()]
    print(f"Tarefa '{nome}' removida com sucesso.")

def menu(tarefas):
    print("\n- Gerenciador de Tarefas -")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Listar tarefas por categoria")
    print("4. Listar tarefas por prioridade")
    print("5. Marcar tarefa como concluída")
    print("6. Remover tarefa")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome da tarefa: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")
        prioridade = input("Prioridade (baixa, média, alta): ")
        adicionar_tarefa(tarefas, nome, descricao, categoria, prioridade)
    elif opcao == '2':
        listar_tarefas(tarefas)
    elif opcao == '3':
        categoria = input("Categoria para filtrar: ")
        listar_por_categoria(tarefas, categoria)
    elif opcao == '4':
        prioridade = input("Prioridade para filtrar: ")
        listar_por_prioridade(tarefas, prioridade)
    elif opcao == '5':
        nome = input("Nome da tarefa para concluir: ")
        marcar_como_concluida(tarefas, nome)
    elif opcao == '6':
        nome = input("Nome da tarefa para remover: ")
        remover_tarefa(tarefas, nome)
    elif opcao == '7':
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    tarefas = []
    print("Bem-vindo ao Gerenciador de Tarefas")
    while True:
        menu(tarefas)
