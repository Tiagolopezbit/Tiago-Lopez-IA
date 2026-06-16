from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

modelos = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

def evaluar_modelos(modelos, X_train, y_train):
    for nombre, modelo in modelos.items():
        scores = cross_val_score(modelo, X_train, y_train, cv=5, scoring='accuracy')
        print(f'[{nombre}] CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})')
