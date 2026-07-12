import subprocess
from pathlib import Path

from app.core.config import settings


class OneDriveSync:

    def __init__(self):
        self.remote = settings.ONEDRIVE_REMOTE
        self.local_dir = Path(settings.EXCEL_LOCAL_DIR)

        self.local_dir.mkdir(parents=True, exist_ok=True)

    def sync(self):

        subprocess.run(
            [
                "rclone",
                "copy",
                self.remote,
                str(self.local_dir),
                "--update"
            ],
            check=True
        )