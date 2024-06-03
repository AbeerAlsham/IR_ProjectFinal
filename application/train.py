import os
from services import timer
from services import io
from configuration import paths
from engine.offline import document_text_processor, document_representation


def training(path, concat, name):
    timer.start()
    
    print(f"# =-=-=-=-=-= {name} {concat} =-=-=-=-=-= #")
    
    print("# ---------- Parsing Dataset into Dictionary ---------- #")
    dataset = io.read_tsv_to_dict(path)
    
    print("# ---------- Save Parsed Dataset as object ---------- #")
    io.write_object_to_file(os.path.join(path.OUT_FOLDER, f"{name.lower()}_{concat.lower()}.pkl", dataset))
    
    print("# ---------- Start Training ---------- #")
    print("# ---------- Text Processing ---------- #")
    processed_dcouments = document_text_processor.process_document(dataset)
    del dataset # Free up memore
    
    print("# ---------- Saving Parsed Dataset as object ---------- #")
    io.write_object_to_file(os.path.join(path.OUT_FOLDER, f"{name.lower()}_processed_{concat.lower()}.pkl"), processed_dcouments)
    
    print("# ---------- Data Representation ---------- #")
    inverted_index, tfidf, vectorizer = document_representation.document_representation(processed_dcouments)
    del processed_dcouments # Free up memore
    
    print("# ---------- Saving TF-IDF, Inverted Index & Vectorizer ---------- #")
    io.write_object_to_file(os.path.join(path.OUT_FOLDER, f"{name.lower()}_{concat.lower()}_inverted_index.pkl", inverted_index))
    io.write_object_to_file(os.path.join(path.OUT_FOLDER, f"{name.lower()}_{concat.lower()}_tfidf.pkl", tfidf))
    io.write_object_to_file(os.path.join(path.OUT_FOLDER, f"{name.lower()}_{concat.lower()}_vectorizer.pkl", vectorizer))
    del inverted_index, tfidf, vectorizer # Free up memore
    
    print("# --- Finished")
    print("# --- execution time :",  timer.end(), "s")
    
    
# Start Training
training(paths.ANTIQUE_DATASET_NOTPROCESSED_PATH, "Collection" ,"ANTIQUE")
training(paths.ANTIQUE_QUERY_NOTPROCESSED_PATH, "Query" ,"ANTIQUE")

training(paths.LOTTE_DATASET_NOTPROCESSED_PATH, "Collection","LOTTE")
training(paths.LOTTE_QUERY_NOTPROCESSED_PATH, "Query","LOTTE")