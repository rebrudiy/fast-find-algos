import matplotlib.pyplot as plt
from hash_table_test import hash_table_search_time
from binarytreetest import binary_search_tree_time
from red_black_tree_test import rb_tree_time
from hash_table_test import lengths
hash_table_search_time.sort()
binary_search_tree_time.sort()
rb_tree_time.sort()
lengths.sort()
plt.plot(lengths, hash_table_search_time, color='r', label='hash')
plt.plot(lengths, binary_search_tree_time, color='g', label='binary')
plt.plot(lengths, rb_tree_time, color='b', label='redblack')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("len")
plt.ylabel("time")
plt.title("find element")
plt.legend()

# To load the display window
plt.show()
