#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
import json
import os


def speak():
    """Generates the order."""
    data = load_from_json_rock_n_roll()
    proposition = build_proposition(data)
    menu_item = "{subject} {what} {who} with {where} {how}, {when}."
    return menu_item.format(**proposition)


def build_proposition(data):
    """Build the who, what, when, why, how of the order.

    :param dict data:
        All Guy Fieri's menu propositions.
    """
    return {
        'subject': choice(data['subject_full_name']),
        'what': choice(data['what']),
        'who': choice(data['who']),
        'where': choice(data['where']),
        'how': choice(data['how']),
        "when": choice(data['when'])
    }


def load_from_json_rock_n_roll(path=None, filename='data.json'):
    """Load the config from json (I don't love this, but its better than using
    python's god awful ``ConfigParser``.
    """
    directory = (path if path else os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(directory, filename)
    buf = None
    with open(file_path) as fh:
        buf = json.loads(fh.read())
    return buf
