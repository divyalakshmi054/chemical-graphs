import Resources.GeometricEntities as Ge
import Input.InputInterface as Ii
import argparse


def parse_input():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('-f', '--file', action='store', type=str, required=False, help="Specify File Input")
    args = parser.parse_args()
    if args.file is not None:
        return Ii.InputFile(args.file).get_points()
    else:
        return Ii.InputCommandLine().get_points()


def main():
    points = parse_input()
    for i in points:
        print(i.x, i.y)


if __name__ == "__main__":
    main()
