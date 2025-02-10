#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
import sys
from datetime import datetime

def sanitize_filename(raw_title: str) -> str:
    """
    Removes or replaces characters not suitable for filenames,
    and converts spaces to underscores.
    """
    sanitized = re.sub(r'[^\w\s-]', '', raw_title, flags=re.UNICODE)
    sanitized = sanitized.strip().replace(" ", "_")
    return sanitized

def extract_timestamp(conversation: dict) -> float:
    """
    Returns update_time if present; otherwise create_time.
    If neither is found, defaults to 0.0 (epoch).
    """
    update_time = conversation.get("update_time")
    if update_time is not None:
        return update_time
    create_time = conversation.get("create_time")
    return create_time if create_time is not None else 0.0

def format_date_from_timestamp(ts: float) -> str:
    """
    Given a Unix timestamp in seconds (float),
    return a string in 'DD.MM.YYYY' format.
    """
    dt = datetime.utcfromtimestamp(ts)
    return dt.strftime("%d.%m.%Y")

def main():
    # Default file to read from
    input_json_path = "conversations.json"
    
    # If the user supplies a different input file, use it
    if len(sys.argv) > 1:
        input_json_path = sys.argv[1]

    # Load the conversations JSON
    with open(input_json_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    # Sort conversations in reverse chronological order (newest first)
    conversations.sort(key=extract_timestamp, reverse=True)

    # Create the output folder "conversations" in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "conversations")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write each conversation in that reverse-chronological order
    for index, conv in enumerate(conversations, start=1):
        ts = extract_timestamp(conv)
        date_str = format_date_from_timestamp(ts)
        raw_title = conv.get("title", "untitled")
        clean_title = sanitize_filename(raw_title)

        # Example filename: "1_Tavus_Kuşu_tüyü_Pazarı_09.02.2025.json"
        filename = f"{index}_{clean_title}_{date_str}.json"
        filepath = os.path.join(output_folder, filename)

        with open(filepath, 'w', encoding='utf-8') as outfile:
            json.dump(conv, outfile, ensure_ascii=False, indent=2)

        print(f"Saved: {filename}")

if __name__ == "__main__":
    main()