import numpy as np


def make_matrix(dim):
    zs = np.zeros(shape=(dim, dim - 2))
    o1 = np.ones(shape=(dim, 1))
    o2 = np.random.choice([0, 1], size=(dim, 1))
    mat = np.c_[o1, o2, zs]

    rows = []
    for row in mat:
        rows.append(np.random.permutation(row))
    matn = np.array(rows)

    while np.linalg.det(matn) == 0:
        rows = []
        for row in mat:
            rows.append(np.random.permutation(row))
        matn = np.array(rows)

    return matn


def main():
    matn = make_matrix(4)
    matn_inv = np.linalg.inv(matn)
    xs = matn_inv.sum(axis=1, keepdims=True)

    attempts = 10000
    while (xs == 0.5).all():
        matn = make_matrix(4)
        matn_inv = np.linalg.inv(matn)
        xs = matn_inv.sum(axis=1, keepdims=True)
        attempts -= 1
        print(f'{attempts} attempts')
        if attempts == 0:
            break
    else:
        print(matn)
        print('-' * 40)
        print(matn_inv)
        print('-' * 40)
        print(xs)

    # print(np.linalg.inv(matn))


if __name__ == '__main__':
    main()
