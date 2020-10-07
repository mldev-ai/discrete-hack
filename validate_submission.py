import argparse

def validate(problines,sublines):
    # Read data from the Problem
    size = problines[1].split()
    M,N = int(size[0]),int(size[1])

    valid,error = True,""
    pieces = []
    for line in sublines:
        line = line.strip()
        entries = line.split()
        if len(entries) > 5:
            return False, f"Incorrect Formatting: {line}"
        
        try:
            cords = []
            for cord in entries[1:]:
                x,y = cord.split(',')
                cords += [(int(x),int(y))]
        except Exception as e:
            return False, e

        if any([x>=M or y>=N for x,y in cords]):
            return False, f"Out of bounds for floor size {M,N}: {line}"

        label = entries[0]
        pieces += [label]
    
    if len(set(pieces)) < len(pieces):
        return False, "Piece used twice. Every piece label can be used at most once"

    return True,""


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Validate discreteHack submission")
    parser.add_argument('--problem', required=True,help="path to problem file")
    parser.add_argument('--submission', required=True,help="path to submission file")

    args = parser.parse_args()

    print("""This script validates that your submission format is correct.\n It DOES NOT check
    piece shapes or forbidden squares.
    
    Usage:\n python validate_submission.py --problem Problem.txt --submission Submission.txt
    """)

    with open(args.problem,'r') as fin:
        problines = fin.readlines()

    with open(args.submission,'r') as fin:
        sublines = fin.readlines()

    valid, error = validate(problines,sublines)
    if valid:
        print("Submission valid")
    else:
        print("Submision invalid\n",error)
