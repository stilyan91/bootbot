import sys

from stats import word_counter, count_character, print_report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

    
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    

def main():
    file_content = get_book_text(book_path)
    word_counter(file_content)
    count_character(file_content)
    print_report(count_character(file_content))
    
main()