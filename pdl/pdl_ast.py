from typing import Any, Optional, TypeAlias

from pydantic import BaseModel, RootModel


class ConditionExpr(BaseModel):
    pass


class EndsWithArgs(BaseModel):
    arg0: "PromptType"
    arg1: str


class EndsWithCondition(ConditionExpr):
    ends_with: EndsWithArgs


class ContainsArgs(BaseModel):
    arg0: "PromptType"
    arg1: str


class ContainsCondition(ConditionExpr):
    contains: ContainsArgs


ConditionType: TypeAlias = str | EndsWithCondition | ContainsCondition


class Block(BaseModel):
    """PDL program block"""

    title: Optional[str] = None
    assign: Optional[str] = None
    show_result: bool = True


class ModelBlock(Block):
    model: str
    input: Optional["PromptType"] = None
    decoding: Optional[str] = None
    stop_sequences: Optional[list[str]] = None
    include_stop_sequences: bool = False
    params: Optional[Any] = None


class CodeBlock(Block):
    lan: str
    code: "PromptsType"


class ApiBlock(Block):
    api: str
    url: str
    input: "PromptType"


class VarBlock(Block):
    var: str


class ValueBlock(Block):
    value: Any


class SequenceBlock(Block):
    prompts: list["PromptType"]


class IfBlock(Block):
    prompts: list["PromptType"]
    condition: ConditionType


class RepeatsBlock(Block):
    prompts: list["PromptType"]
    repeats: int


class RepeatsUntilBlock(Block):
    prompts: list["PromptType"]
    repeats_until: ConditionType


BlockType: TypeAlias = (
    ModelBlock
    | CodeBlock
    | ApiBlock
    | VarBlock
    | ValueBlock
    | IfBlock
    | RepeatsBlock
    | RepeatsUntilBlock
    | SequenceBlock
    | Block
)
PromptType: TypeAlias = str | BlockType  # pyright: ignore
PromptsType: TypeAlias = list[PromptType]


class Program(RootModel):
    """
    Prompt Description Program (PDL)
    """

    # root: dict[str, BlockType]
    root: BlockType
