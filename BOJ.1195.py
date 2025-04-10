while True:
    alpha = input()
    beta = input()
    beta_r = ''.join(reversed(beta))
    alpha_r = ''.join(reversed(alpha))
    alpha_L = len(alpha)
    beta_L = len(beta)
    L = alpha_L if alpha_L > beta_L else beta_L
    output = list()

    for i in range(4 * L):
        if i < L:
            addi_L = i % L
            alpha_plus = alpha.rjust(alpha_L + addi_L, "5")

            delta = int(alpha_plus) + (int(beta) * (10 ** addi_L))
        # elif i < 2 * L:
        #     addi_L = i % L
        #     beta_plus = beta_r.ljust(beta_L + addi_L, "5")
        #
        #     delta = int(beta_plus) + int(alpha)
        elif i < 3 * L:
            addi_L = i % L
            beta_plus = beta.rjust(beta_L + addi_L, "5")

            delta = int(beta_plus) + (int(alpha) * (10 ** addi_L))
        # else:
        #     addi_L = i % L
        #     alpha_plus = alpha_r.ljust(alpha_L + addi_L, "5")
        #
        #     delta = int(alpha_plus) + int(beta)

        if '4' not in list(str(delta)):
            output.append(len(str(delta)) - str(delta).count('5'))
    output.append(alpha_L + beta_L)
    print(min(output))