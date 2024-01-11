import os
import shutil
import numpy as np


def split_data(source_folder, output_folder, split_ratio):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get all files in the source folder
    files = [
        f
        for f in os.listdir(source_folder)
        if os.path.isfile(os.path.join(source_folder, f))
    ]
    np.random.shuffle(files)  # Shuffle for random splitting

    # Calculate split indices
    split_point_1 = int(split_ratio[0] * len(files))
    split_point_2 = split_point_1 + int(split_ratio[1] * len(files))

    # Function to copy files
    def copy_files(start_index, end_index, sub_folder):
        os.makedirs(os.path.join(output_folder, sub_folder), exist_ok=True)
        for i in range(start_index, end_index):
            shutil.copy(
                os.path.join(source_folder, files[i]),
                os.path.join(output_folder, sub_folder),
            )

    # Splitting files
    copy_files(0, split_point_1, "train")
    copy_files(split_point_1, split_point_2, "validation")
    copy_files(split_point_2, len(files), "test")


# Example usage
category_folders = [
    "category1",
    "category2",
    "category3",
]  # Replace with your categories
base_folder = "/path/to/images"
split_ratio = (0.7, 0.2, 0.1)  # 70% training, 20% validation, 10% test

for category in category_folders:
    split_data(
        os.path.join(base_folder, category),
        os.path.join(base_folder, category + "_split"),
        split_ratio,
    )


def get_total_count_of_images(file_list) -> int:
    return len(file_list)
