import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np

def plot_decision_tree(train,test=None,clf=None, pair=['petal_length','petal_width'],out=None,max_depth=None,classes=None):
    plot_colors = "ryb"
    plot_step = 0.02

    # We only take the two corresponding features
    X_train = np.array(train[pair])
    y_train = np.array(train['species'])
    if not test is None:
        X_test = np.array(test[pair])
        y_test = np.array(test['species'])
        XX = np.concatenate((X_train,X_test),axis=0)
    else:
        XX = X_train
    # Train
    if clf is None:
        clf = tree.DecisionTreeClassifier(random_state=0,max_depth=max_depth).fit(X_train, y_train)
    else:
        clf = clf.fit(X_train, y_train)
    
    # Plot the decision boundary
    plt.figure(figsize=(10,8))

    x_min, x_max = XX[:, 0].min() - 1, XX[:, 0].max() + 1
    y_min, y_max = XX[:, 1].min() - 1, XX[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    Z[Z == 'setosa'],Z[Z == 'versicolor'],Z[Z == 'virginica'] = 0,1,2

    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)

    plt.xlabel(pair[0])
    plt.ylabel(pair[1])

    if classes is None:
        classes = train['species'].unique()
    # Plot the training points
    for i, color in zip(classes, plot_colors):
        idx = np.where(y_train == i)
        plt.scatter(X_train[idx, 0], X_train[idx, 1], c=color, label=i+"_train",
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=30)
        
        if not test is None:
            idx = np.where(y_test == i)
            plt.scatter(X_test[idx, 0], X_test[idx, 1], c=color, label=i+"_test",
                        cmap=plt.cm.RdYlBu, edgecolor='black', s=20, marker = 's')
            
    print("Train accuracy:",clf.score(train[pair], train['species']))
    print("Test accuracy:",clf.score(test[pair], test['species']))
    plt.title("Decision surface of a decision tree")
    plt.legend(loc='lower right', borderpad=0, handletextpad=0)
    plt.axis("tight")
    if not out is None:
        plt.savefig(out,transparent=True)
    plt.show()
    
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes()
    x = tree.plot_tree(clf,feature_names=pair, class_names=train['species'].unique(),label='none',filled=True,ax=ax)
    plt.show()
    
    
    
def plot_random_forest(clf,train,test=None,pair=['petal_length','petal_width'],out=None,classes=None):
    plot_colors = "ryb"
    plot_step = 0.02

    # We only take the two corresponding features
    X_train = np.array(train[pair])
    y_train = np.array(train['species'])
    if not test is None:
        X_test = np.array(test[pair])
        y_test = np.array(test['species'])
        XX = np.concatenate((X_train,X_test),axis=0)
    else:
        XX = X_train
    # Train
    clf = clf.fit(X_train, y_train)
    
    # Plot the decision boundary
    plt.figure(figsize=(10,8))

    x_min, x_max = XX[:, 0].min() - 1, XX[:, 0].max() + 1
    y_min, y_max = XX[:, 1].min() - 1, XX[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    Z[Z == 'setosa'],Z[Z == 'versicolor'],Z[Z == 'virginica'] = 0,1,2

    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)

    plt.xlabel(pair[0])
    plt.ylabel(pair[1])

    if classes is None:
        classes = train['species'].unique()
    # Plot the training points
    for i, color in zip(classes, plot_colors):
        idx = np.where(y_train == i)
        plt.scatter(X_train[idx, 0], X_train[idx, 1], c=color, label=i+"_train",
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=30)
        if not test is None:
            idx = np.where(y_test == i)
            plt.scatter(X_test[idx, 0], X_test[idx, 1], c=color, label=i+"_test",
                        cmap=plt.cm.RdYlBu, edgecolor='black', s=20, marker = 's')
    print("Train accuracy:",clf.score(train[pair], train['species']))
    print("Test accuracy:",clf.score(test[pair], test['species']))
    plt.title("Decision surface of a decision tree")
    plt.legend(loc='lower right', borderpad=0, handletextpad=0)
    plt.axis("tight")
    if not out is None:
        plt.savefig(out,transparent=True)
    plt.show()
    
    
def plot_tree(clf,features,classes):
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes()
    x = tree.plot_tree(clf,feature_names=features, class_names=classes,label='none',filled=True,ax=ax)
    plt.show()