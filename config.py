import os

def get_paths(timestamp):
    current_run_path = os.path.join('model', str(timestamp))
    os.makedirs(current_run_path, exist_ok=True)
    
    paths = {
        'run_screenshot': os.path.join(current_run_path, "run_screenshot"),
        'place_screenshot': os.path.join(current_run_path, "place_screenshot"),
        'place_screenshot_marker': os.path.join(current_run_path, "place_screenshot_marker"),
        'satellite_images': os.path.join(current_run_path, "satellite_images"),
        'satellite_images_marker': os.path.join(current_run_path, "satellite_images_marker"),
        'train': os.path.join(current_run_path, "train"),
        'val': os.path.join(current_run_path, "val"),
        'test': os.path.join(current_run_path, "test"),
        'test_output': os.path.join(current_run_path, "test_output"),
        'test_output_combined': os.path.join(current_run_path, "test_output_combined"),
        'model': os.path.join(current_run_path, "model"),
    }

    for path in paths.values():
        os.makedirs(path, exist_ok=True)

    return paths
