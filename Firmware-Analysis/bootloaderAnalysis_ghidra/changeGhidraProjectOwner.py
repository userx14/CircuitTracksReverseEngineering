import os
import getpass
import xml.etree.ElementTree as ET

def update_state_value_in_xml(file_path, new_value):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for state in root.iter('STATE'):
            if 'VALUE' in state.attrib:
                old_value = state.attrib['VALUE']
                state.attrib['VALUE'] = new_value
                print(f"Updated VALUE from '{old_value}' to '{new_value}' in: {file_path}")
                tree.write(file_path, encoding='UTF-8', xml_declaration=True)
                return True
        print(f"No 'STATE' tag with VALUE attribute found in: {file_path}")
    except ET.ParseError as e:
        print(f"Failed to parse XML in {file_path}: {e}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    return False

def main():
    current_username = getpass.getuser()
    current_dir = os.getcwd()

    for folder_name in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder_name)
        if os.path.isdir(folder_path):
            file_path = os.path.join(folder_path, 'project.prp')
            if os.path.isfile(file_path):
                update_state_value_in_xml(file_path, current_username)

if __name__ == '__main__':
    main()
