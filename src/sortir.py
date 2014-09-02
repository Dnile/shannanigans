__author__ = 'danielby'

from heapq import merge
import click

def merge_sort(m):
    """

    :type m: list
    """
    if len(m) <= 1:
        return m

    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def uniq(sorted_text):
    return sorted(sorted_text)


@click.command()
@click.option('--f', help='text file to read')
def main(f):
    data = open(f).readlines()
    sorted_text = merge_sort(data)
    deduped_text = uniq(sorted_text)
    print deduped_text



if __name__=="__main__":
    main()
