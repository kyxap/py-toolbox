import pytest
from py_toolbox.bitwarden import BitwardenManager, BitwardenError
from unittest.mock import MagicMock


def test_bitwarden_manager_init_no_bw(mocker):
    # Mock shutil.which to simulate 'bw' not installed
    mocker.patch("shutil.which", return_value=None)
    with pytest.raises(BitwardenError, match="Bitwarden CLI"):
        BitwardenManager()


def test_bitwarden_manager_init_with_bw(mocker):
    # Mock shutil.which to simulate 'bw' installed
    mocker.patch("shutil.which", return_value="/usr/local/bin/bw")
    manager = BitwardenManager(session_token="test_session")
    assert manager.session == "test_session"


def test_bitwarden_unlock(mocker):
    mocker.patch("shutil.which", return_value="/usr/local/bin/bw")
    mock_run = mocker.patch("subprocess.run")

    # Mock successful unlock
    mock_run.return_value = MagicMock(
        stdout="new_session_token", stderr="", returncode=0
    )

    manager = BitwardenManager()
    token = manager.unlock("mypassword")

    assert token == "new_session_token"
    assert manager.session == "new_session_token"
    mock_run.assert_called_once()


def test_bitwarden_get_password(mocker):
    mocker.patch("shutil.which", return_value="/usr/local/bin/bw")
    mock_run = mocker.patch("subprocess.run")

    # Mock successful password retrieval
    mock_run.return_value = MagicMock(stdout="secret123", stderr="", returncode=0)

    manager = BitwardenManager(session_token="test_session")
    password = manager.get_password("MySecret")

    assert password == "secret123"
    mock_run.assert_called_with(
        ["bw", "get", "password", "MySecret", "--session", "test_session"],
        capture_output=True,
        text=True,
        check=True,
    )
