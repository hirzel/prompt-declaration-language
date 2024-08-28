from pdl.pdl.pdl_ast import Program  # pyright: ignore
from pdl.pdl.pdl_interpreter import empty_scope  # pyright: ignore
from pdl.pdl.pdl_interpreter import InterpreterState, process_prog  # pyright: ignore

array_data = {"description": "Array", "array": ["1", "2", "3", "4"]}


def test_array_data():
    state = InterpreterState()
    data = Program.model_validate(array_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == ["1", "2", "3", "4"]


for_data = {
    "description": "For block example",
    "for": {
        "i": [1, 2, 3, 4],
    },
    "repeat": "{{ i }}",
}


def test_for_data():
    state = InterpreterState()
    data = Program.model_validate(for_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == [1, 2, 3, 4]


repeat_until_data = {
    "description": "Repeat until",
    "sequence": [
        {
            "def": "I",
            "document": [{"lan": "python", "code": "result = 0"}],
            "show_result": False,
        },
        {
            "repeat": [
                {
                    "def": "I",
                    "lan": "python",
                    "code": ["result = {{ I }} + 1"],
                }
            ],
            "until": "{{ I == 5 }}",
            "as": "array",
        },
    ],
}


def test_repeat_until():
    state = InterpreterState()
    data = Program.model_validate(repeat_until_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == [1, 2, 3, 4, 5]