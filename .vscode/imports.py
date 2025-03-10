# typical pattern
# from llama_index.core.xxx import ClassABC  # core submodule xxx
# from llama_index.xxx.yyy import (
#     SubclassABC,
# )  # integration yyy for submodule xxx

# concrete example
from llama_index.core.llms import LLM
from llama_index.llms.openai import OpenAI

