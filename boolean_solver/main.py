import tkinter as tk
import program1 as p1 
from tkinter import scrolledtext
from quine_mccluskey.qm import QuineMcCluskey


# Helper function to append results
def append_result(text):
    result.insert(tk.END, text + "\n")

# Function to process the boolean expression based on selected operation
def process_operation(operation):
    expression = input_field.get()
    symbols_str, variable_names = p1.extract_symbols(expression)
    #append_result(f"{len(variable_names)}")
    if (len(variable_names) > 4):
        #append_result(symbols_str)
        append_result(f"Symbols count greater than 4 not currently supported")
        return -1
    # functions necessary for basic functions
    minterms = p1.boolean_expression_to_minterms(expression, symbols_str)
    maxterms = p1.boolean_expression_to_maxterms(expression, symbols_str)
    binary_minterms = p1.convert_minterms_to_binary(minterms)
    minterm_indices = p1.minterms_to_indices(binary_minterms)
    binary_maxterms = p1.convert_minterms_to_binary(maxterms)
    maxterm_indices = p1.minterms_to_indices(binary_maxterms)
    sop_expression = p1.minterms_to_canonical_sop(minterms)
    pos_expression = p1.minterms_to_canonical_sop(maxterms)
    minimized_sop = p1.simplify(sop_expression, symbols_str)
    minimized_pos = p1.simplify(pos_expression,symbols_str)
    # rquired for implicant calculations
    qm = QuineMcCluskey()
    prime_implicants = p1.generate_minterm_table(binary_minterms)
    qm_EPIs = qm.simplify(minterm_indices)
    pi_string = (str(prime_implicants) + ', ' + str(qm_EPIs))
    pi_string_edit = pi_string.replace("[", '').replace("]", '')
    pi_string_final = pi_string_edit.replace("{", '').replace("}", '')

    #result.delete('1.0', tk.END)  # Clear previous results

    try:
        #expr = parse_expr(expression, evaluate=False)  # Parse the input expression
        #simplified_expr = simplify(expr)  # Simplify the expression

        # Placeholder switch-case for different operations
        if operation == "minterms":
            #answer = p1.boolean_expression_to_minterms(expression, symbols_str)
            append_result(f"Minterms: {minterms}")
        elif operation == "maxterms":
            #answer = p1.boolean_expression_to_maxterms(expression, symbols_str)
            append_result(f"Maxterms: {maxterms}")
        elif operation == "can_sop":
            #binary_minterms = p1.convert_minterms_to_binary(minterms)
            #answer = p1.minterms_to_indices(binary_minterms)
            append_result(f"Canonical SOP: {minterm_indices}")
        elif operation == "can_pos":
            append_result(f"Canonical POS: {maxterm_indices}")
        elif operation == "inv_sop":
            append_result(f"Inverse SOP: {maxterm_indices}")
        elif operation == "inv_pos":
            append_result(f"Inverse POS: {minterm_indices}")
        elif operation == "min_sop":
            append_result(f"Minimized SOP: {minimized_sop}")
        elif operation == "num_lit_sop":
            saved_sop_literals, sop_literals = p1.calculate_saved_literals(sop_expression, minimized_sop, symbols_str)
            append_result(f"Number of Saved Literals in SOP: {saved_sop_literals}")
        elif operation == "min_pos":
            append_result(f"Minimized POS: {minimized_pos}")
        elif operation == "num_lit_pos":
            saved_pos_literals, pos_literals = p1.calculate_saved_literals(pos_expression, minimized_pos, symbols_str)
            append_result(f"Number of Saved Literals in POS: {saved_pos_literals}")
        elif operation == "prime_implicants":
            append_result(f"Prime Implicants: {pi_string_final}")
        elif operation == "num_prime_implicants":
            append_result(f"Number of Prime Implicants: {len(prime_implicants) + len(qm_EPIs)}")
        elif operation == "ess_prime_implicants":
            append_result(f"Essential Prime Implicants: {qm_EPIs}")
        elif operation == "num_ess_prime_implicants":
            append_result(f"Number of EPIs: {len(qm_EPIs)}")
        elif operation == "onset_minterms":
            append_result(f"Number of ON-set minterms: {len(minterms)}")
        elif operation == "onset_maxterms":
            append_result(f"Number of ON-set maxterms: {len(maxterms)}")
        elif operation == "transistors_sop":
            inverter_count, and_gate_count, or_gate_count, total_transistors_sop = p1.estimate_transistors(str(minimized_sop))
            append_result(f"Assumptions:\nInverter = 2 transitors\nAND and OR gates = 2N transistors where N is # inputs\nTotal Transistors in SOP Design: {total_transistors_sop}")
        elif operation == "transistors_pos":
            inverter_count_pos, and_gate_count_pos, or_gate_count_pos, total_transistors_pos = p1.estimate_transistors_pos(str(minimized_pos))
            append_result(f"Assumptions:\nInverter = 2 transitors\nAND and OR gates = 2N transistors where N is # inputs\nTotal Transistors in SOP Design: {total_transistors_pos}")

    except Exception as e:
        result.insert(tk.END, f"Error: {str(e)}")

def clear_results():
    result.delete('1.0', tk.END)
    

# Setting up the GUI
root = tk.Tk()
root.title("Boolean Expression Analyzer")

# Input field setup
input_label = tk.Label(root, text="Enter Boolean Expression:")
input_label.grid(row=0, column=0, columnspan=6)
input_field = tk.Entry(root, width=50)
input_field.grid(row=1, column=0, columnspan=6)

# Buttons for each functionality
operations = [
    "minterms", "maxterms", "can_sop", "can_pos", "inv_sop", "inv_pos",
    "min_sop", "num_lit_sop", "min_pos", "num_lit_pos", "prime_implicants",
    "num_prime_implicants", "ess_prime_implicants", "num_ess_prime_implicants",
    "onset_minterms", "onset_maxterms", "transistors_sop", "transistors_pos"
]
row = 2
col = 0
for i, op in enumerate(operations):
    button = tk.Button(root, text=op.replace('_', ' ').title(), command=lambda op=op: process_operation(op))
    button.grid(row=row, column=col, sticky='ew')
    col += 1
    if col > 5:
        col = 0
        row += 1

# Result display area
result = scrolledtext.ScrolledText(root, width=80, height=20)
result.grid(row=row+1, column=0, columnspan=6)

# Clear button in the top right
clear_button = tk.Button(root, text="Clear", command=clear_results)
clear_button.grid(row=0, column = 4, sticky = 'ne')

# Run the application
root.mainloop()
