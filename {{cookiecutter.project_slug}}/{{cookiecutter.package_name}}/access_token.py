"""FastAPI Users access token database adapter for {{ cookiecutter.db_adapter_name }}."""
from datetime import datetime
from typing import Any, Dict, Generic, Optional

from fastapi_users.authentication.strategy.db import AccessTokenDatabase, AP


class {{ cookiecutter.access_token_adapter_class_name }}(Generic[AP], AccessTokenDatabase[AP]):
    """
    Access token database adapter for {{ cookiecutter.db_adapter_name }}.
    """

    async def get_by_token(
        self, token: str, max_age: Optional[datetime] = None
    ) -> Optional[AP]:
        """Get a single access token by token."""
        raise NotImplementedError()

    async def create(self, create_dict: Dict[str, Any]) -> AP:
        """Create an access token."""
        raise NotImplementedError()

    async def update(self, access_token: AP, update_dict: Dict[str, Any]) -> AP:
        """Update an access token."""
        raise NotImplementedError()

    async def delete(self, access_token: AP) -> None:
        """Delete an access token."""
        raise NotImplementedError()
