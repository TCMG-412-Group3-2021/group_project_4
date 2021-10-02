
from collections import Counter

main_file= open ("http_access_log.txt")
data = main_file.read()

html_count = data.count(".html")
gif_count = data.count(".gif")
xbm_count = data.count(".xbm")
jpg_count = data.count(".jpg")
jpeg_count = data.count(".jpeg")
ps_count = data.count(".ps")

list_count = Counter({'html': html_count, 'gif': gif_count, 'xbm': xbm_count, 'jpg': jpg_count, 'jpeg': jpeg_count, 'ps': ps_count})
max = list_count.most_common(1)[-1]
min = list_count.most_common()[-1]

print(f"The most requested file is {max}")
print(f"The least requested file is {min}")


