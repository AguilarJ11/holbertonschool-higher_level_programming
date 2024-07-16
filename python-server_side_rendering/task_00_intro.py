#!/usr/bin/python3

from os import abort


def generate_invitations(template, attendees):
    """
    Check template - String, attendees - List of dict. terminate if not
    Check if parameters are empty, it one of those are, error message show
    return a file output_x.txt x is the index starting from 1
    """
    if not isinstance(template, str):
        print(f"Invalid type {template}")
        abort()
    elif not isinstance(attendees, list):
        print(f"Invalid type {attendees}")
        abort()
        
    for item in attendees:
        if not isinstance(item, dict):
            print(f"Invalid type {item}")
            abort()
    num = 1    
    for item in attendees:
        new_template = template

        for key, value in item.items():
                replace = "{" + key + "}"
                if value:
                    new_template = new_template.replace(replace, value)
                else:
                    new_template = new_template.replace(replace, key + ": N/A")
        with open("output_" + str(num) + ".txt", "w") as file:
            file.write(new_template)
        num+=1