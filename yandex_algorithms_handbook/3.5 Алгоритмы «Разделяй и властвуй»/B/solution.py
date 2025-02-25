def merge_sorted_lists(list1, list2):
  merged_list = []
  i = j = 0
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i = i + 1
    else:
      merged_list.append(list2[j])
      j = j + 1

  merged_list.extend(list1[i:])
  merged_list.extend(list2[j:])
  return merged_list

def main():
    n = int(input())
    lists = []
    for _ in range(n):
        s = int(input())
        lst = [int(x) for x in input().split()]
        lists.append(lst)

    f_list = lists[0]
    for i in range(1, n):
        f_list = merge_sorted_lists(f_list, lists[i])
    print(*f_list)

if __name__ == "__main__":
    main()