import csv
import sys

def main():
    student_work = dict()
    with open(sys.argv[1], newline='') as input_file:
        csv_reader = csv.DictReader(input_file)
        for row in csv_reader:
            name = row['First name'] + ' ' + row['Last name']
            if not name in student_work:
                student_work[name] = [row['Submission']]
            else:
                student_work[name].append(row['Submission'])

    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = sys.argv[1][:-4]+'-extracted-comments.txt'
    
    with open(output_file, 'w') as out:
        for student, comments in student_work.items():
            out.write(student)
            for number, comment in enumerate(comments):
                out.write(f'\n\n{number+1}     {comment}')
            out.write('\n\n\n')


if __name__ == "__main__":
    main()