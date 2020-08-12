import pandas as pd
data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]}) 

import altair as alt
chart = alt.Chart(data)
alt.Chart(data).mark_point()
chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
chart.save('chart1.html')