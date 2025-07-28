from utlities.jsonconverter import *
from utlities.visualization.graphing import *

make_json(budgetbuddy)
plt.ion()
plt.savefig("output/savings_growth.png", dpi=300, bbox_inches='tight')
plt.close()


