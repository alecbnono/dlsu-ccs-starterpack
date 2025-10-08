import os
import json


def clean_name(name):
    clean = name[3:].replace("-", " ").title()
    return clean


def lesson_filter(name):
    if name.endswith(".md"):
        if name.lower().startswith("readme"):
            return False
        return True
    return False


def generate_lesson(name, section_path):
    base_name = os.path.splitext(name)[0]
    lesson = {
        "title": clean_name(base_name),
        "path": f"{section_path}/{base_name}".replace("\\", "/")
    }
    return lesson


def generate_section(name, course_path):
    section_path = f"/{course_path}/{name}".replace("\\", "/")
    section_dir = os.path.join(course_path, name)
    lessons = [
        generate_lesson(f, section_path)
        for f in os.listdir(section_dir)
        if lesson_filter(f)
    ]
    return {"title": clean_name(name), "lessons": lessons}


def generate_course(name, base_path):
    course_path = os.path.join(base_path, name)
    course_entry = {
        "course": name,
        "title": name,
        "path": f"/{name}",
        "sections": []
    }

    for section_name in os.listdir(course_path):
        section_dir = os.path.join(course_path, section_name)
        if os.path.isdir(section_dir):
            section = generate_section(section_name, name)
            course_entry["sections"].append(section)

    return course_entry


def build_manifest(base_path):
    manifest = []

    for course_name in os.listdir(base_path):
        course_dir = os.path.join(base_path, course_name)
        if os.path.isdir(course_dir) and not course_name.startswith("."):
            course_entry = generate_course(course_name, base_path)
            manifest.append(course_entry)

    return manifest


if __name__ == "__main__":
    data = build_manifest(".")
    with open("manifest.json", "w") as f:
        json.dump(data, f, indent=2)
    print("✅ Manifest generated successfully.")
