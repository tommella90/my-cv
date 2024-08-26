from django.core.exceptions import ValidationError

def validate_file_size(file):
    filesize = file.size
    max_size = 5000000

    if filesize > max_size:
        raise ValidationError(f"File size should not exceed {max_size}")