import setuptools

setuptools.setup(
    name="doc_manager",
    version="0.0.1",
    author="Assystant Technologies Pvt Ltd",
    description="A simple document manager to store media files in S3 storage bucket.",
    install_requires=[
        "django",
        "djangorestframework",
        "boto3",
        "django-storages",
    ],
    # python_requires = ">=3.10"
)
