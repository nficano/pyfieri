#!/usr/bin/env python

from random import choice
import json
import os


def generate():
    data = load_from_json()
    proposition = build_proposition(data)
    order_structure = "{subject} {what} {who} with {where} {how}, {when}."
    return order_structure.format(**proposition)


def build_proposition(data):
    return {
        'subject': choice(data['subject_full_name']),
        'what': choice(data['what']),
        'who': choice(data['who']),
        'where': choice(data['where']),
        'how': choice(data['how']),
        "when": choice(data['when'])
    }


def load_from_json():
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = "data.json"
    path = os.path.join(directory, filename)
    with open(path) as fh:
        return json.loads(fh.read())


if __name__ == "__main__":
    print generate()
