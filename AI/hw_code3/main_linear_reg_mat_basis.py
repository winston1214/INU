# LINEAR REGRESSION MODEL (Inverse Matrix + Nonlinear Basis)

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # STEP 1: SET DATA ------------------------------------------------------------------------------------------------#
    data_x = np.linspace(1.0, 10.0, 100)[:, np.newaxis]
    data_y = np.sin(data_x) + 0.1 * np.power(data_x, 2) + 0.5 * np.random.randn(100, 1)
    data_x /= np.max(data_x)

    data_x = np.hstack((np.ones_like(data_x), data_x))

    # Set train & test data
    order = np.random.permutation(len(data_x))
    portion = 20
    x_test = data_x[order[:portion]]
    y_test = data_y[order[:portion]]
    x_train = data_x[order[portion:]]
    y_train = data_y[order[portion:]]

    # STEP 2: DO PREDICTION -------------------------------------------------------------------------------------------#
    # Nonlinear basis function
    def apply_exp_basis(X, s=0.5):
        '''201600779 김영민'''
        var = s**2
        mu_ls = np.array([1,0,0.2,0.4,0.6])
        phi = []
        for i in mu_ls:
            phi.append(np.exp(-np.square(X[:,1] - i) / 2*var)) # calculate gaussian basis
        
        Phi = np.array(phi).T
        return Phi

    phi_train = apply_exp_basis(x_train)
    '''201600779 김영민'''
    tmp = np.dot(phi_train.T,phi_train) 
    tmp2 = np.dot(phi_train.T,y_train)
    theta_hat = np.dot(inv(tmp),tmp2)  # 코드 작성시 이부분을 지우세요!.
    ## end
    phi_test = apply_exp_basis(x_test)
    y_pred = np.matmul(phi_test, theta_hat)

    # STEP 3: PLOT ----------------------------------------------------------------------------------------------------#
    ax = plt.figure(figsize=(9, 7), constrained_layout=True).subplots(1, 1)
    ax.plot(x_test[:, 1], y_test, 'bo', label='Ground-truth')
    ax.plot(x_test[:, 1], y_pred, 'ro', label='Prediction')
    plt.legend()
    plt.show()



