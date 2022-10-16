import eel
from back.convert import convert_cur


@eel.expose
def convert_cur_py(value: float, from_cur: str, to_cur: str):
    return convert_cur(value, from_cur, to_cur)







