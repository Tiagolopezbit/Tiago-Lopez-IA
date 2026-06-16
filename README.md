#  Sistema de 3 Agentes - Prediccion de Especies de Ranas

## Descripcion
Sistema multiagente de Machine Learning para predecir la especie de rana a partir de coordenadas GPS, fecha y provincia. Dataset: Australian FrogID (136,621 registros).

## Agentes
- **Agente 1 - Normalizador:** limpia, imputa, escala y codifica el dataset
- **Agente 2 - Entrenador:** aplica validacion cruzada, entrena 3 modelos y selecciona el mejor
- **Agente 3 - Comunicador:** genera reporte en lenguaje natural y graficas

## Modelos evaluados
| Modelo | CV Accuracy | Test Accuracy |
|---|---|---|
| Random Forest | 39.40% | 37.67% |
| Decision Tree | 37.10% | 35.30% |
| KNN | 44.07% | 43.40% |

## Resultado
El mejor modelo fue **KNN** con 43.40% de accuracy en test.

## Tecnologias
- Python, Pandas, Scikit-learn, Matplotlib, Seaborn
- Google Colab
