import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '23JSWty8GlAAAAAAAAAAAXShlOUegtYxm4WLd9k1nfFnugQOM1JvsDXDDGk-Wm1t'
    transferData = TransferData(access_token)

    file_from = 'blank.txt'
    file_to = '/Ma_app/blank.txt' 

    transferData.uploadFile(file_from, file_to)
    print("file has been uploaded")

main()
