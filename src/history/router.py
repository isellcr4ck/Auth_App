from http.client import responses

from fastapi import APIRouter
from .schemas import MeasureBase, MeasureResponse, UserById
from . import crud
from .models import Measure
from ..auth.models import User
from sqlalchemy import delete, text

SESSION = crud.init_db()

router = APIRouter(prefix="/history", tags=["History"])
@router.get("")
async def read_history():
    request = SESSION.query(Measure).all()
    return request

@router.post("")
async def measure(user_id: int, measure: MeasureBase):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    one_measure = Measure(username=get_user_by_id.username, downloadSpeed=measure.downloadSpeed,
                          uploadSpeed=measure.uploadSpeed, coordinates=measure.coordinates,
                          )
    SESSION.add(one_measure)
    SESSION.commit()
    response_one = MeasureResponse(username=get_user_by_id.username, downloadSpeed=one_measure.downloadSpeed,
                                   uploadSpeed=one_measure.uploadSpeed, coordinates=one_measure.coordinates
                                   )
    response_two = UserById(id=get_user_by_id.id, email=get_user_by_id.email, username=get_user_by_id.username)
    return {"measure": response_one, "user": response_two}


@router.get("/{user_id}")
async def read_measure(user_id: int):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    response = SESSION.query(Measure).filter_by(username=get_user_by_id.username).first()
    return {"measure": response, "user": get_user_by_id}


@router.post("/{user_id}")
async def user(user_id: int):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    return {"id": get_user_by_id.id,
            "email": get_user_by_id.email,
            "username": get_user_by_id.username
            }

@router.get("/user/{user_id}")
async def user(user_id: int):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    request = SESSION.query(Measure).filter_by(username=get_user_by_id.username).all()
    return request

@router.post("/user/{user_id}")
async def history(user_id: int):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    user_query = SESSION.query(Measure).filter_by(username=get_user_by_id.username).all()
    if not user_query:
        return {"message": f"user №{user_id} did not measure the speed"}
    return user_query


@router.delete("/{user_id}")
async def delete(user_id: int):
    get_user_by_id = SESSION.query(User).filter_by(id=user_id).one_or_none()
    if not get_user_by_id:
        return {"message": "User not found"}
    all_measures = SESSION.query(Measure).filter_by(username=get_user_by_id.username).all()
    if all_measures:
        stmt = text("DELETE FROM History WHERE username = :username")
        params = {"username": get_user_by_id.username}
        result = SESSION.execute(stmt, params)
        SESSION.commit()
        return {"message": "Records deleted successfully."}
    else:
        return {"message": "There are no records for this user."}
