import altair as alt
from vega_datasets import data

source = data.barley()
 
chart=alt.Chart(source).mark_bar().encode(
    x='sum(yield)',
    y='variety',
    color='year'
)  

print(data.airports()) 
print(data._datasets.items()) 
chart.save('chart12.html', None,True)