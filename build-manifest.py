import os
import json
import re

# --- CONFIGURATION ---
CONTENT_DIR = "content"
OUTPUT_FILE = "metadata.json"

def clean_slug(filename):
    """
    Removes order prefixes (01-) and 'activity-' tags for clean URLs.
    Example: '02-activity-first-program.md' -> 'first-program'
    """
    name = os.path.splitext(filename)[0][3:]
    name = name.replace("activity-", "")
    return name

def format_title(filename):
    """
    Converts a slug-style filename into a clean Title Case string.
    Example: 'first-program' -> 'First Program'
    """
    slug = clean_slug(filename)
    return slug.replace("-", " ").title()

def get_lesson_type(filename):
    """Determines if a lesson is a lecture or an activity based on filename."""
    return "activity" if "activity" in filename.lower() else "lecture"

def get_course_details(course_path, folder_name):
    """
    Reads course-info.json for rich metadata. 
    Falls back to folder name if the file is missing.
    """
    info_path = os.path.join(course_path, "course-info.json")
    
    if os.path.exists(info_path):
        try:
            with open(info_path, 'r', encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading {info_path}: {e}")
    
    # Fallback/Default data if course-info.json doesn't exist
    return {
        "fullTitle": folder_name.replace("-", " ").title(),
        "courseCode": folder_name.upper(),
        "description": "No description provided for this course.",
        "iconKey": "default"
    }

def process_lessons(section_path, course_folder, section_folder):
    """Crawls a section folder and returns a list of lesson dictionaries."""
    lessons = []
    if not os.path.exists(section_path):
        return lessons

    # Filter for .md files and sort them to respect "01-", "02-" prefixes
    files = sorted([f for f in os.listdir(section_path) if f.endswith(".md")])
    
    for file_name in files:
        lessons.append({
            "title": format_title(file_name),
            "slug": clean_slug(file_name),
            "path": f"{course_folder}/{section_folder}/{file_name}",
            "type": get_lesson_type(file_name)
        })
    return lessons

def generate_manifest():
    """Main function to crawl the content directory and write the JSON manifest."""
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: Directory '{CONTENT_DIR}' not found.")
        return

    manifest = {"courses": []}

    # 1. Get Course Folders (e.g., CCPROG1, CCDSTRU)
    course_folders = sorted([
        f for f in os.listdir(CONTENT_DIR) 
        if os.path.isdir(os.path.join(CONTENT_DIR, f))
    ])

    for course_folder in course_folders:
        course_path = os.path.join(CONTENT_DIR, course_folder)
        
        # Load the rich metadata (Full Title, Desc, Icon, etc.)
        details = get_course_details(course_path, course_folder)
        
        course_data = {
            "title": details.get("fullTitle"),
            "courseCode": details.get("courseCode"),
            "slug": course_folder.lower(),
            "description": details.get("description"),
            "icon_key": details.get("iconKey"),
            "sections": []
        }

        # 2. Get Sections (e.g., 01-Introduction)
        section_folders = sorted([
            f for f in os.listdir(course_path) 
            if os.path.isdir(os.path.join(course_path, f))
        ])

        for section_folder in section_folders:
            section_path = os.path.join(course_path, section_folder)
            
            section_data = {
                # Strips "01-" from folder name for the UI title
                "title": section_folder.replace("-", " ").title()[3:],
                "lessons": process_lessons(section_path, course_folder, section_folder)
            }
            
            # Only add sections that actually have lessons
            if section_data["lessons"]:
                course_data["sections"].append(section_data)
        
        manifest["courses"].append(course_data)

    # 3. Write to File
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)
    
    print(f"✅ Successfully generated {OUTPUT_FILE}")
    print(f"📊 Total Courses processed: {len(manifest['courses'])}")

if __name__ == "__main__":
    generate_manifest()
