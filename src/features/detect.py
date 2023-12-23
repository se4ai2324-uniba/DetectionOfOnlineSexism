import os
import cv2
import numpy as np
from alibi_detect.cd import KSDrift
from datetime import datetime
import os 

def compute_features(data_path):
    images = [cv2.imread(os.path.join(data_path, file), cv2.IMREAD_GRAYSCALE) for file in os.listdir(data_path)]
    histograms = [np.histogram(image.flatten(), 256, [0, 256])[0] for image in images]
    return np.mean(histograms, axis=0)

def detect_drift(train_data_path, test_data_path, threshold=0.01):
    train_features = compute_features(train_data_path)
    test_features = compute_features(test_data_path)

    drift_detector = KSDrift(train_features, p_val=threshold)
    drift_results = drift_detector.predict(test_features, drift_type='batch', return_p_val=True, return_distance=True)

    return drift_results

def log_drift_results(log_file, model_name, dataset_name, drift_results):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as log:
        log.write(f"[{current_time}] Model: {model_name}, Dataset: {dataset_name}\n")
        log.write(f"  Drift Detected: {drift_results['data']['is_drift']}\n")
        log.write(f"  p-value: {drift_results['data']['p_val']}\n")
        log.write(f"  distance: {drift_results['data']['distance']}\n")

if __name__ == "__main__":
    print(os.getcwd())
    model1_train_data_path = "/ProjectAI/data/Raw/train_sexist.csv"
    model1_test_data_path = "\ProjectAI\data\Raw\test_sexist.csv"
    model1_validation_data_path = "\ProjectAI\data\Raw\dev_sexist.csv"
    model1_log_file = "\ProjectAI\src\features\Log\model_sexism.txt"

    model2_train_data_path = "\ProjectAI\data\Raw\train_category.csv"
    model2_test_data_path = "\ProjectAI\data\Raw\test_category.csv"
    model2_validation_data_path = "\ProjectAI\data\Raw\dev_category.csv"
    model2_log_file =  "\ProjectAI\src\features\Log\model_category.txt"

    model1_drift_results = detect_drift(model1_train_data_path, model1_test_data_path)
    model2_drift_results = detect_drift(model2_train_data_path, model2_test_data_path)

    # Logga i risultati per il Modello 1 (test set)
    log_drift_results(model1_log_file, "Modello 1", "Test Set", model1_drift_results)

    # Esegui la rilevazione del drift per il Modello 1 (validation set)
    model1_validation_drift_results = detect_drift(model1_train_data_path, model1_validation_data_path)

    # Logga i risultati per il Modello 2 (test set)
    log_drift_results(model1_log_file, "Modello 2", "Test Set", model2_drift_results)

    # Esegui la rilevazione del drift per il Modello 2 (validation set)
    model2_validation_drift_results = detect_drift(model2_train_data_path, model2_validation_data_path)

    # Visualizza i risultati
    print("Modello 1 - Drift Detected (Test Set):", model1_drift_results['data']['is_drift'])
    print("Modello 1 - Drift Detected (Validation Set):", model1_validation_drift_results['data']['is_drift'])
    # Ripeti il processo per il Modello 2
    print("Modello 2 - Drift Detected (Test Set):", model2_drift_results['data']['is_drift'])
    print("Modello 2 - Drift Detected (Validation Set):", model2_validation_drift_results['data']['is_drift'])