import yaml

from pdl.pdl.pdl_ast import Program  # pyright: ignore
from pdl.pdl.pdl_interpreter import empty_scope  # pyright: ignore
from pdl.pdl.pdl_interpreter import InterpreterState, process_prog  # pyright: ignore


def parse_prog_str(prog_str):
    prog_yaml = yaml.safe_load(prog_str)
    prog = Program.model_validate(prog_yaml)
    return prog


def test_messages1():
    prog_str = """
description: Messages block
array:
  - role: system
    content: You are a helpful software engineer. You write clear, concise, well-commented code.
  - role: user
    content: Write a Python function that implement merge sort.
"""
    prog = parse_prog_str(prog_str)
    state = InterpreterState()
    result, output, _, _ = process_prog(state, empty_scope, prog)
    assert result == [
        {
            "role": "system",
            "content": "You are a helpful software engineer. You write clear, concise, well-commented code.",
        },
        {
            "role": "user",
            "content": "Write a Python function that implement merge sort.",
        },
    ]
    assert output == [
        {
            "role": "system",
            "content": "You are a helpful software engineer. You write clear, concise, well-commented code.",
        },
        {
            "role": "user",
            "content": "Write a Python function that implement merge sort.",
        },
    ]