import Logic.Verification as V
import Resources.GeometricEntities as Ge

if __name__ == "__main__":
    gp = Ge.Graph([Ge.Point(1, 1), Ge.Point(2, 2), Ge.Point(3, 3)], 1.0, 1.0)
    gi = Ge.Graph([Ge.Point(1, 4), Ge.Point(2, 5.5), Ge.Point(3, 6)], 0.5, 0.5)
    n = V.Normalize(gp)
    n.fit_to_input_pos(gi)
    print(n.tp)
