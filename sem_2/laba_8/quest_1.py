import pandas as pd
import plotly.express as px


def load_data(filename):
    try:
        return pd.read_csv(filename)
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return None


def create_heatmap(df):
    fig = px.imshow(df.set_index('country')[['health', 'income', 'inflation', 'life_expectancy']],
                    labels=dict(x="Страна", y="Показатель", color="Значение"),
                    color_continuous_scale='Viridis',
                    aspect="auto")

    fig.update_layout(title='Показатели стран',
                      xaxis_title='Страны',
                      yaxis_title='Показатели',
                      height=1000,
                      width=1600)
    return fig

def normalize(df):
    metrics = ['health', 'income', 'inflation', 'life_expectancy']
    for metric in metrics:
        min_val = df[metric].min()
        max_val = df[metric].max()
        df[metric] = (df[metric] - min_val) / (max_val - min_val)
    return df

def main():
    data = load_data('data_country.csv')
    if data is None:
        return
    data = normalize(data)
    fig = create_heatmap(data)
    if fig:
        fig.show()

if __name__ == "__main__":
    main()