import math
import pandas as pd
from graphviz import Source
import csv
import os
import shutil


def process_data(input_path: str, detailed_solution: bool, output_dir: str, svg: bool, graph_preview: bool, dot: bool,
                 sub_folder: bool) -> None:
    """
    This method is called from the GUI. Process the input CSV file.
    :param input_path: The path to the CSV file.
    :param detailed_solution: Flag on whether a detailed solution file is to be created.
    :param output_dir: The directory where the output is to be stored.
    :param svg: Flag on whether an SVG file of the decision tree is to be created.
    :param graph_preview: Flag on whether the graph should be previewed when an SVG is to be created.
    :param dot: Flag on whether a DOT file is to be created.
    :param sub_folder: Flag on whether all output files are to be stored in an output folder in the output directory.
    """

    # invalid file paths
    if input_path == "" or output_dir == "":
        return

    # file names and file paths
    input_file_name = os.path.basename(input_path)
    if detailed_solution:
        solution_type = "extended"
    else:
        solution_type = "compact"
    solution_path = output_dir + "/" + input_file_name[:-4] + "_" + solution_type + "_solution.txt"
    dot_path = output_dir + "/" + input_file_name[:-3] + "dot"

    # corner case (Randfall): data is first created not in a sub folder and then in a sub folder:
    # In order to prevent data to be deleted from the not sub folder when being moved to the sub folder
    # we need to remember that the data already existed before in the not sub folder.
    if os.path.exists(solution_path):
        solution_already_existent = True
    else:
        solution_already_existent = False
    if os.path.exists(dot_path):
        dot_already_existent = True
    else:
        dot_already_existent = False

    # decision tree creation together with log and dot file
    decision_tree_creation(input_path, detailed_solution, output_dir)

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

        # solution file
        new_path_solution_file = sub_folder_dir + "/" + input_file_name[:-4] + "_" + solution_type + "_solution.txt"
        if solution_already_existent:
            shutil.copy2(solution_path, new_path_solution_file)
        else:
            os.replace(solution_path, new_path_solution_file)

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

    # Sometimes on Windows machines a second DOT file without the ".dot" file ending is created.
    # Delete this file if it exists.
    trash_dot_file_path = output_dir + "/" + input_file_name[:-4]
    if os.path.exists(trash_dot_file_path):
        os.remove(trash_dot_file_path)


def decision_tree_creation(input_path: str, detailed_solution_file: bool, output_dir: str) -> None:
    """
    Creates the DOT file of the tree and a solution file.
    :param input_path: The path of the CSV file where the data is stored.
    :param detailed_solution_file: A boolean flag whether a detailed or compact solution file is to be created.
    :param output_dir: The directory where the DOT file and solution file is to be saved.
    """

    # data management
    df: pd.DataFrame = read_csv_file(input_path)
    input_file_name = os.path.basename(input_path)

    # calculation
    output = decision_tree_calculation(df, " ", detailed_solution_file)

    # create the solution file
    if detailed_solution_file:
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


def decision_tree_calculation(subset: pd.DataFrame, root_id_suffix: str,
                              detailed_approach: bool) -> (str, list[str], list[str]):
    """
    Recursively calculates the decision tree. No output files are generated yet.
    :param subset: The data for which the decision tree is to be calculated.
    :param root_id_suffix: Necessary to distinguish between different splitting nodes with the same attribute name.
    :param detailed_approach: Boolean value for whether a detailed approach is to be documented.
            With detailed_approach = False a compact approach is documented.
    :return: A tuple. The first element is the attribute which was used for splitting and the second element
            is the input for the DOT file for the subtree with the splitting node as root. The third element is the
            input for the approach file.
    """
    approach: list[str] = []  # initialization of the approach
    approaches: list[str] = []  # all approaches generated by recursively calculating subtrees appended one by
    # another

    # initialization of variables
    n: int = len(subset.index)  # amount of entries
    igs = []  # the information gains for all attributes
    cols: list[str] = subset.columns.values.tolist()  # get a list of all attribute names
    m = len(cols)  # amount of columns

    approach.append("General information:")
    approach.append("\t|S| = " + str(n))
    approach.append("\tremaining columns: " + str(cols))
    if detailed_approach:
        approach.append("Calculate the entropy of the subset:")

    # retrieve the data to count the rows for the entropy
    target_attr_vals = subset.iloc[:, m - 1]  # get a list of all values of the target attribute including duplicates
    target_attr_vals_unique = target_attr_vals.unique()  # get a list of all values of the target attribute excluding
    # duplicates

    # count how often every target attribute occurs
    target_attr_vals_counts = target_attr_vals.value_counts()

    if detailed_approach:
        approach.append("\tCount the occurrence of each target attribute value:")
        for i in range(len(target_attr_vals_counts)):
            approach.append("\t\t" + str(target_attr_vals_counts.keys()[i]) + ": " + str(target_attr_vals_counts[i]))
        approach.append("\tCalculate the entropy:")
    entropy_calc = ""  # here the calculation steps for the entropy are saved

    # calculate the entropy for all data points
    entropy: float = 0
    for i in range(len(target_attr_vals_unique)):  # For every distinct value of the target attribute ...
        percentage = target_attr_vals_counts[i] / n  # ... calculate the percentage of its occurrence compared to all
        # values ...
        approach_percentage = math.log2(percentage)  # ... and calculate log_2 of the percentage ...
        entropy -= percentage * approach_percentage  # ... to multiply the percentage with log_2(percentage)
        # and subtract the result from the current entropy.
        entropy_calc += "(" + str(target_attr_vals_counts[i]) + "/" + str(n) + ")" + " * log_2(" + \
                        str(target_attr_vals_counts[i]) + "/" + str(n) + ") + "  # extend our current entropy
        # calculation

    entropy_str = "Entropy(S) = " + entropy_calc[:-3] + " = " + str(round(entropy, 3))
    if detailed_approach:
        approach.append("\t\t" + entropy_str)
    else:
        approach.append(entropy_str)
    if detailed_approach:
        approach.append("Calculate the information gain of all attributes:")
    else:
        approach.append("information gain calculation:")

    # Calculate the information gain of all attributes.
    for i in range(m - 1):  # For every attribute ...
        entropies = []  # ... we save the entropies of all values ...
        ns = []  # ... and we save how many rows we have for every value ...
        vals: list[str] = subset.iloc[:, i].unique()  # ... and get all distinct values for the attribute.

        approach.append("\t" + str(cols[i]) + ":")
        if detailed_approach:
            approach.append("\t\tCalculate the entropy of all values of the attribute:")

        # Calculate the entropy of all values of the attribute.
        for val in vals:  # For every value of the attribute ...
            subset_subset = subset[subset[cols[i]] == val]  # ... we retrieve all rows which contain this value ...
            n_subset = len(subset_subset)  # ... and count the amount of rows for the given subset ...
            target_attr_vals_counts_subset = subset_subset.iloc[:, m - 1].value_counts()  # ... and count how often
            # every target attribute value occurs ...
            entropy_for_val = 0  # ... and initialize the entropy.

            if detailed_approach:
                approach.append("\t\t\t" + str(val) + ":")
                approach.append("\t\t\t\tCount the occurrence of each target attribute value:")
                for j in range(len(target_attr_vals_counts_subset)):
                    approach.append("\t\t\t\t\t" + str(target_attr_vals_counts_subset.keys()[j]) + ": " +
                                    str(target_attr_vals_counts_subset[j]))
                approach.append("\t\t\t\tCalculate the entropy:")
            entropy_calc = ""  # here the calculation steps for the entropy are saved

            # Calculate the entropy for the given value of the attribute.
            for j in range(len(target_attr_vals_counts_subset)):  # For every value of the target attribute ...
                percentage = target_attr_vals_counts_subset[j] / n_subset  # ... we calculate the percentage it makes
                # out of all values. ...
                approach_percentage = math.log2(percentage)  # ... and calculate log_2(percentage) ...
                entropy_for_val -= percentage * approach_percentage  # ... and subtract percentage *
                # log_percentage from the current entropy.
                entropy_calc += "(" + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ")" + " * log_2(" \
                                + str(target_attr_vals_counts_subset[j]) + "/" + str(n_subset) + ") + "  # extend our
                # current entropy calculation

            # append our calculated values to our lists
            entropies.append(entropy_for_val)
            ns.append(n_subset)

            entropy_str = "Entropy(S_" + str(val) + ") = " + entropy_calc[:-3] + " = " + str(round(entropy_for_val, 3))
            if detailed_approach:
                approach.append("\t\t\t\t\t" + entropy_str)
            else:
                approach.append("\t\t" + entropy_str)

        # calculate the information gain of this attribute
        entropies_sum = 0  # the right side of the calculation of the information gain
        for j in range(len(vals)):  # For every value of the attribute ...
            entropies_sum += (ns[j] / n) * entropies[j]  # ... add the entropy normalized by n to our sum of entropies.
        ig = entropy - entropies_sum
        igs.append(ig)

        if detailed_approach:
            approach.append("\t\tCalculate the information gain for the attribute:")
        ig_calc = ""  # the right side of the calculation of the information gain
        for j in range(len(vals)):
            ig_calc += "(" + str(ns[j]) + "/" + str(n) + ") * Entropy(S_" + str(vals[j]) + ") + "
        ig_str = "Gain(S," + str(cols[i]) + ") = " + ig_calc[:-3] + " = " + str(round(igs[i], 3))
        if detailed_approach:
            approach.append("\t\t\t" + ig_str)
        else:
            approach.append("\t\t" + ig_str)

    # get the best split attribute
    best_index = -1  # initialization
    best_ig = -math.inf  # initialization
    for i in range(m - 1):
        if igs[i] > best_ig:
            best_index = i
            best_ig = igs[i]
    split_attr_name = cols[best_index]

    if detailed_approach:
        approach.append("Determine the best attribute for splitting: ")
    igs_comma_separated = ""  # all information gains separated by commas
    for col in cols[:-1]:
        igs_comma_separated += "Gain(S," + str(col) + "), "
    max_str = "max{" + igs_comma_separated[:-2] + "} = Gain(S," + str(split_attr_name) + ") --> split at " \
              + str(split_attr_name)
    if detailed_approach:
        approach.append("\t" + max_str)
        approach.append("Create the subtree:")
        approach.append("\tCreate the node " + str(split_attr_name))
        approach.append("\tCreate a child node for every value of " + str(split_attr_name) + ":")
    else:
        approach.append(max_str)

    # Create the graph data.
    dot = []  # the content of the DOT file
    split_attr_id = split_attr_name + root_id_suffix  # the id of the split node
    vals: list[str] = subset.iloc[:, best_index].unique()  # get all values of the split attribute
    id_suffix = 0  # the suffix which is added to the id of newly created nodes

    for val in vals:  # Iterate over all values of the split attribute.

        if detailed_approach:
            approach.append("\t\t" + str(val) + ":")

        val_subset = subset[subset[split_attr_name] == val]  # all rows which have val for the split attribute
        amount_of_different_target_attr_vals = len(val_subset.iloc[:, m - 1].unique())  # How many distinct target
        # attribute values do we have?
        if amount_of_different_target_attr_vals == 1:  # stops the recursion when there is only one target attribute
            # value left (i. e. when we have perfect entropy)
            child_node_name = val_subset.iloc[:, m - 1].unique()[0]  # The remaining target attribute value.
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the
            # target attribute value

            if detailed_approach:
                approach.append("\t\t\tThere is only target attribute value left (i. e. we have perfect entropy). --> "
                                "Create " + str(child_node_name) + " as the child node.")

        elif m == 2:  # stops the recursion if there are no other split attributes left, and we have no perfect entropy
            child_node_name = val_subset.iloc[:, m - 1].value_counts().keys()[0]  # the target attribute value with the
            # most rows
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)  # the id of the node which represents the
            # target attribute value with the most rows

            if detailed_approach:
                approach.append("\t\t\tThere is more than one target attribute values left but we have no more "
                                "attributes for further splits.\n\t\t\tChoose the target attribute value with the most "
                                "occurrences as the child node. --> Create " + str(child_node_name) + " as the child "
                                                                                                      "node.")

        else:  # keep splitting attributes
            val_subset = val_subset.drop(columns=[split_attr_name])  # remove the split attribute column from the subset
            return_val = decision_tree_calculation(val_subset, root_id_suffix + str(id_suffix),
                                                   detailed_approach)  # recursively calculate the decision
            # tree with the split attribute as root node
            child_node_name = return_val[0]  # the split attribute one level deeper in the tree
            child_node_id = child_node_name + root_id_suffix + str(id_suffix)
            dot += return_val[1]  # the dot file entries in the subtree

            if detailed_approach:
                approaches.append("\n\nThis is the approach for the creation of the subtree with " +
                                  str(child_node_name) + " as the root.")  # necessary so that we know where the
                # returning approach belongs to
            else:
                approaches.append("\n\nroot = " + str(child_node_name))  # necessary so that we know where the
                # returning approach belongs to
            approaches += return_val[2]  # append the approach of the subtree to the approach for all subtrees
            if detailed_approach:
                approach.append("\t\t\tThere is more than one target attribute value left (i. e. we have no "
                                "perfect entropy) and we can perform an additional split.\n\t\t\tSplit at the "
                                "attribute which leads to the highest information gain. --> Create " +
                                str(child_node_name) + " as the child node.")
        if detailed_approach:
            approach.append("\t\t\tCreate an edge from " + str(split_attr_name) + " to " + str(child_node_name)
                            + " with the label " + str(val) + ".")

        dot.append("\"" + child_node_id + "\" [label=\"" + child_node_name + "\"]")  # the dot file entry for the child
        # node
        dot.append("\"" + split_attr_id + "\" -> \"" + child_node_id + "\" [label=\"" + val + "\"]")  # the dot file
        # entry for the edge between the split attribute and child node
        id_suffix += 1

    return split_attr_name, dot, (approach + approaches)  # The name of the split attribute, all dot file entries and
    # the approaches of all subtrees so far are returned.


def read_csv_file(path: str) -> pd.DataFrame:
    """
    Read data from a CSV file.
    :param path: The file path of the CSV file.
    :return: The dataframe of the CSV file.
    """
    with open(path, newline='') as f:
        reader = csv.reader(f)
        cols = next(reader)
        if cols[0].__contains__(';'):
            cols = cols[0].split(';')
        elif cols[0].__contains__(','):
            cols = cols[0].split(',')
        elif cols[0].__contains__('\t'):
            cols = cols[0].split('\t')
        rows = []
        for row in reader:
            if row[0].__contains__(';'):
                row = row[0].split(';')
            elif row[0].__contains__(','):
                row = row[0].split(',')
            elif row[0].__contains__('\t'):
                row = row[0].split('\t')
            rows.append(row)
        df = pd.DataFrame(rows, columns=cols)
        return df
