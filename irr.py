#PYTHON CODE TO DETERMINE IRR BY ITERATION

def calc_irr(cashflows):
    guess = 0.1
    max_iter = 1000
    tolerance = 1e-6  # Desired level of accuracy

    for i in range(max_iter):
        npv = 0.0
        derivative = 0.0

        for t, cashflow in enumerate(cashflows):
            npv += cashflow / (1 + guess) ** t
            derivative += -t * cashflow / (1 + guess) ** (t + 1)

        guess -= npv / derivative

        if abs(npv) < tolerance:
            return guess

    return None


if __name__ == "__main__":
    cash_flows = [-2000000, -500000, 0, 1500000, 2250000, 3000000]
    irr = calc_irr(cash_flows)

    if irr is not None:
        print(f"The IRR is approximately {irr * 100:.2f}%")
    else:
        print("IRR calculation did not converge.")