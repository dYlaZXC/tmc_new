import xlwt

YELLOW_CELL = xlwt.easyxf(
    "pattern: fore_colour yellow, pattern solid; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; ")
YELLOW_CELL_CENTER = xlwt.easyxf(
    "pattern: fore_colour yellow, pattern solid; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; align: vert center, horiz center;")
DEFAULT_CELL = xlwt.easyxf(
    "borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; ")
DEFAULT_CELL_CENTER = xlwt.easyxf(
    "borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; align: vert center, horiz center;")
DEFAULT_CELL_VERTICAL_CENTER = xlwt.easyxf(
    "borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; align: vert center;")
BOLD_CELL_CENTER = xlwt.easyxf(
    "font: bold on; borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin; align: vert center, horiz center;")
