import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Ali"]
usernamer = ["Ali1"]
passwords = ["123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "Hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)