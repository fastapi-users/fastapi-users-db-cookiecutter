from typing import AsyncGenerator

import pytest

from {{ cookiecutter.package_name}} import {{ cookiecutter.db_adapter_class_name }}
from tests.conftest import UserDB, UserDBOAuth

@pytest.fixture
async def {{ cookiecutter.db_adapter_slug }}_user_db() -> AsyncGenerator[{{ cookiecutter.db_adapter_class_name }}, None]:
    raise NotImplementedError()


@pytest.fixture
async def {{ cookiecutter.db_adapter_slug }}_user_db_oauth() -> AsyncGenerator[{{ cookiecutter.db_adapter_class_name }}, None]:
    raise NotImplementedError()


@pytest.mark.asyncio
@pytest.mark.db
async def test_queries({{ cookiecutter.db_adapter_slug }}_user_db: {{ cookiecutter.db_adapter_class_name }}[UserDB]):
    user = UserDB(
        email="lancelot@camelot.bt",
        hashed_password="guinevere",
    )

    # Create
    user_db = await {{ cookiecutter.db_adapter_slug }}_user_db.create(user)
    assert user_db.id is not None
    assert user_db.is_active is True
    assert user_db.is_superuser is False
    assert user_db.email == user.email

    # Update
    user_db.is_superuser = True
    await {{ cookiecutter.db_adapter_slug }}_user_db.update(user_db)

    # Get by id
    id_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get(user.id)
    assert id_user is not None
    assert id_user.id == user_db.id
    assert id_user.is_superuser is True

    # Get by email
    email_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get_by_email(str(user.email))
    assert email_user is not None
    assert email_user.id == user_db.id

    # Get by uppercased email
    email_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get_by_email("Lancelot@camelot.bt")
    assert email_user is not None
    assert email_user.id == user_db.id

    # Exception when inserting existing email
    with pytest.raises():
        await {{ cookiecutter.db_adapter_slug }}_user_db.create(user)

    # Exception when inserting non-nullable fields
    with pytest.raises():
        wrong_user = UserDB(hashed_password="aaa")
        await {{ cookiecutter.db_adapter_slug }}_user_db.create(wrong_user)

    # Unknown user
    unknown_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get_by_email("galahad@camelot.bt")
    assert unknown_user is None

    # Delete user
    await {{ cookiecutter.db_adapter_slug }}_user_db.delete(user)
    deleted_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get(user.id)
    assert deleted_user is None


@pytest.mark.asyncio
@pytest.mark.db
async def test_queries_custom_fields({{ cookiecutter.db_adapter_slug }}_user_db: {{ cookiecutter.db_adapter_class_name }}[UserDB]):
    """It should output custom fields in query result."""
    user = UserDB(
        email="lancelot@camelot.bt",
        hashed_password="guinevere",
        first_name="Lancelot",
    )
    await {{ cookiecutter.db_adapter_slug }}_user_db.create(user)

    id_user = await {{ cookiecutter.db_adapter_slug }}_user_db.get(user.id)
    assert id_user is not None
    assert id_user.id == user.id
    assert id_user.first_name == user.first_name


@pytest.mark.asyncio
@pytest.mark.db
async def test_queries_oauth(
    {{ cookiecutter.db_adapter_slug }}_user_db_oauth: {{ cookiecutter.db_adapter_class_name }}[UserDBOAuth],
    oauth_account1,
    oauth_account2,
):
    user = UserDBOAuth(
        email="lancelot@camelot.bt",
        hashed_password="guinevere",
        oauth_accounts=[oauth_account1, oauth_account2],
    )

    # Create
    user_db = await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.create(user)
    assert user_db.id is not None
    assert hasattr(user_db, "oauth_accounts")
    assert len(user_db.oauth_accounts) == 2

    # Update
    user_db.oauth_accounts[0].access_token = "NEW_TOKEN"
    await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.update(user_db)

    # Get by id
    id_user = await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.get(user.id)
    assert id_user is not None
    assert id_user.id == user_db.id
    assert id_user.oauth_accounts[0].access_token == "NEW_TOKEN"

    # Get by email
    email_user = await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.get_by_email(str(user.email))
    assert email_user is not None
    assert email_user.id == user_db.id
    assert len(email_user.oauth_accounts) == 2

    # Get by OAuth account
    oauth_user = await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.get_by_oauth_account(
        oauth_account1.oauth_name, oauth_account1.account_id
    )
    assert oauth_user is not None
    assert oauth_user.id == user.id

    # Unknown OAuth account
    unknown_oauth_user = await {{ cookiecutter.db_adapter_slug }}_user_db_oauth.get_by_oauth_account("foo", "bar")
    assert unknown_oauth_user is None
