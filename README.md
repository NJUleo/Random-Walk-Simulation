# Random Walk Simulation

## Computing Module

## Module 12.2.1

$$
x_i, i = 0, 1, ..., 383
$$


$$
A_n = \frac
		{\Sigma_{i = 1}^{n}x_{i - 1}(x_i - x_{i - 1})}
		{\Sigma_{i = 1}^{n} x_{i - 1}^{2}}
\cdot
	\frac
		{1}
		{\sqrt
			{\frac{1}{n}
				\Sigma_{i = 1}^{n}(x_i - \overline{x})^2}}
				\newline
				n = 2, 3, ..., 383
$$

$$
Sup\,A_n = max_{n = 30}^{383}(A_n)
$$

For convenience, define the following names:
$$
B_n = \Sigma_{i = 1}^{n}x_{i - 1}(x_i - x_{i - 1})
$$

$$
C_n =\Sigma_{i = 1}^{n} x_{i - 1}^{2}
$$

$$
D_n = \Sigma_{i = 1}^{n}(x_i - \overline{x})^2
$$

## Module 12.2.2

$$
A_n = n\cdot
	\frac
		{\Sigma_{i = 1}^{n}x_{i - 1}(x_i - x_{i - 1})
		}
		{\Sigma_{i - 1}^{n}x_{i - 1}^2}
$$

$$
Sup\,A_n = max_{n = 30}^{383}(A_n)
$$

For convenience, define the following names:
$$
B_n = \Sigma_{i = 1}^{n}x_{i - 1}(x_i - x_{i - 1})
$$

$$
C_n =\Sigma_{i = 1}^{n} x_{i - 1}^{2}
$$