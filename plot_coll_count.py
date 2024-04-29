import matplotlib.pyplot as plt
from hash_table_test import coll_count, lengths
coll_count.sort()
lengths.sort()
plt.plot(lengths, coll_count, color='r', label='hash')
plt.xlabel("len")
plt.ylabel("count")
plt.title("coll count")
plt.legend()

# To load the display window
plt.show()