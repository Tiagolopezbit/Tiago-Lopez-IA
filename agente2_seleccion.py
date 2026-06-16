from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def seleccionar_mejor(modelos, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    mejor_nombre = ''
    mejor_acc = 0
    for nombre, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f'[{nombre}] Test Accuracy: {acc:.4f}')
        if acc > mejor_acc:
            mejor_acc = acc
            mejor_nombre = nombre
    print(f'Mejor modelo: {mejor_nombre} con {mejor_acc:.4f}')
    return mejor_nombre
