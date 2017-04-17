import numpy as np


def load_dataset(dataset_name):
    '''
    data,labels = load_dataset(dataset_name)

    Load a given dataset

    Returns
    -------
    data : numpy ndarray
    labels : list of str
    '''
    data = []
    labels = []
    with open('./data/{0}.tsv'.format(dataset_name)) as ifile:
        for line in ifile:
            tokens = line.strip().split('\t')
            data.append([float(tk) for tk in tokens[:-1]])
            labels.append(tokens[-1])
    print('\n面积A 周长P 紧密度C 谷粒长度 宽度 偏度系数 谷粒槽长度')
    print('data[:10]=',data[:10],'\n')
    data = np.array(data)