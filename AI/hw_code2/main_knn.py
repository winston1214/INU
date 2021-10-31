# K-nearest neighbors on the Iris Flowers Dataset

from random import seed
from random import randrange
from csv import reader
from math import sqrt
import numpy as np

# CSF파일을 불러옴
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# String column을 float로 변환
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


# String column을 int로 변환
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup


# 각 column에 최대값 & 최소값을 구함
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax


# Dataset을 0~1로 맞춤
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


# Dataset을 k-fold로 나눔
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for _ in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split


# Accuracy percentage 계산
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0


# Cross-validation을 이용해서 knn-알고리즘을 평가
def evaluate_algorithm(dataset, knn_algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    # n_folds 만큼의 train & test case를 만든다.
    for fold in folds:
        # train_set 생성
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])

        # test_set 생성
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None

        # knn 알고리즘을 실행!
        predicted = knn_algorithm(train_set, test_set, *args)

        # 결과를 정리
        actual = [row[-1] for row in fold]

        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


# KNN 알고리즘 구현
def knn(train, test, num_neighbors):
    pred_results = list()
    for row in test:
        '''knn 계산 201600779 김영민'''
        dis_list = [] # 거리 저장 리스트
        for train_val in train: # train 값과 비교
            val_t = np.array(train_val[:-1]) # trian
            val_test = np.array(row[:-1]) # test
            distance = np.sum(np.abs(val_t - val_test)) # 거리 계산
            label = train_val[-1] # 정답값 계산
            dis_list.append([distance,label]) # 거리 - 정답값 한 곳에 모아 리스트에 저장
        
        k_list = sorted(dis_list)[:num_neighbors] # 가까운 순서대로 정렬 후 k개 뽑기
        first = k_list[0] # 가장 가까운 값 저장
        k_label_list = np.array(k_list)[:,-1] # 라벨만 저장
        uni,cnt = np.unique(k_label_list,return_counts=True) # k 개의 후보 정답값 중 
        if len(uni)>2 and cnt[0] == cnt[1]: # 동일 순위 검사
            output = first # 1순위를 정답값으로 예측
        else:
            output = uni[np.argmax(cnt)] # 가장 많이 나온 label 값으로 
        pred_results.append(output)
    return (pred_results)


if __name__ == "__main__":
    # Dataset 불러오기
    seed(1)
    filename = './iris.csv'
    dataset = load_csv(filename)

    # Dataset 처리
    for i in range(len(dataset[0]) - 1):
        str_column_to_float(dataset, i)
    str_column_to_int(dataset, len(dataset[0]) - 1)

    # 알고리즘 평가
    n_folds = 5  # cross-validation
    num_neighbors = 5  # knn-classification
    scores = evaluate_algorithm(dataset, knn, n_folds, num_neighbors)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores) / float(len(scores))))
    
