import tkinter as tk
from tkinter import messagebox

# Lista para armazenar as tarefas
tasks = []

# Função para adicionar uma nova tarefa
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Por favor, insira uma tarefa.")

# Função para remover uma tarefa selecionada
def remove_task():
    task_index = task_list.curselection()
    if task_index:
        task_list.delete(task_index)
        tasks.pop(task_index[0])
    else:
        messagebox.showwarning("Por favor, selecione uma tarefa.")

# Cria a janela principal
root = tk.Tk()
root.title("Tarefas")

# Cria os widgets
task_label = tk.Label(root, text="Task:")
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
task_list = tk.Listbox(root)

# Coloca os widgets na janela
task_label.grid(row=0, column=0)
task_entry.grid(row=0, column=1)
add_button.grid(row=1, column=0)
remove_button.grid(row=1, column=1)
task_list.grid(row=2, columnspan=2)

# Inicia o loop do tkinter
root.mainloop()
