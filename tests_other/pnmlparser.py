import main_program.workflow_engine as we
import xml.etree.ElementTree as eT


def parse_file(filename):
    # Parse filename
    tree = eT.parse(filename)
    root = tree.getroot()

    # Storing object references to places and transitions until we get to parse the arcs
    current_wf = ""  # Storing the reference to the workflow as it is being populated
    dict_places = {}  # Arcs need to retrieve object references from node label strings
    dict_transitions = {}  # Arcs need to retrieve object references from node label strings

    # Parse the Petri-Net itself
    for n in root.iter('net'):
        i = n.get('id')
        current_wf = we.Workflow(i)

    # Parse all places
    for p in root.iter('place'):
        i = p.get('id')
        j = we.Place(i)
        dict_places[i] = j  # 'ID'-string i is key, object reference j is value
        current_wf.add_place(j)

    # Parse all transitions
    for t in root.iter('transition'):
        i = t.get('id')
        s = t.find('name/text').text
        # j = workflow_engine.Transition(s)
        j = we.Transition(s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        dict_transitions[i] = j  # 'ID'-string i is key, object reference j is value
        current_wf.add_transition(j)

    # Parse all arcs
    for a in root.iter('arc'):
        i = a.get('id')
        s = a.get('source')
        t = a.get('target')

        if s in dict_places:  # This is an arc leading from a place to a transition
            # Find the place object reference according to string s
            x = dict_places.get(s)

            # Find the transition object reference according to string t
            y = dict_transitions.get(t)

            # Create the arc
            we.Arc(i, x, y, 0)

        else:  # This is an arc leading from a transition to a place
            # Find the place object reference according to string s
            x = dict_transitions.get(s)

            # Find the transition object reference according to string t
            y = dict_places.get(t)

            # Create the arc
            we.Arc(i, x, y, 0)

    # The workflow now needs to identify those of its places that are a source or a sink
    current_wf.search_sources_sinks()

    return current_wf
