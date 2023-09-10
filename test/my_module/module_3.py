import module_1

SMALL = module_1.SMALL
N = module_1.N
uniform = module_1.uniform
det = module_1.det
norm = module_1.norm
solve_out_of_the_box = module_1.solve_out_of_the_box


def test_error(solver_function):
    # Сгенерируем хорошо обусловленную систему
    while True:
        a = uniform(0.0, 1.0, (N, N))
        b = uniform(0.0, 1.0, (N,))

        d = det(a)
        if abs(d) <= SMALL:  # Определитель маленький — плохо
            # print(f"det: {d}")
            continue  # Попробуем ещё
        if d < 0.0:  # Отрицательный — поменяем знак
            # print(f"det: {d}")
            a = -a

        try:
            oob_solution = solve_out_of_the_box(a, b)
        except Exception as e:  # Всё-таки система плохая
            # print(f"exc: {e}")
            continue  # Попробуем ещё

        sb = a @ oob_solution
        if norm(sb - b, ord=1) > SMALL:
            # print("Bad solution...")
            continue  # Всё же не очень система получилась =)

        break  # Всё, считаем, что мы случайно сгенерировали хорошую систему

    tested_solution = solver_function(a, b)
    return norm(tested_solution - oob_solution, ord=1)