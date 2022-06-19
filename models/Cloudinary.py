import cloudinary
import cloudinary.uploader

class Cloud:
    def upload(location):
        result = cloudinary.uploader.upload(location)
        url = result.get("ur")
        return url