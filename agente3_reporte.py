import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def graficar_comparacion(metricas):
    nombres = list(metricas.keys())
    accuracies = [metricas[n]['test_accuracy'] for n in nombres]
    plt.figure(figsize=(8, 5))
    bars = plt.bar(nombres, accuracies, color=['#4CAF50', '#2196F3', '#FF9800'])
    plt.title('Comparacion de Modelos - Accuracy en Test')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)
    for bar, acc in zip(bars, accuracies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, f'{acc:.4f}', ha='center')
    plt.tight_layout()
    plt.show()

def graficar_confusion(y_test, y_pred, clases, mejor_nombre):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(12, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=clases, yticklabels=clases)
    plt.title(f'Matriz de Confusion - {mejor_nombre}')
    plt.ylabel('Real')
    plt.xlabel('Predicho')
    plt.tight_layout()
    plt.show()
