import cloudinary.uploader

class Cloud:
    def upload(self,location):
        result = cloudinary.uploader.upload(location)
        url = result.get("url")
        return url