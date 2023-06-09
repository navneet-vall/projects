import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        #input_box
        self.result = tk.Entry(master, width=20, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, pady=10)

        #buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        #buttons_loop_values
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                button = tk.Button(master, text=buttons[i][j], width=5, height=2, font=('Times New Roman', 20),
                                   command=lambda x=buttons[i][j]: self.button_click(x))
                button.grid(row=i + 1, column=j, padx=2, pady=2)

    def button_click(self, value):
        #clr_results_C_button
        if value == 'C':
            self.result.delete(0, 'end')

        #eval_values
        elif value == '=':
            result = eval(self.result.get())
            self.result.delete(0, 'end')
            self.result.insert(0, str(result))

        #output_result
        else:
            self.result.insert('end', value)


#app_main_window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()


