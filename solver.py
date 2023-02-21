import math

import pandas as pd
import graphviz


# Wurzel = leerer Baum
# Subset = {Dataset}
#
# def decision_tree_calculation(Wurzel, Subset)
#     Erstelle [Alle Spaltennamen]
#
#     Für jede Spalte:
#         Erstelle [Werte]
#         Erstelle S(Spalte) = [9 +, 5 -]
#         Berechne Entropie der gesamten Spalte
#
#         Für jeden Wert:
#             Erstelle S(Wert)
#             Berechne Entropie(Wert)
#
#         Berechne Gain(der gesanten Spalte)
#
#     Vergleiche Gain aller Spalten
#     Wähle Maximum
#     Wähle Spalte des Maximums als Knoten
#
#     Lege für jeden Wert der Spalte eine Kante an
#     Zähle für jede Kante die Menge der Antworten
#         Wenn nur Ja oder nur Nein:
#             Antwort als Kindknoten, Abbruchkriterium
#         Ansonsten:
#             Wurzel = Aktuelle Wurzel
#             Subset = Dataset | Spalte->Wert
#             decision_tree_calculation(Wurzel, Subset)


# Struktur
# GUI
# Load Data
# Calculate Data
# Save Solution
# Save Graph
# Calculate Decision Tree
# Generate Synthetic Data
# Save Synthetic Data


# input for tests
data = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast",
                "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool",
                    "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal",
                 "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong",
             "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"],
    "PlayTennis": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes",
                   "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}
subsetArg: pd.DataFrame = pd.DataFrame(data)
rootArg: graphviz.Digraph = graphviz.Digraph()

##### code for creating and visualizing a graph
# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')
# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', label="Test")
# dot.view()


def decision_tree_calculation(subset: pd.DataFrame, root: graphviz.Digraph):
    # initialization of variables
    n: int = len(subset.index)  # amount of entries
    cols: list[str] = subset.columns.values.tolist()  # get a list of all attributes
    cols_len_index: int = len(cols) - 1  # index of the attribute we want to predict
    igs = []  # the information gains for all attributes

    target_col_vals = subset.iloc[:, cols_len_index]  # get a list of all values of the attribute which we want to predict including duplicates
    target_col_vals_unique = target_col_vals.unique()  # get a list of all values of the attribute which we want to predict excluding duplicates
    target_attr_vals_len = len(target_col_vals_unique)  # amount of different values we have for the target attribute
    target_col_vals_counts: int = target_col_vals.value_counts()  # count how often every target attribute occurs

    # calculate the entropy of all data points
    entropy: float = 0
    for i in range(target_attr_vals_len):
        percentage = target_col_vals_counts[i] / n
        log_val = math.log2(percentage)
        entropy -= percentage * log_val

    # for every attribute ...
    for i in range(cols_len_index):
        vals: list[str] = subset.iloc[:, i].unique()  # get all values of this attribute
        entropies = []  # the entropies for all values
        ns = []  # saves how many entries we have for each value

        for val in vals:  # for every value of the attribute ...
            subset_subset = subset[subset[cols[i]] == val]  # filter to gain all rows which have the current val
            target_col_vals_subset_counts = subset_subset.iloc[:, cols_len_index].value_counts()  # count how often every target attribute occurs
            n_subset = len(subset_subset)  # count how many rows we have for the given subset

            # calculate the entropy
            entropy_for_val = 0
            for j in range(len(target_col_vals_subset_counts)):
                percentage = target_col_vals_subset_counts[j] / n_subset
                log_val = math.log2(percentage)
                entropy_for_val -= percentage * log_val

            entropies.append(entropy_for_val)  # add the entropy to the list of calculated entropies
            ns.append(n_subset)  # add the n for the subset to the list of the ns

        # calculate the information gain of this attribute
        entropies_sum = 0  # the right side of the calculation of the information gain
        for j in range(len(vals)):  # iterate over all entropies for the vals to calc the right side of the calc for ig
            entropies_sum += (ns[j] / n) * entropies[j]  # entropy for each val weighted by amount of rows that have this val
        ig = entropy - entropies_sum
        igs.append(ig)

    # get best split attribute
    best_index = -1
    best_val = -math.inf
    for i in range(cols_len_index):
        if igs[i] > best_val:
            best_index = i
            best_val = igs[i]

    # create nodes and edges
    if root_id == "":
        root.node(cols[best_index])
        root_id = cols[best_index]
    root.node(id=root_id, name="Test")
    root.node(id=root_id, name="Test2")
    vals: list[str] = subset.iloc[:, best_index].unique()  # get all values of this attribute
    for val in vals:
        # create child node
        child_node_id = cols[best_index] + " -> " + val
        root.node(child_node_id)
        root.edge(root_id, child_node_id, label = val)

        # prepare arguments for next decision_tree-call
        val_subset = subset[subset[cols[best_index]] == val]  # subset which has the val
        amount_of_different_target_vals = len(val_subset.iloc[:, cols_len_index].unique())
        if amount_of_different_target_vals == 1:  # stop the recursion when only one target_val remaining
            target_val = val_subset.iloc[:, cols_len_index].unique()[0]
            root.node(child_node_id, label=target_val)
        else:
            decision_tree_calculation(val_subset, root, child_node_id)
    root.view()










# use the method with the sample data set
decision_tree_calculation(subsetArg, rootArg, "")
def log(line: str):
    print(line)
