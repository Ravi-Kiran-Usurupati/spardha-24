from whitenoise.storage import CompressedManifestStaticFilesStorage

class IgnoreMissingFilesStorage(CompressedManifestStaticFilesStorage):
    def post_process(self, *args, **kwargs):
        try:
            return super().post_process(*args, **kwargs)
        except Exception as e:
            if "MissingFileError" in str(e) and ".map" in str(e):
                return []
            raise e
