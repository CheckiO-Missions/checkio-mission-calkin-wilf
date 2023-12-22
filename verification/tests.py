"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1],
            "answer": (1, 1),
        },
        {
            "input": [2],
            "answer": (1, 2),
        },
        {
            "input": [3],
            "answer": (2, 1),
        },
        {
            "input": [10],
            "answer": (3, 5),
        },
        {
            "input": [100],
            "answer": (7, 19),
        },
    ],
    "Extra": [
        {
            "input": [1000],
            "answer": (11, 39),
        },
        {
            "input": [10000],
            "answer": (43, 205),
        },
        {
            "input": [100000],
            "answer": (127, 713),
        },
        {
            "input": [11433],
            "answer": (438, 317),
        },
        {
            "input": [117],
            "answer": (18, 11),
        },
        {
            "input": [171],
            "answer": (34, 13),
        },
    ]
}
