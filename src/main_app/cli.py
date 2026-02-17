import sys
sys.path.insert(0, "libs/modules/src")

from algorithms import binary_search, merge_sort


def main():
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original:  {data}")

    sorted_data = merge_sort(data)
    print(f"Sorted:    {sorted_data}")

    target = 27
    index = binary_search(sorted_data, target)
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
