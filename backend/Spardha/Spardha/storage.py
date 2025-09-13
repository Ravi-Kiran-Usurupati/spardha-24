from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

class IgnoreMissingFilesStorage(ManifestStaticFilesStorage):
    """
    Custom storage to ignore missing source map files.
    """
    def post_process(self, *args, **kwargs):
        try:
            return super().post_process(*args, **kwargs)
        except ValueError:
            # ignore missing files
            return [], True
