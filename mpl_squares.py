from LeleDrawDesigns.line_chart import LineChart
from LeleDrawDesigns.obtain_all_skin import obtain_all_skin

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

LineChart(squares=squares, input_values=input_values, line_width=3, set_title="Square Numbers",
          set_title_fontsize=34, set_x_label="Value", set_x_label_fontsize=24, set_y_label="Square of Value",
          set_y_label_fontsize=24, label_size=20, skin='Solarize_Light2', line_color='green', figsize=(10, 8))

obtain_all_skin()
