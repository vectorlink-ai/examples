import csv
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--correct-file", help="file with correct answers", required=True)
    parser.add_argument("--test-file", help="guesses", required=True)
    args = parser.parse_args()
    matches = {}
    total = 0
    with open(args.correct_file) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None) # headers
        for row in reader:
            if row[0] in matches:
                matches[row[0]].append(row[1])
            else:
                matches[row[0]] = [row[1]]
            total +=1

    found = 0
    positives = 0
    with open(args.test_file) as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None) # headers
        for row in reader:
            dblp_id = row[0]
            acm_id = row[1]
            distance = row[2]
            if dblp_id in matches:
                found +=1
                if acm_id in matches[dblp_id]:
                    positives +=1
                else:
                    print(f"unmatched record: '{dblp_id}'<=>'{acm_id}', probability: {distance}")
            else:
                print(f"couldn't find: {dblp_id}")


    recall = found / total
    precision = positives / found
    print(f"recall: {recall}")
    print(f"precision: {precision}")

