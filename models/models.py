from pydantic import BaseModel

class Model_Cost(BaseModel):
    input_tokens: float
    output_tokens: float

class Model_Definition(BaseModel):
    model: ChatOpenAI,
    cost_per_mm: Model_Cost

MODELS = {
    'gpt-5.4-mini': Model_Definition(
        model=ChatOpenAI(model="gpt-5.4-mini", temperature=0),
        cost_per_mm=Model_Cost(
            input=.75,
            output=4.50
        )
    )
}