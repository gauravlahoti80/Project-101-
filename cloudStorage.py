from os import access
import dropbox

class TransferData:
        def __init__(self , access_token):
            self.access_token = access_token
        
        def upload_files(self,file_from , file_to):
            dbx = dropbox.Dropbox(self.access_token)
            f = open(file_from , 'rb')
            dbx.files_upload(f.read() , file_to)
        
def main():
    access_token = 'sl.Azam6cBNq3-mUe85ST_eD3KsYDqhHgse7EPFRtcCf1LWmkHLKkl5cFINtvLqnzo2jM9tEIkEt6vDuXYonwZMFOdTuS7jjYWSLUp8XJsJo0gBOLBqSKhPgI4Md2w6VuymkfhrbZj7I7M'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload the file ot dropbox: ")
    transferData.upload_files(file_from , file_to)
    print("File has been moved")
main()