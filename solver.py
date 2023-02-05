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


def decision_tree_calculation(subset: pd.DataFrame, root: graphviz.Digraph = None) -> None:
    pass


def log(line: str):
    print(line)
