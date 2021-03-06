from typing import Optional

from pydantic import BaseModel, Field


class AddFaceResponse(BaseModel):
    uuid: Optional[str] = Field(None, description='Уникальный идентификатор для добавленного лица')
    message: str = Field(..., description='Сообщение от сервера')


class DeleteFaceResponse(BaseModel):
    message: str = Field(..., description='Сообщение от сервера')


class DetectFaceResponse(BaseModel):
    uuid: Optional[str] = Field(None, description='Уникальный идентификатор для найденного лица')
    message: str = Field(..., description='Сообщение от сервера')
