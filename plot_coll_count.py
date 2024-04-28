import matplotlib.pyplot as plt
from hash_table_test import coll_count
coll_count.reverse()

lens = [20, 100, 1000, 10000, 57545, 60307, 100000]

plt.plot(lens, coll_count, color='r', label='hash')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("len")
plt.ylabel("count")
plt.title("coll count")
plt.legend()

# To load the display window
plt.show()