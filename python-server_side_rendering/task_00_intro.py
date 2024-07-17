#!/usr/bin/python3


def generate_invitations(template, attendees):
    """
    Check template - String, attendees - List of dict. terminate if not
    Check if parameters are empty, it one of those are, error message show
    return a file output_x.txt x is the index starting from 1
    """
    if not isinstance(template, str) or not template:
        return "Template is empty or invalid type, no output files generated."
    elif not isinstance(attendees, list) or not attendees:
        return "Attendees is empty or invalid type, no output files generated."
        
    for item in attendees:
        if not isinstance(item, dict):
            return "The list is not a list of dictionaries"

    num = 1    
    for item in attendees:
        new_template = template

        for key, value in item.items():
                replace = "{" + key + "}"
                if value:
                    new_template = new_template.replace(replace, value)
                else:
                    new_template = new_template.replace(replace, key + "N/A")
        with open("output_" + str(num) + ".txt", "w") as file:
            file.write(new_template)
        num+=1