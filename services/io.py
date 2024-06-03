import pickle

# For reading native sources
def read_tsv_to_dict(file_path, num_lines=None):
    doc_dict = {}
    with open(file_path, 'r', encoding="utf-8") as file:
        for i, line in enumerate(file):
            if num_lines is not None and i >= num_lines:
                break
            doc_id, content = line.split('\t', 1)
            if doc_id not in doc_dict:
                doc_dict[doc_id] = []
            doc_dict[doc_id].append(content.strip())
    return doc_dict


def write_object_to_file(file_path, obj):
  with open(file_path, 'wb') as file:
      pickle.dump(obj, file)

def read_object_from_file(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)