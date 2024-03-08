from LeleDrawDesigns.dice_analysis import dice_analysis
from LeleDrawDesigns.histogram import Histogram
from LeleDrawDesigns.line_chart import LineChart
from LeleDrawDesigns.obtain_all_skin import obtain_all_skin

poss_results, frequencies = dice_analysis()

input_values = []
for i in range(len(frequencies)):
    input_values.append(i + 1)

title = 'Results of Rolling One D6 1,000 Times'
xlabel = 'Result'
ylabel = 'Frequency of Result'

Histogram(poss_results, frequencies, skin='Solarize_Light2', title=title, title_fontsize=20,
          x_label=xlabel, x_label_fontsize=20, y_label=ylabel, y_label_fontsize=20, color='green',
          edgecolor='black')

LineChart(input_values=input_values, squares=frequencies, style='straight',
          line_color='green', skin='Solarize_Light2', set_title=title,
          set_title_fontsize=20, set_x_label=xlabel, set_x_label_fontsize=20,
          set_y_label=ylabel, set_y_label_fontsize=20, line_width=3)

LineChart(input_values=input_values, squares=frequencies, style='curved',
          line_color='green', skin='Solarize_Light2', set_title=title,
          set_title_fontsize=20, set_x_label=xlabel, set_x_label_fontsize=20,
          set_y_label=ylabel, set_y_label_fontsize=20, line_width=3)

obtain_all_skin()
