from pypresence import Presence
import time
import os
from applescript import *
from dotenv import load_dotenv
load_dotenv()


def get_active_file(title: str) -> str:
    return (title[:-13]).split('/')[-1]


RPC = Presence(os.getenv('client_id'))

open_app("cpeditor")
RPC.connect()
st = time.time()
RPC.update(start=st, large_image="cpeditor", state="Just Launched")

current_file = None
while True:
    if not is_runnning("cpeditor"):
        print("cp-editor has been closed")
        RPC.close()
        break
    window_name = get_front_window_name("cpeditor")
    if window_name.strip() != 'New update available':
        f = get_active_file(window_name)
        if f != current_file:
            current_file = f
            RPC.update(start=st, large_image="cpeditor", details=f"Editing {f}", state="HACKERMANS")
    time.sleep(1.5)
