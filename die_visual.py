from LeleDrawDesigns.dice_analysis import dice_analysis
from LeleDrawDesigns.histogram import Histogram

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
