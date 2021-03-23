from google_drive_downloader import GoogleDriveDownloader as gdd

fname = "cocci.txt" # filename with links  later change to healthy.txt
save_dir = "rawImg/cocci/" # Specify directory to save to, later change to rawImg/healthy/


def download_image(id, save_to):
	gdd.download_file_from_google_drive(file_id=id, dest_path=save_to)

with open(fname) as text_file:
	for link in text_file.read().splitlines():
		file_id = link.split("=")[1]
		try:
			download_image(file_id, save_dir+file_id+".jpg")
		except Exception as e:
			print(e)

