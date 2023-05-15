import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry box for displaying the result
        self.result = tk.Entry(master, width=20, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, pady=10)

        #buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        # Loop through the list of buttons and create them
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                button = tk.Button(master, text=buttons[i][j], width=5, height=2, font=('Times New Roman', 20),
                                   command=lambda x=buttons[i][j]: self.button_click(x))
                button.grid(row=i + 1, column=j, padx=2, pady=2)

    def button_click(self, value):
        # Clear the result entry box
        if value == 'C':
            self.result.delete(0, 'end')

        # Evaluate the expression and display the result
        elif value == '=':
            result = eval(self.result.get())
            self.result.delete(0, 'end')
            self.result.insert(0, str(result))

        # Append the button value to the result entry box
        else:
            self.result.insert('end', value)


# Create the main window and start the application
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()


