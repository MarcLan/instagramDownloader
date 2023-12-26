from obs import ObsClient
from obs import PutObjectHeader
import os

obsClient = ObsClient(
    access_key_id = 'HDANZNU1ZCJUPSDPY1AU',
    secret_access_key = 'rlRGxa7gXJpnpOCXtCo17TxcaVIProDHc0gONKqI',
    server = 'https://obs.ap-southeast-3.myhuaweicloud.com'
)

# Create OBS bucket
resp = obsClient.createBucket(bucketName='ly-clips', location='ap-southeast-3')
if resp.status < 300:
    print('requestID: ', resp.requestID)
else:
    print('errorCode: ', resp.errorCode)
    print('errorMessage: ', resp.errorMessage)

# Determine whether the bucket exists
bucket = obsClient.headBucket('ly-clips') 
    
if bucket.status < 300: 
    print('Bucket exists') 
elif bucket.status == 404: 
    print('Bucket does not exist')

# Upload object
bucketName = 'ly-clips'
folderName = "clips/"

L = []
for root, dirs, files in os.walk(r"D:/08 Code/insToBili/：saved"):
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            fileName = os.path.basename(file)
            print(fileName)
            uploader = obsClient.putFile(bucketName, folderName+fileName, filePath)
            L.append(uploader)

#file_path = 'D:/08 Code\insToBili/：saved/*.mp4'


if resp.status < 300: 
    print('requestId:', uploader.requestId) 
    print('etag:', uploader.body.etag) 
    print('versionId:', uploader.body.versionId) 
    print('storageClass:', uploader.body.storageClass) 
else: 
    print('errorCode:', uploader.errorCode) 
    print('errorMessage:', uploader.errorMessage)
