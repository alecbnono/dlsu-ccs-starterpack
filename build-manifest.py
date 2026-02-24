import os
import json
import re

# --- CONFIGURATION ---
CONTENT_DIR = "content"
OUTPUT_FILE = "metadata.json"

# Maps your DLSU Course Codes to specific icon keys used in React
COURSE_ICONS = {
    "CCPROG1": "code",
    "CCDSTRU": "binary",
    "CCPROG3": "java",
    "CCINFOM": "database",
}

def clean_slug(filename):
    """
    Removes order prefixes (01-) and 'activity-' tags for clean URLs.
    Example: '02-activity-first-program.md' -> 'first-program'
    """
    # Remove file extension
    name = os.path.splitext(filename)[0]
    # Remove leading numbers and dash (e.g., "01-")
    name = name[3:]
    # Remove "activity-" keyword
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
    return "ACTIVITY" if "activity" in filename.lower() else "LECTURE"

def process_section(section_path, course_name, section_name):
    """Crawls a section folder and returns a list of lesson dictionaries."""
    lessons = []
    # Filter for .md files and sort them to respect the "01-", "02-" prefixes
    files = sorted([f for f in os.listdir(section_path) if f.endswith(".md")])

    for file_name in files:
        lessons.append({
            "title": format_title(file_name),
            "slug": clean_slug(file_name),
            "path": f"{course_name}/{section_name}/{file_name}",
            "type": get_lesson_type(file_name)
        })
    return lessons

def generate_manifest():
    """Main function to crawl the content directory and write the JSON manifest."""
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: Directory '{CONTENT_DIR}' not found.")
        return

    manifest = {"courses": []}

    # 1. Iterate through Courses (e.g., CCPROG1, CCDSTRU)
    course_folders = sorted([f for f in os.listdir(CONTENT_DIR) if os.path.isdir(os.path.join(CONTENT_DIR, f))])

    for course_folder in course_folders:
        course_path = os.path.join(CONTENT_DIR, course_folder)

        course_data = {
            "title": course_folder.upper(),
            "slug": course_folder.lower(),
            "icon_key": COURSE_ICONS.get(course_folder.upper(), "default"),
            "sections": []
        }

        # 2. Iterate through Sections (e.g., 01-Introduction)
        section_folders = sorted([f for f in os.listdir(course_path) if os.path.isdir(os.path.join(course_path, f))])

        for section_folder in section_folders:
            section_path = os.path.join(course_path, section_folder)

            section_data = {
                # Strips the "01-" from "01-Introduction" for the UI title
                "title": format_title(section_folder),
                "lessons": process_section(section_path, course_folder, section_folder)
            }

            course_data["sections"].append(section_data)

        manifest["courses"].append(course_data)

    # 3. Write to File
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4)

    print(f"Successfully generated {OUTPUT_FILE} with {len(manifest['courses'])} courses.")

if __name__ == "__main__":
    generate_manifest()
