import re
import yaml

def parse_sql_statements(sql_content):
    """
    Trả về hai tập hợp (set):
      - outputs: chứa tên bảng (catalog.schema.table) được tạo/drop
      - inputs: chứa tên bảng (catalog.schema.table) được sử dụng (FROM, JOIN)
    """
    # Loại bỏ comment dạng -- ...
    sql_no_comments = re.sub(r'--.*$', '', sql_content, flags=re.MULTILINE)

    # Sử dụng regex để lọc output
    output_pattern = re.compile(
        r'(?i)\b(?:CREATE|DROP|INSERT\s+INTO)\s+(?:TEMP\s+)?TABLE\s+([\w\.]+)'
    )

    # Dùng regex tìm input
    input_pattern = re.compile(
        r'(?i)\b(?:FROM|JOIN)\s+([\w\.]+)'
    )

    outputs_found = re.findall(output_pattern, sql_no_comments)
    inputs_found = re.findall(input_pattern, sql_no_comments)

    # Chuyển về set để loại bỏ trùng lặp
    outputs = set(outputs_found)
    inputs = set(inputs_found)

    return outputs, inputs

def main():
    input_file = 'input.sql'
    output_yaml_file = 'tables.yaml'
  
    with open(input_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()
    outputs, inputs = parse_sql_statements(sql_content)
    data = {
        'inputs': sorted(inputs),
        'outputs': sorted(outputs)
    }
  
    with open(output_yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

    print(f"Ghi kết quả vào: {output_yaml_file}")

if __name__ == "__main__":
    main()
