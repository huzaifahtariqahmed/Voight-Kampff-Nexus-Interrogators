import json

def write_jsonl(filename, data_list):
        with open(filename, 'w', encoding='utf-8') as f:
            for item in data_list:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')

def split_augmentations_by_type(input_files, output_prefix="output"):
    """
    Splits data from jsonl files into four augmentation strategy files: 
    backtranslation, antonym, synonym, and deletion.

    Args:
        input_files (list of str): Paths to the input .jsonl files.
        output_prefix (str): Prefix for the output files (default: "output").

    Output:
        Creates four files:
        - output_backtranslation.jsonl
        - output_antonym.jsonl
        - output_synonym.jsonl
        - output_deletion.jsonl
    """
    backtranslation = []
    antonym = []
    synonym = []
    deletion = []

    for file in input_files:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                data = json.loads(line)
                mod = i % 4
                if mod == 0:
                    backtranslation.append(data)
                elif mod == 1:
                    antonym.append(data)
                elif mod == 2:
                    synonym.append(data)
                elif mod == 3:
                    deletion.append(data)


    write_jsonl(f"augmentation_strategies/{output_prefix}_backtranslation.jsonl", backtranslation)
    write_jsonl(f"augmentation_strategies/{output_prefix}_antonym.jsonl", antonym)
    write_jsonl(f"augmentation_strategies/{output_prefix}_synonym.jsonl", synonym)
    write_jsonl(f"augmentation_strategies/{output_prefix}_deletion.jsonl", deletion)

# Example usage
split_augmentations_by_type(["augmented_data_3.jsonl", "augmented_data_4.jsonl", "augmented_data_5.jsonl"])
