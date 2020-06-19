import chemical_graphs


def parse_flags():
    import argparse
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('template', type=str)
    parser.add_argument('input', type=str)
    parser.add_argument('-p', '--position', help="Comparison of slope & position between input and template graph",
                        dest='cmp_pos', action='store_true')
    parser.set_defaults(cmp_pos=False)
    parser.add_argument('-e', '--error', help="Set error margin", dest='error_margin', type=float, nargs=2)
    parser.set_defaults(error_margin=[1.0, 1.0])
    parser.add_argument('-r', '--rate', help="Rate of approach to template graph", dest='rate_approach', type=float)
    parser.set_defaults(rate_approach=0.5)
    args = parser.parse_args()
    args.error_margin = tuple(args.error_margin)
    if args.error_margin[0] <= 0 or args.error_margin[1] <= 0:
        print("Error margin for both x and y-coordinate should be greater than 0")
        quit(1)
    if not 0 < args.rate_approach < 1:
        print("Rate of approach to template graph should be between 0 and 1")
        quit(1)
    args = vars(args)
    return args


def get_points(filename):
    file = open(filename, 'r')
    points = []
    for line in file:
        pt = line.split(',')
        x = float(pt[0])
        y = float(pt[1])
        points.append((x, y))
    return points


def convert_to_graph(points):
    # Convert list of tuples to graph object
    pass


if __name__ == '__main__':
    flags = parse_flags()
    error = chemical_graphs.get_error_object(flags["error_margin"])