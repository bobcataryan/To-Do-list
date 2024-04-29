import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")
        self.tasks = []

        # Create task list
        self.task_list = tk.Listbox(master, width=50)
        self.task_list.pack(pady=10)

        # Entry for new task
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack()

        # Buttons
        self.add_btn = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)
        self.delete_btn = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack()
        self.clear_btn = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_btn.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)
        self.tasks = []

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
