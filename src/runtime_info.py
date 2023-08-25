import os
from typing import Final

IS_RUNNING_AS_LAMBDA: Final = bool(os.environ.get("AWS_LAMBDA_FUNCTION_NAME"))
ORIGINS: Final = os.environ.get("ORIGINS", "").split(",")
