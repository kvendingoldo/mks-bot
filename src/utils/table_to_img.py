import dataframe_image as dfi
from io import BytesIO


def convert(table):
    buf = BytesIO()
    dfi.export(table, buf)
    return buf