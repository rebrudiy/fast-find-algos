import matplotlib.pyplot as plt
from hash_table_test import hash_table_search_time
from binarytreetest import binary_search_tree_time
from red_black_tree_test import rb_tree_time
lens = [20, 100, 1000, 10000, 57545, 60307, 100000]
hash_table_search_time.reverse()
binary_search_tree_time.reverse()
rb_tree_time.reverse()
plt.plot(lens, hash_table_search_time, color='r', label='hash')
plt.plot(lens, binary_search_tree_time, color='g', label='binary')
plt.plot(lens, rb_tree_time, color='b', label='redblack')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("len")
plt.ylabel("time")
plt.title("find element")
plt.legend()

# To load the display window
plt.show()
