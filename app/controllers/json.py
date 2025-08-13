from app.models.entry import EntryCreate, Entry
from typing import List

import json
import os


class JsonController:
    def __init__(self):
        pass

    def build_path(self, file_name: str) -> str:
        curr_dir = os.path.abspath(
            os.path.dirname(
                __file__
            )
        )
        one_up = os.path.abspath(
            os.path.dirname(
                curr_dir
            )
        )
        data_dir = os.path.join(one_up, "data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        json_file_path = os.path.join(data_dir, file_name)

        if not os.path.isfile(json_file_path):
            with open(json_file_path, 'w+', encoding="utf-8-sig") as new:
                json.dump([], new, indent=2)

            return json_file_path

        return json_file_path
    
    def get_entries(self) -> List[Entry]:
        user_file = self.build_path("user.json")

        with open(user_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            entries = []

            for entry in data:
                entries.append(
                    Entry(
                        entry_id = entry["entry_id"],
                        title = entry["title"],
                        details = entry["details"],
                        created_at = entry["created_at"]
                    )
                )

            return entries
        
    def save_entry(self, entry: EntryCreate) -> bool:
        if not entry:
            return False
        
        user_file = self.build_path("user.json")

        with open(user_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            current_entries = data
            current_entries.append(entry.model_dump())

            with open(user_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(current_entries, new, indent=2)

        return True
    
    def get_entry(self, entry_id: int) -> Entry:
        user_file = self.build_path("user.json")

        with open(user_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            for entry in data:
                if entry["entry_id"] == int(entry_id):
                    return Entry(
                        entry_id = entry["entry_id"],
                        title = entry["title"],
                        details = entry["details"],
                        created_at = entry["created_at"]
                    )
                
        return None
    
    def update_entry(self, updated_entry: Entry) -> bool:
        if not updated_entry:
            return False
        
        user_file = self.build_path("user.json")

        with open(user_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            for index, item in enumerate(data):
                entry = data[index]

                if entry["entry_id"] == updated_entry.entry_id:
                    data[index]["title"] = updated_entry.title
                    data[index]["details"] = updated_entry.details

                    with open(user_file, 'w+', encoding="utf-8-sig") as new:
                        json.dump(data, new, indent=2)

                    return True
        
        return False
    
    def delete_entry(self, entry_id: int) -> bool:
        if not entry_id:
            return False
        
        user_file = self.build_path("user.json")

        with open(user_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            current_entries = data
            updated_entries = [entry for entry in current_entries if entry["entry_id"] != int(entry_id)]

            with open(user_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(updated_entries, new, indent=2)

        return True