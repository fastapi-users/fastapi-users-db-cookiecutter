"""FastAPI Users database adapter for {{ cookiecutter.db_adapter_name }}."""
from typing import Any, Dict, Generic, Optional

from fastapi_users.db.base import BaseUserDatabase
from fastapi_users.models import ID, OAP, UP


__version__ = "0.0.0"


class {{ cookiecutter.db_adapter_class_name }}(Generic[UP, ID], BaseUserDatabase[UP, ID]):
    """
    Database adapter for {{ cookiecutter.db_adapter_name }}.
    """

    async def get(self, id: ID) -> Optional[UP]:
        """Get a single user by id."""
        raise NotImplementedError()

    async def get_by_email(self, email: str) -> Optional[UP]:
        """Get a single user by email."""
        raise NotImplementedError()

    async def get_by_oauth_account(self, oauth: str, account_id: str) -> Optional[UP]:
        """Get a single user by OAuth account id."""
        raise NotImplementedError()

    async def create(self, create_dict: Dict[str, Any]) -> UP:
        """Create a user."""
        raise NotImplementedError()

    async def update(self, user: UP, update_dict: Dict[str, Any]) -> UP:
        """Update a user."""
        raise NotImplementedError()

    async def delete(self, user: UP) -> None:
        """Delete a user."""
        raise NotImplementedError()

    async def add_oauth_account(self, user: UP, create_dict: Dict[str, Any]) -> UP:
        """Create an OAuth account and add it to the user."""
        raise NotImplementedError()

    async def update_oauth_account(
        self, user: UP, oauth_account: OAP, update_dict: Dict[str, Any]
    ) -> UP:
        """Update an OAuth account on a user."""
        raise NotImplementedError()
