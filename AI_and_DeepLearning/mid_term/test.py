from train import neuralNetwork,dot,transpose,sigmoid,relu,main
def testing(input_list,wih,who):
    #입력 리스트를 2차원 행렬로 변환
    inputs = transpose(input_list)
    #은닉 계층에서 들어오는 신호를 계산
    hidden_inputs=dot(wih,inputs)
    #은닉 계층에서 나가는 신호를 계산
    hidden_outputs=sigmoid(hidden_inputs)
    #최종 출력 계층으로 들어오는 신호를 계산
    final_inputs=dot(who,hidden_outputs)
    #최종 출력 계층에서 나가는 신호를 계산
    final_outputs=sigmoid(final_inputs)
    return final_outputs
def argmax(x): # numpy argmax
    flatten_x = sum(x,[])
    for i,j in enumerate(flatten_x):
        if max(flatten_x) == j:
            return i
def predict(): # 예측값 출력
    dataset = [[3.5064385449265267, 2.34547092892632525, 0], [4.384621956392097, 3.4530853889904205, 0], 
    [4.841442919897487, 4.02507852317520154, 0], [3.5985868973088437, 4.1621314217538705, 0],
     [2.887219775424049, 3.31523082529190005, 0], [9.79822645535526, 1.1052409596099566, 1],
      [7.8261241795117422, 0.6711054766067182, 1], [2.5026163932400305, 5.800780055043912, 1],
       [5.032436157202415, 8.650625621472184, 1], [4.095084253434162, 7.69104329159447, 1]]
    wih,who = main()
    pred_list = []
    label_list = []
    for data in dataset:
        inputs = data[:2]
        correct_label = data[-1]
        label_list.append(correct_label)
        outputs = testing(inputs,wih,who)
        pred_list.append(outputs)
    print(f'predict : {pred_list}')
    return label_list,pred_list
def final_test(): # 정확도 출력
    scorecard = []
    correct_label, pred_list = predict()
    for answer,outputs in zip(correct_label,pred_list):
        label=argmax(outputs)
        
        if label == answer:
            scorecard.append(1)
        else:
            scorecard.append(0)
    
    print(f'accuracy : {sum(scorecard)/len(scorecard)}')
if __name__ == '__main__':
    final_test()
