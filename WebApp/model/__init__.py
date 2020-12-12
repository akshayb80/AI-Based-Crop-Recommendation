import pickle
def result(n,p,k,temp,hum,ph,rain):
    model=pickle.load(open('decision_tree_classifier.pkl','rb'))
    res= model.predict([[n,p,k,temp,hum,ph,rain]])
    print(f"\n\n{res}\n\n")
    return res
    