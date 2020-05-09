"""Contains global fixtures for pytest"""
import pytest
import kanboard


@pytest.fixture
def kb(mocker):
    """
    A mock of the kanboard client.

    This mock is used by various tests and can be extended with more methods should they be needed.
    """
    kb = mocker.Mock(kanboard.Client)
    kb.create_comment = mocker.Mock()
    kb.create_user = mocker.Mock()
    kb.get_all_users = mocker.Mock()
    kb.open_task = mocker.Mock()
    kb.update_task = mocker.Mock()
    return kb
