# @Author 201600779 경제학과 김영민
import math
import random
random.seed(1)
'''
numpy function 구현
'''
def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
    return M
def matrix_addition(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Different Size')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] + B[i][j]
    return C
def matrix_subtraction(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Different Size')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]
    return C
def matrix_mul(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Different Size')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] * B[i][j]
    return C
def transpose(M):
    if not isinstance(M[0],list):
        M = [M]
    rows = len(M)
    cols = len(M[0])
    MT = zeros_matrix(cols, rows)
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]
    return MT
def dot(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        raise ArithmeticError('Different Size')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C
def scalar_mul(scal,A):
    A1 = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
             A1[i][j] = A[i][j]*scal
    return A1
def scalar_sub(scal,A):
    A1 = A.copy()
    for i in range(len(A)):
        for j in range(len(A[0])):
             A1[i][j] = A[i][j]-scal
    return A1
'''
activation function 구현
'''
def sigmoid(ls):
    for i,x in enumerate(ls):
        for j,y in enumerate(x):
            ls[i][j] = 1/(1+math.exp(-y))
    return ls
def relu(ls):
    for i,x in enumerate(ls):
        for j,y in enumerate(x):
            if y<=0:
                ls[i][j] = 0
            else:
                ls[i][j] = y
    return ls

'''
오차 함수의 미분을 이용하여 따로 MSE 함수를 정의 후 사용하지 않고 식에 녹여냈습니다.
'''
class neuralNetwork:
    
    #신경망 초기화하기
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes=inputnodes
        self.hnodes=hiddennodes
        self.onodes=outputnodes
        
        '''
        가중치 행렬 wih와 who
        배열 내 가중치는 w_i_j로 표기, 노드 i에서 다음 계층의 노드 j로 연결됨을 의미
        w11 w21
        w12 w22 등'''
        self.wih = [ [random.random() for i in range(self.inodes)] for i in range(self.hnodes)]
        self.who=[[random.random() for i in range(self.hnodes)] for i in range(self.onodes)]
        
        #학습률
        self.lr=learningrate
        
        #활성화 함수
        # self.activation_function = lambda x: sigmoid(x) # sigmoid 사용
        self.activation_function = lambda x: relu(x) # relu 사용
            
    #신경망 학습시키기
    def update(self, inputs_list,targets_list):
        #입력 리스트를 2차원의 행렬로 반환
        inputs = transpose(inputs_list)
        targets= transpose([targets_list])
        
        #은닉 계층으로 들어오는 신호를 계산
        hidden_inputs=dot(self.wih,inputs)

        #은닉 계층에서 나가는 신호를 계산
        hidden_outputs=self.activation_function(hidden_inputs)

        #최종 출력 계층으로 들어오는 신호를 계산

        final_inputs=dot(self.who,hidden_outputs)
        #최종 출력 계층에서 나가는 신호를 계산
        final_outputs=self.activation_function(final_inputs)
        
        #출력 계층의 오차는(실제값-계산값)
        output_errors = matrix_subtraction(targets*len(final_outputs),final_outputs)

        #은닉 계층의 오차는 가중치에 의해 나뉜 출력 계층의 오차들을 재조합해서 계산
        hidden_errors = dot(transpose(self.who),output_errors)
        
        #은닉 계층과 출력 계층 간의 가중치 업데이트
        
        tmp1 = scalar_sub(1.0,final_outputs)
        tmp1_result = matrix_mul(matrix_mul(output_errors,final_outputs),tmp1)
        
        
        self.who= matrix_addition(self.who,scalar_mul(self.lr,dot(tmp1_result,transpose(hidden_outputs))))
        
        #입력 계층과 은닉 계층 간의 가중치 업데이트
        tmp2 = scalar_sub(1.0,final_outputs)
        tmp2_result = matrix_mul(matrix_mul(hidden_errors,hidden_outputs),tmp2)
        self.wih= matrix_addition(self.wih,scalar_mul(self.lr,dot(tmp2_result,transpose(inputs))))
#         print('wih',self.wih)
        
def training(n,dataset,epochs):  # training function
    for _ in range(epochs):
        for data in dataset:
            inputs = data[:2]
            targets = data[-1]
            n.update(inputs,targets)
    return n.wih,n.who
def main(): # main function
    dataset = [[3.5064385449265267, 2.34547092892632525, 0], [4.384621956392097, 3.4530853889904205, 0], 
    [4.841442919897487, 4.02507852317520154, 0], [3.5985868973088437, 4.1621314217538705, 0],
     [2.887219775424049, 3.31523082529190005, 0], [9.79822645535526, 1.1052409596099566, 1],
      [7.8261241795117422, 0.6711054766067182, 1], [2.5026163932400305, 5.800780055043912, 1],
       [5.032436157202415, 8.650625621472184, 1], [4.095084253434162, 7.69104329159447, 1]]
    input_nodes = 2
    hidden_nodes = 2
    output_nodes = 2
    learning_rate = 0.001
    epochs=136
    n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)
    wih,who = training(n,dataset,epochs)
    print(f'input -> hidden weights : {wih}')
    print(f'hidden -> output weights : {who}')
    return wih,who
if __name__ == '__main__':
    main()