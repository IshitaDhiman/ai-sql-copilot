from fastapi import APIRouter, HTTPException, Request

from services.sql_service import ask_database
from services.sql_generation_service import generate_sql_from_question

router = APIRouter(
    prefix="/sql",
    tags=["AI SQL"]
)


async def _extract_question(request: Request, question: str | None = None) -> str:
    if question and question.strip():
        return question.strip()

    query_param = request.query_params.get("question") or request.query_params.get("query")
    if query_param and query_param.strip():
        return query_param.strip()

    try:
        payload = await request.json()
        if isinstance(payload, dict):
            for key in ("question", "query"):
                payload_value = payload.get(key)
                if isinstance(payload_value, str) and payload_value.strip():
                    return payload_value.strip()
    except Exception:
        pass

    raise HTTPException(
        status_code=422,
        detail="Question is required"
    )


@router.api_route("/generate", methods=["GET", "POST"])
async def generate_sql(request: Request, question: str | None = None):
    """
    Generate SQL only.
    """

    try:
        question_text = await _extract_question(request, question)
        sql = generate_sql_from_question(question_text)

        return {
            "question": question_text,
            "generated_sql": sql
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.api_route("/execute", methods=["GET", "POST"])
async def execute_sql(request: Request, question: str | None = None):
    """
    Generate SQL and execute it.
    """

    try:
        question_text = await _extract_question(request, question)
        return ask_database(question_text)

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )