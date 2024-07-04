import re
import  os


def is_verified(file_name):
    # date_pattern = r'\d{4}-\d{2}-\d{2}'
    # return re.search(date_pattern, file_name) is None

    date_pattern = r'\d{4}-\d{2}-\d{2}$'
    return bool(re.search(date_pattern, file_name))



def count_files(directory):

    approved_count = 0
    not_approved_count = 0

    try:
        for file_name in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file_name)):
                if is_verified(file_name):
                    approved_count += 1
                else:
                    not_approved_count += 1
    except FileNotFoundError:
        pass

    return {
        'approved': approved_count,
        'not_approved': not_approved_count
    }

