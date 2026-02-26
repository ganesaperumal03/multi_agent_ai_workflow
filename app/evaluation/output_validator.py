from pydantic import BaseModel, ValidationError
from typing import Optional


class CodeOutputSchema(BaseModel):
    generated_code: str


class ReviewOutputSchema(BaseModel):
    review_feedback: str


class RefactorOutputSchema(BaseModel):
    refactored_code: str


class DocumentationOutputSchema(BaseModel):
    documentation: str


class OutputValidator:

    @staticmethod
    def validate(schema, data: dict):
        try:
            validated = schema(**data)
            return validated.model_dump()
        except ValidationError as e:
            return {
                "status": "failed",
                "validation_error": e.errors()
            }