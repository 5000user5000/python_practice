# 將大量檔案改名稱
import os

# Replace the directory path with the folder containing JPEG images to be converted
directory_path = "D:/img"

# Function to rename multiple files
def main():
	i = 0
	for filename in os.listdir(directory_path):
		my_dest = filename.replace("something-wanna-del","").replace("del~t","") # 修改檔名，這裡是把一些字串給刪除
		my_source =directory_path + "/" + filename
		my_dest =directory_path + "/"  + my_dest
		# rename() function will rename all the files
		os.rename(my_source, my_dest)
		i += 1
	print(i) # 確認數量
	print("Done!")

if __name__ == '__main__':
	main()
