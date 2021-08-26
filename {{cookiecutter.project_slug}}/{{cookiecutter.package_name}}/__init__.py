"""FastAPI Users database adapter for {{ cookiecutter.db_adapter_name }}."""
from typing import Optional, Type

from pydantic import UUID4

from fastapi_users.db.base import BaseUserDatabase
from fastapi_users.models import UD


__version__ = "0.0.0"


class {{ cookiecutter.db_adapter_class_name }}(BaseUserDatabase[UD]):
    """
    Database adapter for {{ cookiecutter.db_adapter_name }}.

    :param user_db_model: Pydantic model of a DB representation of a user.
    """

    def __init__(
        self,
        user_db_model: Type[UD],
    ):
        super().__init__(user_db_model)

    async def get(self, id: UUID4) -> Optional[UD]:
        """Get a single user by id."""
        raise NotImplementedError()

    async def get_by_email(self, email: str) -> Optional[UD]:
        """Get a single user by email."""
        raise NotImplementedError()

    async def get_by_oauth_account(self, oauth: str, account_id: str) -> Optional[UD]:
        """Get a single user by OAuth account id."""
        raise NotImplementedError()

    async def create(self, user: UD) -> UD:
        """Create a user."""
        raise NotImplementedError()

    async def update(self, user: UD) -> UD:
        """Update a user."""
        raise NotImplementedError()

    async def delete(self, user: UD) -> None:
        """Delete a user."""
        raise NotImplementedError()
