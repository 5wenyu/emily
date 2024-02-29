# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:56:33 2024

@author: student
"""

import itertools

def generate_truth_table():
    variables = ['P', 'Q']
    results = ['P ∧ Q', 'P ∨ Q', '¬P', 'P → Q', 'P ← Q', 'P ↔ Q']
    header = '\t'.join(variables + results)
    print(header)

    for p, q in itertools.product([True, False], repeat=2):
        p_str = 'T' if p else 'F'
        q_str = 'T' if q else 'F'
        results = [
            p and q,
            p or q,
            not p,
            (not p) or q,
            p or (not q),
            (not p or q) and (p or not q)
        ]
        results = ['T' if result else 'F' for result in results]
        row = '\t'.join([p_str, q_str] + results)
        print(row)

generate_truth_table()
0