from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.address_repository import AddressRepository
from schemas.address_schema import AddressInput

class AddressService:
    def __init__(self, session: Session):
        self.repository= session
        self.address_repository = AddressRepository(session)

    def update(self, _id:int, data: AddressInput):
        if not self.address_repository.exists_by_id(_id):
            raise HTTPException(status_code=404, detail='Endereço não encontrado')
        address = self.address_repository.get_by_id(_id)
        return self.address_repository.update(data, address)

    def delete(self, _id: int):
        if not self.address_repository.exists_by_id(_id):
            raise HTTPException(status_code=404, detail='Endereço não encontrado')
        address = self.address_repository.get_by_id(_id)
        return self.address_repository.delete(address)