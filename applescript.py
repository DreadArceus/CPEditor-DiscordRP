import subprocess


def open_app(app: str) -> None:
    try:
        subprocess.check_output(
            ["osascript", "-e", f'tell app "{app}" to open'])
    except subprocess.CalledProcessError:
        pass


def is_runnning(app: str) -> bool:
    count = int(subprocess.check_output(["osascript",
                "-e", "tell application \"System Events\"",
                                         "-e", f'count (every process whose name is "{app}")',
                                         "-e", "end tell"]).strip())
    return count > 0


def get_front_window_name(app: str) -> str:
    return subprocess.check_output(['osascript', "-e",
                                    'tell application "System Events"', "-e",
                                    f'set cpe to first application process whose name is "{app}"', "-e",
                                    'end tell', "-e",
                                    'tell cpe', "-e",
                                    'set window_name to name of front window', "-e",
                                    'end tell']).decode('utf-8')
