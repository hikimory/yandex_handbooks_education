import sys
from typing import List

def main() -> None:
    users: List[str] = input().split()
    movies: List[str] = input().split()
    count_users: int = len(users)
    count_movies: int = len(movies)

    for _ in range(count_users):
        data: List[str] = input().split()
        if int(data[1]) != count_movies:
            print("NO")
            return

    print("YES")

if __name__ == '__main__':
    main()