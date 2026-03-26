import subprocess
import os
import shutil


class BitwardenError(Exception):
    """Base class for library errors"""

    pass


class BitwardenManager:
    def __init__(self, session_token: str = None):
        # Allow passing a token during initialization or take it from environment
        self.session = session_token or os.environ.get("BW_SESSION")
        self._check_bw_installed()

    def _check_bw_installed(self):
        if not shutil.which("bw"):
            raise BitwardenError(
                "Bitwarden CLI (bw) not found in PATH. Install it: https://bitwarden.com/help/cli/"
            )

    def unlock(self, master_password: str) -> str:
        """Unlocks the vault and saves the session"""
        try:
            res = subprocess.run(
                ["bw", "unlock", "--raw"],
                input=master_password,
                capture_output=True,
                text=True,
                check=True,
            )
            self.session = res.stdout.strip()
            # Update environment variable for the current process
            os.environ["BW_SESSION"] = self.session
            return self.session
        except subprocess.CalledProcessError as e:
            raise BitwardenError(f"Failed to unlock: {e.stderr.strip()}")

    def get_password(self, item_name: str) -> str:
        """Gets a password by item name"""
        if not self.session:
            raise BitwardenError("Vault is locked. Call .unlock(password) first")

        try:
            res = subprocess.run(
                ["bw", "get", "password", item_name, "--session", self.session],
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout.strip()
        except subprocess.CalledProcessError:
            raise BitwardenError(f"Password for '{item_name}' not found.")
