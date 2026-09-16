import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    total_player = len(sys.argv)
    i = 1
    score_list = []
    while i < total_player:
        try:
            score_list = score_list + [int(sys.argv[i])]
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1
    if len(score_list) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"Scores processed: {score_list}")
        print(f"Total player: {len(score_list)}")            
        print(f"Total score: {sum(score_list)}")        
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}")
    print()


if __name__=="__main__":
    main()
