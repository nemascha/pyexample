
import argparse

def x(x_center, y_center, values):
    print "X center:", x_center
    print "Y center:", y_center
    print "Values:", values

def main():
    parser = argparse.ArgumentParser(description="Do something.")
    parser.add_argument('-x', '--x-center', type=float, required=True)
    parser.add_argument('-y', '--y-center', type=float, required=True)
    parser.add_argument('values', type=float, nargs='*')
    args = parser.parse_args()

    x(args.x_center, args.y_center, args.values)

if __name__ == '__main__':
    main()