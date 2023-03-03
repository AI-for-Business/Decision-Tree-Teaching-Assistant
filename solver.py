import math
import pandas as pd
from graphviz import Source
import csv
import os
import shutil

# Creates the decision tree. The argument root_id_suffix is necessary to distinguish different nodes
# with the same name by adding the root_id_suffix to the name of the node to create a unique id
# for the node.
# Returns a tuple. The first element is the attribute which was used for splitting and the second element
# is the input for the dot file for the subtree with the splitting node as root. The third element is the
# input for the detailed log file.
def decision_tree_calculation_detailed_log(subset: pd.DataFrame, root_id_suffix: str) -> (str, list[str], list[str]):
    log: list[str] = []  # initialization of the log file
    logs: list[str] = []  # all log files generated by recursively calculating subtrees appended one by another

    # initialization of variables
    n: int = len(subset.index)  # amount of entries
    igs = []  # the information gains for all attributes
    cols: list[str] = subset.columns.values.tolist()  # get a list of all attribute names
    m = len(cols)  # amount of columns

    log.append("General information:")
    log.append("\t|S| = " + str(n))
    log.append("\tremaining columns: " + str(cols))
    log.append("Calculate the entropy of the subset:")

    # retrieve the data to count the rows for the entropy
    target_attr_vals = subset.iloc[:, m-1]  # get a list of all values of the target attribute including duplicates
    target_attr_vals_unique = target_attr_vals.unique()  # get a list of all values of the target attribute excluding duplicates

    # count how often every target attribute occurs
    target_attr_vals_counts = target_attr_vals.value_counts()

    log.append("\tCount the occurrence of each target attribute value:")
    for i in range(len(target_attr_vals_counts)):
        log.append("\t\t" + str(target_attr_vals_counts.keys()[i]) + ": " + str(target_attr_vals_counts[i]))
    log.append("\tCalculate the entropy:")
    entropy_calc = ""  # here the calculation steps for the entropy are saved

    # calculate the entropy for all data points
    entropy: float = 0
    for i in range(len(target_attr_vals_unique)):  # For every distinct value of the target attribute ...
        percentage = target_attr_vals_counts[i] / n  # ... calculate the percentage of its occurence compared to all values ...
        log_percentage = math.log2(percentage)  # ... and calculate the log_2 of the percentage ...
        entropy -= percentage * log_percentage  # ... to multiply the percentage with log_2(percentage) and subtract the result from the current entropy.
        entropy_calc += "(" + str(target_attr_vals_counts[i]) + "/" + str(n) + ")" + " * log_2(" + str(target_attr_vals_counts[i]) + "/" + str(n) + ") + "  # extend our current entropy calculation

    log.append("\t\tEntropy(S) = " + entropy_calc[:-3] + " = " + str(round(entropy, 3)))
    log.append("Calculate the information gain of all attributes:")

    # Calculate the information gain of all attributes.
    for i in range(m-1):  # For every attribute ...
        entropies = []  # ... we save the entropies of all values ...
        ns = []  # ... and we save how many rows we have for every value ...
        vals: list[str] = subset.iloc[:, i].unique()  # ... and get all distinct values for the attribute.

        log.append("\t" + str(cols[i]) + ":")
        log.append("\t\tCalculate the entropy of all values of the attribute:")

        # Calculate the entropy of all values of the attribute.
        for val in vals:  # For every value of the attribute ...
            subset_subset = subset[subset[cols[i]] == val]  # ... we retrieve all rows which contain this value ...
            n_subset = len(subset_subset)  # ... and count the amount of rows for the given subset ...
            target_attr_vals_counts_subset = subset_subset.iloc[:, m-1].value_counts()  # ... and count how often every target attribute value occurs ...
            entropy_for_val = 0 # ... and initialize the entropy.

            log.append("\t\t\t" + str(val) + ":")
            log.append("\t\t\t\tCount the occurrence of each target attribute value:")
            for j in range(len(target_attr_vals_counts_subset)):
                log.append("\t\t\t\t\t" + str(target_attr_vals_counts_subset.keys()[j]) + ": " + str(target_attr_vals_counts_subset[j]))
            log.append("\t\t\t\tCalculate the entropy:")
            entropy_calc = ""  # here the calculation steps for the entropy are saved

            # Calculate the entropy for the given value of the attribute.
            for j in range(len(target_attr_vals_counts_subset)):  # For every value of the target attribute ...
                percentage = target_attr_vals_counts_subset[j] / n_subset  # ... we calculate the percentage it makes out of all values. ...
                log_percentage = math.log2(percentage)  # ... and calculate log_2(percentage) ...
                entropy_for_val -= percentage * log_percentage  # ... and subtract percentage * log_percentage from the current entropy.
                entropy_calc += "(" + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ")" + " * log_2(" + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ") + "  # extend our current entropy calculation

            # append our calculated values to our lists
            entropies.append(entropy_for_val)
            ns.append(n_subset)

            log.append("\t\t\t\t\tEntropy(S_" + str(val) + ") = " + entropy_calc[:-3] + " = " + str(round(entropy_for_val, 3)))

        # calculate the information gain of this attribute
        entropies_sum = 0  # the right side of the calculation of the information gain
        for j in range(len(vals)):  # For every value of the attribute ...
            entropies_sum += (ns[j] / n) * entropies[j]  # ... add the entropy normalized by n to our sum of entropies.
        ig = entropy - entropies_sum
        igs.append(ig)

        log.append("\t\tCalculate the information gain for the attribute:")
        ig_calc = ""  # the right side of the calculation of the information gain
        for j in range(len(vals)):
            ig_calc += "(" + str(ns[j]) + "/" + str(n) + ") * Entropy(S_" + str(vals[j]) + ") + "
        log.append("\t\t\tGain(S," + str(cols[i]) + ") = " + ig_calc[:-3] + " = " + str(round(igs[i], 3)))

    # get the best split attribute
    best_index = -1  # initialization
    best_ig = -math.inf  # initialization
    for i in range(m-1):
        if igs[i] > best_ig:
            best_index = i
            best_ig = igs[i]
    split_attr_name = cols[best_index]

    log.append("Determine the best attribute for splitting: ")
    igs_comma_separated = ""  # all information gains separated by commas
    for col in cols[:-1]:
        igs_comma_separated += "Gain(S," + str(col) + "), "
    log.append("\tmax{" + igs_comma_separated[:-2] + "} = Gain(S," + str(split_attr_name) + ") --> split at " + str(split_attr_name))
    log.append("Create the subtree:")
    log.append("\tCreate the node " + str(split_attr_name))
    log.append("\tCreate a child node for every value of " + str(split_attr_name) + ":")

    # Create the graph data.
    dot = []  # the content of the dot file
    split_attr_id = split_attr_name + root_id_suffix  # the id of the split node
    vals: list[str] = subset.iloc[:, best_index].unique()  # get all values of the split attribute
    id_suffix = 0  # the suffix which is added to the id of newly created nodes

    for val in vals:  # Iterate over all values of the split attribute.

        log.append("\t\t" + str(val) + ":")

        val_subset = subset[subset[split_attr_name] == val]  # all rows which have val for the split attribute
        amount_of_different_target_attr_vals = len(val_subset.iloc[:, m-1].unique())  # How many different target attribute values do we have?
        if amount_of_different_target_attr_vals == 1:  # stops the recursion when there is only one target attribute value left (i. e. when we have perfect entropy)
            child_node_name = val_subset.iloc[:, m-1].unique()[0]  # The remaining target attribute value.
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the target attribute value

            log.append("\t\t\tThere is only target attribute value left (i. e. we have perfect entropy). --> Create " + str(child_node_name) + " as the child node.")

        elif m == 2:  # stops the recursion if there are no other split attributes left and we have no perfect entropy
            child_node_name = val_subset.iloc[:, m-1].value_counts().keys()[0]  # the target attribute value with the most rows
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the target attribute value with the most rows

            log.append("\t\t\tThere is more than one target attribute values left but we have no more attributes for further splits.\n"
                       "\t\t\tChoose the target attribute value with the most occurrences as the child node. --> Create " + str(child_node_name) + " as the child node.")

        else:  # keep splitting attributes
            val_subset = val_subset.drop(columns=[split_attr_name])  # remove the split attribute column from the data set
            return_val = decision_tree_calculation_detailed_log(val_subset, root_id_suffix + str(id_suffix))  # recursively calculate the decision tree with the split attribute as root node
            child_node_name = return_val[0]  # the split attribute one level deeper in the tree
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)
            dot += return_val[1]  # the dot file entries in the subtree

            logs.append("\n\nThis is the log for the creation of the subtree with " + str(child_node_name) + " as the root.")  # necessary so that we know where the returning log belongs to
            logs += return_val[2]  # append the log file of the subtree to the log file for all subtrees
            log.append("\t\t\tThere is more than one target attribute value left (i. e. we have no perfect entropy) and we can perform an additional split.\n"
                       "\t\t\tSplit at the attribute which leads to the highest information gain. --> Create " + str(child_node_name) + " as the child node.")
        log.append("\t\t\tCreate an edge from " + str(split_attr_name) + " to " + str(child_node_name) + " with the label " + str(val) + ".")

        dot.append("\"" + child_node_id + "\" [label=\"" + child_node_name + "\"]")  # the dot file entry for the child node
        dot.append("\"" + split_attr_id + "\" -> \"" + child_node_id + "\" [label=\"" + val + "\"]")  # the dot file entry for the edge between the split attribute and child node
        id_suffix += 1

    return split_attr_name, dot, (log + logs)  # The name of the split attribute and all dot file entries are returned.


# Creates the decision tree. The argument root_id_suffix is necessary to distinguish different nodes
# with the same name by adding the root_id_suffix to the name of the node to create a unique id
# for the node.
# Returns a tuple. The first element is the attribute which was used for splitting and the second element
# is the input for the dot file for the subtree with the splitting node as root. The third element is the
# input for the compact log file.
def decision_tree_calculation_compact_log(subset: pd.DataFrame, root_id_suffix: str) -> (str, list[str], list[str]):
    log: list[str] = []  # initialization of the log file
    logs: list[str] = []  # all log files generated by recursively calculating subtrees appended one by another

    # initialization of variables
    n: int = len(subset.index)  # amount of entries
    igs = []  # the information gains for all attributes
    cols: list[str] = subset.columns.values.tolist()  # get a list of all attribute names
    m = len(cols)  # amount of columns

    log.append("General information:")
    log.append("\t|S| = " + str(n))
    log.append("\tremaining columns: " + str(cols))

    # retrieve the data to count the rows for the entropy
    target_attr_vals = subset.iloc[:, m-1]  # get a list of all values of the target attribute including duplicates
    target_attr_vals_unique = target_attr_vals.unique()  # get a list of all values of the target attribute excluding duplicates

    # count how often every target attribute occurs
    target_attr_vals_counts = target_attr_vals.value_counts()

    entropy_calc = ""  # here the calculation steps for the entropy for the log file are saved

    # calculate the entropy for all data points
    entropy: float = 0
    for i in range(len(target_attr_vals_unique)):  # For every distinct value of the target attribute ...
        percentage = target_attr_vals_counts[i] / n  # ... calculate the percentage of its occurence compared to all values ...
        log_percentage = math.log2(percentage)  # ... and calculate the log_2 of the percentage ...
        entropy -= percentage * log_percentage  # ... to multiply the percentage with log_2(percentage) and subtract the result from the current entropy.
        entropy_calc += "(" + str(target_attr_vals_counts[i]) + "/" + str(n) + ")" + " * log_2(" + str(target_attr_vals_counts[i]) + "/" + str(n) + ") + "  # extend our current entropy calculation

    log.append("Entropy(S) = " + entropy_calc[:-3] + " = " + str(round(entropy, 3)))
    log.append("information gain calculation:")

    # Calculate the information gain of all attributes.
    for i in range(m-1):  # For every attribute ...
        entropies = []  # ... we save the entropies of all values ...
        ns = []  # ... and we save how many rows we have for every value ...
        vals: list[str] = subset.iloc[:, i].unique()  # ... and get all distinct values for the attribute.

        log.append("\t" + str(cols[i]) + ":")

        # Calculate the entropy of all values of the attribute.
        for val in vals:  # For every value of the attribute ...
            subset_subset = subset[subset[cols[i]] == val]  # ... we retrieve all rows which contain this value ...
            n_subset = len(subset_subset)  # ... and count the amount of rows for the given subset ...
            target_attr_vals_counts_subset = subset_subset.iloc[:, m-1].value_counts()  # ... and count how often every target attribute value occurs ...
            entropy_for_val = 0 # ... and initialize the entropy.

            entropy_calc = ""  # here the calculation steps for the entropy for the log file are saved

            # Calculate the entropy for the given value of the attribute.
            for j in range(len(target_attr_vals_counts_subset)):  # For every value of the target attribute ...
                percentage = target_attr_vals_counts_subset[j] / n_subset  # ... we calculate the percentage it makes out of all values. ...
                log_percentage = math.log2(percentage)  # ... and calculate log_2(percentage) ...
                entropy_for_val -= percentage * log_percentage  # ... and subtract percentage * log_percentage from the current entropy.
                entropy_calc += "(" + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ")" + " * log_2(" + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ") + "  # extend our current entropy calculation

            # append our calculated values to our lists
            entropies.append(entropy_for_val)
            ns.append(n_subset)

            log.append("\t\tEntropy(S_" + str(val) + ") = " + entropy_calc[:-3] + " = " + str(round(entropy_for_val, 3)))

        # calculate the information gain of this attribute
        entropies_sum = 0  # the right side of the calculation of the information gain
        for j in range(len(vals)):  # For every value of the attribute ...
            entropies_sum += (ns[j] / n) * entropies[j]  # ... add the entropy normalized by n to our sum of entropies.
        ig = entropy - entropies_sum
        igs.append(ig)

        ig_calc = ""  # the right side of the calculation of the information gain
        for j in range(len(vals)):
            ig_calc += "(" + str(ns[j]) + "/" + str(n) + ") * Entropy(S_" + str(vals[j]) + ") + "
        log.append("\t\tGain(S," + str(cols[i]) + ") = " + ig_calc[:-3] + " = " + str(round(igs[i], 3)))

    # get the best split attribute
    best_index = -1  # initialization
    best_ig = -math.inf  # initialization
    for i in range(m-1):
        if igs[i] > best_ig:
            best_index = i
            best_ig = igs[i]
    split_attr_name = cols[best_index]

    igs_comma_separated = ""  # all information gains separated by commas
    for col in cols[:-1]:
        igs_comma_separated += "Gain(S," + str(col) + "), "
    log.append("max{" + igs_comma_separated[:-2] + "} = Gain(S," + str(split_attr_name) + ")")

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
            return_val = decision_tree_calculation_compact_log(val_subset, root_id_suffix + str(id_suffix))  # recursively calculate the decision tree with the split attribute as root node
            child_node_name = return_val[0]  # the split attribute one level deeper in the tree
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)
            dot += return_val[1]  # the dot file entries in the subtree

            logs.append("\n\nroot = " + str(child_node_name))  # necessary so that we know where the returning log belongs to
            logs += return_val[2]  # append the log file of the subtree to the log file for all subtrees

        dot.append("\"" + child_node_id + "\" [label=\"" + child_node_name + "\"]")  # the dot file entry for the child node
        dot.append("\"" + split_attr_id + "\" -> \"" + child_node_id + "\" [label=\"" + val + "\"]")  # the dot file entry for the edge between the split attribute and child node
        id_suffix += 1

    return split_attr_name, dot, (log + logs)  # The name of the split attribute and all dot file entries are returned.


# Calculates the decision tree returning the dot file and creates depending on the input argument
# either a compact or a detailed log file.
def decision_tree_calculation(input_path: str, detailed_log: bool, output_dir: str):
    # data management
    df: pd.DataFrame = read_csv_file(input_path)
    input_file_name = os.path.basename(input_path)

    # calculation
    if detailed_log:
        output = decision_tree_calculation_detailed_log(df, "")
    else:
        output = decision_tree_calculation_compact_log(df, "")

    # create the log file
    if detailed_log:
        log_type = "extended"
    else:
        log_type = "compact"
    log = output[2]
    log_path = output_dir + "/" + input_file_name[:-4] + "_" + log_type + "_solution.txt"
    f = open(log_path, "w")
    for line in log:
        f.write(line + "\n")
    f.close()

    # create the dot file for the tree
    dot_text = output[1]
    dot_path = output_dir + "/" + input_file_name[:-3] + "dot"
    f = open(dot_path, "w")
    f.write("digraph G {\n")
    for line in dot_text:
        f.write("\t" + line + "\n")
    f.write("}")
    f.close()


# Read data from a CSV file
def read_csv_file(path: str) -> pd.DataFrame:
    with open(path, newline='') as f:
        reader = csv.reader(f)
        cols = next(reader)
        cols = cols[0].split(";")
        rows = []
        for row in reader:
            row = row[0].split(";")
            rows.append(row)
        df = pd.DataFrame(rows, columns=cols)
        return df


# This method is called from the GUI.
def process_data(input_path: str, detailed_log: bool, output_dir: str, svg: bool, graph_preview: bool, dot: bool, sub_folder: bool) -> None:
    # invalid file paths
    if input_path == "" or output_dir == "":
        return

    # file names and file paths
    input_file_name = os.path.basename(input_path)
    if detailed_log:
        log_type = "extended"
    else:
        log_type = "compact"
    log_path = output_dir + "/" + input_file_name[:-4] + "_" + log_type + "_solution.txt"
    dot_path = output_dir + "/" + input_file_name[:-3] + "dot"

    # corner case (Randfall): data is first created not in a sub folder and then in a sub folder:
    # In order to prevent data to be deleted from the not sub folder when being moved to the sub folder
    # we need to remember that the data already existed before in the not sub folder.
    if os.path.exists(log_path):
        log_already_existent = True
    else:
        log_already_existent = False
    if os.path.exists(dot_path):
        dot_already_existent = True
    else:
        dot_already_existent = False

    # decision tree creation together with log and dot file
    decision_tree_calculation(input_path, detailed_log, output_dir)

    # svg file creation
    if svg and not sub_folder:
        dot_source = Source.from_file(dot_path, format='svg')
        if graph_preview:
            dot_source.view(dot_path[:-4], cleanup=True)
        else:
            dot_source.render(dot_path[:-4], cleanup=True)

    # move all files to a sub folder when flag is true
    if sub_folder:

        # create directory
        sub_folder_dir = input_path[:-4] + "_processed"
        if not os.path.exists(sub_folder_dir):
            os.mkdir(sub_folder_dir)

        # log file
        new_path_log_file = sub_folder_dir + "/" + input_file_name[:-4] + "_" + log_type + "_solution.txt"
        if log_already_existent:
            shutil.copy2(log_path, new_path_log_file)
        else:
            os.replace(log_path, new_path_log_file)

        # svg file
        if svg:
            dot_source = Source.from_file(dot_path, format='svg')
            svg_path = sub_folder_dir + "/" + input_file_name[:-4]
            if graph_preview:
                dot_source.view(svg_path, cleanup=True)
            else:
                dot_source.render(svg_path)

        # dot file
        if dot:
            new_dot_path = sub_folder_dir + "/" + input_file_name[:-3] + "dot"
            if dot_already_existent:
                shutil.copy2(dot_path, new_dot_path)
            else:
                os.replace(dot_path, new_dot_path)

    # delete dot file when boolean flag is true
    if not dot:
        os.remove(dot_path)
