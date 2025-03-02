import csv
import os

def find_pattern(text, pattern):
    return [i for i in range(len(text)) if text[i:i+len(pattern)] == pattern]

def search_csv(file_path, pattern):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return
    
    total_matches = 0  
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)

        if not rows:
            print(f"Error: File '{file_path}' is empty.")
            return
        
        for row_index, row in enumerate(rows, start=1):
            if row and row[0].strip():
                positions = find_pattern(row[0], pattern)
                match_count = len(positions)

                if match_count > 0:
                    print(f"Pattern '{pattern}' found in row {row_index} at positions {positions} ({match_count} matches)")
                    total_matches += match_count
            
    if total_matches > 0:
        print(f"\n🔍 Total number of matches found: {total_matches}")
    else:
        print("\n❌ No matches found.")

if __name__ == "__main__":
    csv_file = "text.csv"  
    search_pattern = input("🔎 Enter the pattern to search (even a single character): ").strip()
    
    if search_pattern:
        search_csv(csv_file, search_pattern)
    else:
        print("⚠️ Input cannot be empty. Please enter a valid search pattern.")
