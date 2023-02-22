import math
import pandas as pd
from graphviz import Source


# Creates the decision tree. The argument root_id_suffix is necessary to distinguish different nodes
# with the same name by adding the root_id_suffix to the name of the node to create a unique id
# for the node.
# Returns a tuple. The first element is the attribute which was used for splitting and the second element
# is the input for the dot file for the subtree with the splitting node as root.
def decision_tree_calculation(subset: pd.DataFrame, root_id_suffix: str) -> (str, list[str]):
    # initialization of variables
    n: int = len(subset.index)  # amount of entries
    igs = []  # the information gains for all attributes
    cols: list[str] = subset.columns.values.tolist()  # get a list of all attribute names
    m = len(cols)  # amount of columns

    # retrieve the data to count the rows for the entropy
    target_attr_vals = subset.iloc[:, m-1]  # get a list of all values of the target attribute including duplicates
    target_attr_vals_unique = target_attr_vals.unique()  # get a list of all values of the target attribute excluding duplicates

    # count how often every target attribute occurs
    target_attr_vals_counts = target_attr_vals.value_counts()

    # calculate the entropy for all data points
    entropy: float = 0
    for i in range(len(target_attr_vals_unique)):  # For every distinct value of the target attribute ...
        percentage = target_attr_vals_counts[i] / n  # ... calculate the percentage of its occurence compared to all values ...
        log_percentage = math.log2(percentage)  # ... and calculate the log_2 of the percentage ...
        entropy -= percentage * log_percentage  # ... to multiply the percentage with log_2(percentage) and subtract the result from the current entropy.

    # Calculate the information gain of all attributes.
    for i in range(m-1):  # For every attribute ...
        entropies = []  # ... we save the entropies of all values ...
        ns = []  # ... and we save how many rows we have for every value ...
        vals: list[str] = subset.iloc[:, i].unique()  # ... and get all distinct values for the attribute.

        # Calculate the entropy of all values of the attribute.
        for val in vals:  # For every value of the attribute ...
            subset_subset = subset[subset[cols[i]] == val]  # ... we retrieve all rows which contain this value ...
            n_subset = len(subset_subset)  # ... and count the amount of rows for the given subset ...
            target_attr_vals_counts_subset = subset_subset.iloc[:, m-1].value_counts()  # ... and count how often every target attribute value occurs ...
            entropy_for_val = 0 # ... and initialize the entropy.

            # Calculate the entropy for the given value of the attribute.
            for j in range(len(target_attr_vals_counts_subset)):  # For every value of the target attribute ...
                percentage = target_attr_vals_counts_subset[j] / n_subset  # ... we calculate the percentage it makes out of all values. ...
                log_percentage = math.log2(percentage)  # ... and calculate log_2(percentage) ...
                entropy_for_val -= percentage * log_percentage  # ... and subtract percentage * log_percentage from the current entropy.

            # append our calculated values to our lists
            entropies.append(entropy_for_val)
            ns.append(n_subset)

        # calculate the information gain of this attribute
        entropies_sum = 0  # the right side of the calculation of the information gain
        for j in range(len(vals)):  # For every value of the attribute ...
            entropies_sum += (ns[j] / n) * entropies[j]  # ... add the entropy normalized by n to our sum of entropies.
        ig = entropy - entropies_sum
        igs.append(ig)

    # get the best split attribute
    best_index = -1  # initialization
    best_ig = -math.inf  # initialization
    for i in range(m-1):
        if igs[i] > best_ig:
            best_index = i
            best_ig = igs[i]
    split_attr_name = cols[best_index]

    # Create the graph data.
    dot = []  # the content of the dot file
    split_attr_id = split_attr_name + root_id_suffix  # the id of the split node
    vals: list[str] = subset.iloc[:, best_index].unique()  # get all values of the split attribute
    id_suffix = 0  # the suffix which is added to the id of newly created nodes

    for val in vals:  # Iterate over all values of the split attribute.
        val_subset = subset[subset[split_attr_name] == val]  # all rows which have val for the split attribute
        amount_of_different_target_attr_vals = len(val_subset.iloc[:, m-1].unique())  # How many different target attribute values do we have?
        if amount_of_different_target_attr_vals == 1:  # stops the recursion when there is only one target attribute value left (i. e. when we have perfect entropy)
            child_node_name = val_subset.iloc[:, m-1].unique()[0]  # The remaining target attribute value.
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the target attribute value
        elif m == 2:  # stops the recursion if there are no other split attributes left and we have no perfect entropy
            child_node_name = val_subset.iloc[:, m-1].value_counts().keys()[0]  # the target attribute value with the most rows
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the target attribute value with the most rows
        else:  # keep splitting attributes
            val_subset = val_subset.drop(columns=[split_attr_name])  # remove the split attribute column from the data set
            return_val = decision_tree_calculation(val_subset, root_id_suffix + str(id_suffix))  # recursively calculate the decision tree with the split attribute as root node
            child_node_name = return_val[0]  # the split attribute on level deeper in the tree
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)
            dot += return_val[1]  # the dot file entries in the subtree
        dot.append("\"" + child_node_id + "\" [label=\"" + child_node_name + "\"]")  # the dot file entry for the child node
        dot.append("\"" + split_attr_id + "\" -> \"" + child_node_id + "\" [label=\"" + val + "\"]")  # the dot file entry for the edge between the split attribute and child node
        id_suffix += 1

    return split_attr_name, dot  # The name of the split attribute and all dot file entries are returned.


# Creates the dot file and shows the graph.
def show_tree(dot: list[str]):
    # Create the dot file.
    f = open("tree.dot", "w")
    f.write("digraph G {\n")
    for line in dot:
        f.write("\t" + line + "\n")
    f.write("}")
    f.close()

    # Render the graph from the dot file.
    path = 'tree.dot'
    s = Source.from_file(path)
    s.view()


# input for tests

# classical play tennis data set
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

# second data set (notes for Dennis: der gleiche Datensatz, wie aus der 5. KDDM-
# Übung mit einem weiteren Datum am Ende, um den Fall len(cols) == 2 abzudecken
data2 = {
    "Experience": ["1-2", "2-7", ">7", "1-2", ">7", "1-2", "2-7", "2-7", ">7"],
    "Gender": ["m", "m", "f", "f", "m", "m", "f", "m", "f"],
    "Area": ["u", "r", "r", "r", "r", "r", "u", "u", "r"],  # u=urban, r=rural
    "Risk class": ["l", "h", "l", "h", "h", "h", "l", "l", "h"]  # h=high, l=low
}
data_arg: pd.DataFrame = pd.DataFrame(data)  # the dataframe for data
data_arg2: pd.DataFrame = pd.DataFrame(data2)  # the dataframe for data2
root_id_suffix_arg = ""  # second argument of the function


# creates and visualizes the decision tree based on the given data set
tree_arg = decision_tree_calculation(data_arg2, "")
show_tree(tree_arg[1])


def log(line: str):
    print(line)
