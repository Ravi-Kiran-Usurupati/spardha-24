from whitenoise.storage import CompressedManifestStaticFilesStorage
from django.contrib.staticfiles.storage import ManifestFilesMixin

class IgnoreMissingFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Extends CompressedManifestStaticFilesStorage but ignores missing .map files
    to prevent collectstatic from failing.
    """
    def post_process(self, *args, **kwargs):
        try:
            return super().post_process(*args, **kwargs)
        except Exception as e:
            if "MissingFileError" in str(e) and ".map" in str(e):
                # silently ignore missing .map files
                return []
            raise e
