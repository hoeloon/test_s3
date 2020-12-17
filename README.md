# Dependency
```
pip install boto3==1.0.0
```

# View s3 buket using cli
```
pip install awscli
touch ~/.aws/credentials
```
## View item
```
aws s3 ls s3://duluxpreviewservice-com/project/gallery/
```
## Delete item
```
aws s3 rm s3://duluxpreviewservice-com/project/gallery/image.jpg
```

# Issue
unable to generate link without expiry time. 

https://stackoverflow.com/questions/55608012/how-to-generate-permanent-s3-object-file-url-without-expiration
