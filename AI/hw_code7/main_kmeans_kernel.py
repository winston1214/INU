# K-MEANS ALGORITHM with KERNEL-METHOD
import os
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    MAX_ITER = 10000  # 최대 iteration 횟수
    PIC_ITER = 1  # iteration 그림 저장하는 주기

    dir_pic = "./pic"
    if not os.path.exists(dir_pic):
        os.makedirs(dir_pic)

    # STEP 1: LOAD DATA -----------------------------------------------------------------------------------------------#
    data_in = np.load("data_2.npy", allow_pickle=True)
    p = data_in[()]['p']
    num = data_in[()]['num']

    # STEP 2: RUN K-MEANS ---------------------------------------------------------------------------------------------#
    N = np.shape(p)[0]
    K = len(num)

    def apply_rbf_kernel(p1, p2):
        diff = p1 - p2
        dist = np.sum(diff * diff, axis=1)
        exp_tmp = -1.0 * dist * 10.0
        k_out = np.exp(exp_tmp)
        return k_out

    def get_idx_cluster(p, p_cluster,idx_cluster): # 고치기
        num_k = np.shape(p_cluster)[0]
        idx_cluster = []
        dic = {}
        
        for i in range(num_k):
            dic[i] = []
            idx_tmp = np.where(idx_cluster == i)
            idx_tmp = idx_tmp[0]
            tmp1 = apply_rbf_kernel(p,p)
            if len(idx_tmp):
                pi_c = p[idx_tmp,:]
                nc = len(pi_c)
                tmp2 = 0
                for j in range(len(pi_c)):
                    tmp2 += apply_rbf_kernel(p,np.array([j]))
                
                tmp3 = apply_rbf_kernel(pi_c,pi_c)
                distance = tmp1 - (2/nc * tmp2) + (1/(nc**2))*tmp3
                dic[i].append(distance.tolist())
            else:
                dic[i].append(tmp1.tolist())
        if len(dic[0]) != len(dic[1]):
            print('wrong')
        
        for v in range(len(p)):
            if dic[0][v] > dic[1][v]:
                idx_cluster.append(0)
            else:
                idx_cluster.append(1)
        print(idx_cluster)              
        return idx_cluster

    def update_p_cluster(p, p_cluster, idx_cluster):
        num_k = np.shape(p_cluster)[0]
        
        for i in range(num_k):
            idx_tmp = np.where(idx_cluster == i)
            idx_tmp = idx_tmp[0]
            
            if len(idx_tmp) > 0:
                p_sel = p[idx_tmp, :]
                p_cluster_new = np.mean(p_sel, axis=0)
                p_cluster[i, :] = p_cluster_new

        return p_cluster

    def plot_data(p, p_cluster, idx_cluster, dir_pic, iter):
        num_k = np.shape(p_cluster)[0]
        hcolor = ['r', 'b']

        fig = plt.figure(figsize=plt.figaspect(0.5))
        ax1 = fig.add_subplot(1, 1, 1)
        for i in range(num_k):
            idx_tmp = np.where(idx_cluster == i)
            idx_tmp = idx_tmp[0]

            if len(idx_tmp) > 0:
                p_sel = p[idx_tmp, :]
                ax1.plot(p_sel[:, 0], p_sel[:, 1], 'o', color=hcolor[i], markersize=3.0)
                ax1.plot(p_cluster[i, 0], p_cluster[i, 1], '^', color=hcolor[i], markersize=9.0)
        ax1.axis('equal')
        plt.show(block=False)

        if iter < 0:
            filename2save = "{:s}/kmeans_kernel_init.png".format(dir_pic)
        else:
            filename2save = "{:s}/kmeans_kernel_{:d}.png".format(dir_pic, iter)
        plt.savefig(filename2save)
        plt.pause(0.2)

        plt.close(fig)

    # Run algorithm
    p_cluster = np.random.rand(K, 2)  # 초기 cluster 중심점
    idx_cluster = np.random.randint(0, 1, size=(N,))  # 초기 각 데이터별 cluster-index

    plot_data(p, p_cluster, idx_cluster, dir_pic, -1)  # 초기 결과
    for iter in range(MAX_ITER):
        print("{:d}".format(iter))

        # 이전 idx_cluster
        idx_cluster_old = np.copy(idx_cluster)

        # Centroid와 얼마나 가까운지를 기준으로 cluster를 구한다
        idx_cluster = get_idx_cluster(p, p_cluster,idx_cluster)

        # 새로운 cluster의 중심값을 업데이트
        p_cluster = update_p_cluster(p, p_cluster, idx_cluster)

        # Plot
        if iter % PIC_ITER == 0:
            plot_data(p, p_cluster, idx_cluster, dir_pic, iter)  # 중간 결과 저장

        # idx_cluster의 변화가 없으면 iteration 종료
        diff_idx = np.abs(idx_cluster - idx_cluster_old)
        val_end = np.amax(diff_idx)
        if val_end == 0:
            break

    print("END")
