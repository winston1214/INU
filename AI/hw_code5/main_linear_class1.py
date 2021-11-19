# LINEAR CLASSIFICATION (SIMPLE)
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # STEP 1: LOAD DATA -----------------------------------------------------------------------------------------------#
    filename2read = "./data_simple.npy"
    filename2read = "./data_difficult.npy"
    data_in = np.load(filename2read, allow_pickle=True)
    x = data_in[()]['x']
    y = data_in[()]['y']

    is_difficult = "difficult" in filename2read

    # STEP 2: SET PLOT-FUNCTION ---------------------------------------------------------------------------------------#
    def plot_data(x, y, theta, iter):
        idx_set = []
        marker_set = ['o', 'v']
        x0min = np.amin(x[:, 1])
        x0max = np.amax(x[:, 1])
        x1min = np.amin(x[:, 2])
        x1max = np.amax(x[:, 2])
        x1range = np.linspace(x0min, x0max, num=100, endpoint=True)
        
        if len(theta) > 0:
            x2range = -theta[1]/theta[2]*(x1range + (theta[0] - 0.5)/theta[1])
        else:
            x2range = []

        fig, ax = plt.subplots(1, figsize=(9, 7), constrained_layout=True)
        for i in [0, 1]:
            idx = np.where(y == i)[0]
            idx_set.append(idx)

        for i, m in enumerate(marker_set):
            if len(idx_set[i]) > 0:
                ax.scatter(x[idx_set[i]][:, 1], x[idx_set[i]][:, 2], marker=m, label='class {}'.format(i))

        if len(x2range) > 0:
            ax.plot(x1range, x2range, 'k:')
        ax.legend()
        ax.set_xlim([x0min - 1, x0max + 1])
        ax.set_ylim([x1min - 1, x1max + 1])
        ax.set_xlabel('x0')
        ax.set_ylabel('x1')
        plt.show(block=False)

        # 그림 저장
        data_type = "diff" if is_difficult else "simple"
        if len(theta) > 0:
            filename2save = "./linear_class1_{:s}_{:d}.png".format(data_type, iter)
        else:
            filename2save = "./data_{:s}.png".format(data_type)
        plt.savefig(filename2save)
        plt.close()

    plot_data(x, y, [], 0)  # Plot

    # STEP 3: Do Gradient ---------------------------------------------------------------------------------------------#
    def get_gradient(theta, x, y):
        # Gradient 구하는 함수
        # Write code here!
        xtx = np.dot(x.T,x) # 201600779 김영민
        gradient =  (1/len(x)) * (np.dot(theta.T,xtx) - np.dot(y.T,x))# 201600779 김영민
        gradient = gradient.T # 201600779 김영민
        loss = (1/len(x)) * np.sum(np.square(np.dot(x,theta)-y))# 201600779 김영민
        
        return gradient, loss

    def step(d, thres=0.5):
        # Step 함수: thres보다 크면 1, 아니면 0
        dnew = np.zeros_like(d)
        idx_pos = np.where(d > thres)
        idx_pos = idx_pos[0]
        if len(idx_pos) > 0:
            dnew[idx_pos, :] = 1.0
        return dnew

    theta_hat = np.random.randn(3, 1)  # theta_hat 초기값을 random하게 정한다.
    alpha = 0.001
    tolerance = 1e-5

    # Perform Gradient Descent
    iter_cnt = 1  # Iteration count
    while True:
        gradient, loss = get_gradient(theta_hat, x, y)  # 매 iteration마다 grad와 loss계산
        theta_hat_new = theta_hat - alpha * gradient  # theta update

        # Stopping Condition
        if (np.sum(abs(theta_hat_new - theta_hat)) < tolerance) or (iter_cnt > 30000):
            print("Converged.")
            is_stop = True
        else:
            is_stop = False

        # Show iteration procedure
        if iter_cnt % 1000 == 0:
            print("Iteration: %d - Loss: %.4f" % (iter_cnt, loss))
        if iter_cnt == 1 or is_stop:
            xtheta = np.matmul(x, theta_hat_new)
            y_pred = step(xtheta)  # step함수 적용
            # Plot
            plot_data(x, y_pred, theta_hat_new, iter_cnt)

        iter_cnt += 1
        theta_hat = theta_hat_new

        if is_stop:
            break

    print("theta =", theta_hat)
