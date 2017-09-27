def newton(n, x):
    final = (0.5 * (x + (n / x)))
    print('\nMath value: ' + str(final) + '\n')

    for i in range(0, 10):
        final = (0.5 * (final + (n / final)))
        print(str(i+1) + ' - value: ' + str(final))

    return final


n = float(input('What number would you like to squareroot?: '))
x = float(input('Estimate your answer: '))

print ('\nFinal value: ' + str(newton(n, x)))



