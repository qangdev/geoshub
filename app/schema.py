from pydantic import BaseModel


class ServiceBase(BaseModel):
    name: str = None
    price: float = None
    os_platform: str = None


class NewService(ServiceBase):
    pass


class EditSerive(ServiceBase):
    id: int = None


class Activity(BaseModel):
    request: str = None
