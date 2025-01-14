from typing import Generic, TypeVar, Type, Any, Tuple

from pydantic import BaseModel

DataT = TypeVar('DataT')


class Response(BaseModel, Generic[DataT]):
    data: DataT

    @classmethod
    def __concrete_name__(cls: Type[Any], params: Tuple[Type[Any], ...]) -> str:
        return f'{params[0].__name__.title()}Response'


print(repr(Response[int](data=1)))
print(repr(Response[str](data='a')))
