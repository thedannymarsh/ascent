#!/usr/bin/env python3.7

"""
The copyrights of this software are owned by Duke University.
Please refer to the LICENSE and README.md files for licensing instructions.
The source code can be found on the following GitHub repository: https://github.com/wmglab-duke/ascent

Compare thresholds across models using a barchart.

For more controls over how the plotting occurs, see the seaborn documentation on barplot:
https://seaborn.pydata.org/generated/seaborn.barplot.html
"""

# RUN THIS FROM REPOSITORY ROOT
import matplotlib.pyplot as plt
import seaborn as sb

from src.core.query import Query

sb.set_theme()

q = Query(
    {
        'partial_matches': False,
        'include_downstream': True,
        'indices': {'sample': [0], 'model': [0, 1], 'sim': [0]},
    }
).run()

data = q.threshold_data()
g = sb.barplot(data=data, x='model', y='threshold')
plt.title('Threshold barchart comparison')
plt.savefig('threshold_comparison_barchart.png', dpi=400, bbox_inches='tight')