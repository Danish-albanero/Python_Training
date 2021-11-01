from . import s3_analyzer
from . import pg_analyzer
from . import oracle_analyzer

analyzers = {
    "s3": s3_analyzer,
    "postgresql": pg_analyzer,
    "oracle": oracle_analyzer,
}
