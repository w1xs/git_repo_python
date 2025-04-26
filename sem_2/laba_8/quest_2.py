import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_data(filename):
    try:
        return pd.read_csv(filename)
    except Exception as e:
        print(f"Ошибка загрузки данных: {e}")
        return None

def make_bar_plot(df):
    paid_courses = df[df['is_paid'] == True]
    free_courses = df[df['is_paid'] == False]
    count_paid = len(paid_courses)
    count_free = len(free_courses)
    stats_paid = {
        'max': paid_courses['num_subscribers'].max(),
        'mean': paid_courses['num_subscribers'].mean(),
        'min': paid_courses['num_subscribers'].min()
    }
    stats_free = {
        'max': free_courses['num_subscribers'].max(),
        'mean': free_courses['num_subscribers'].mean(),
        'min': free_courses['num_subscribers'].min()
    }

    level_counts_paid = paid_courses['level'].value_counts()
    level_counts_free = free_courses['level'].value_counts()

    fig = make_subplots(
        rows=3, cols=2,
        specs=[[{"type": "bar", "colspan": 2}, None],
               [{"type": "bar", "colspan": 2}, None],
               [{"type": "bar", "colspan": 2}, None]],
        subplot_titles=("Количество курсов",
                        "Статистика подписчиков",
                        "Количество курсов по уровням")
    )

    fig.add_trace(
        go.Bar(
            x=['Платные', 'Бесплатные'],
            y=[count_paid, count_free],
            name='Количество курсов',
            marker_color=['blue', 'green']
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(
            x=['Максимум', 'Среднее', 'Минимум'],
            y=[stats_paid['max'], stats_paid['mean'], stats_paid['min']],
            name='Платные',
            marker_color='blue'
        ),
        row=2, col=1
    )

    fig.add_trace(
        go.Bar(
            x=['Максимум', 'Среднее', 'Минимум'],
            y=[stats_free['max'], stats_free['mean'], stats_free['min']],
            name='Бесплатные',
            marker_color='green'
        ),
        row=2, col=1
    )

    fig.add_trace(
        go.Bar(
            x=level_counts_paid.index,
            y=level_counts_paid.values,
            name='Платные',
            marker_color='blue'
        ),
        row=3, col=1
    )

    fig.add_trace(
        go.Bar(
            x=level_counts_free.index,
            y=level_counts_free.values,
            name='Бесплатные',
            marker_color='green'
        ),
        row=3, col=1
    )

    fig.update_layout(
        title_text='Сравнение платных и бесплатных курсов Udemy',
        showlegend=True,
        height=1000
    )

    fig.update_xaxes(title_text="Тип курса", row=1, col=1)
    fig.update_yaxes(title_text="Количество", row=1, col=1)
    fig.update_xaxes(title_text="Метрика", row=2, col=1)
    fig.update_yaxes(title_text="Количество подписчиков", row=2, col=1)
    fig.update_xaxes(title_text="Уровень курса", row=3, col=1)
    fig.update_yaxes(title_text="Количество курсов", row=3, col=1)

    return fig

def main():
    data = load_data("udemy_courses_extended.csv")
    fig = make_bar_plot(data)
    fig.show()

if __name__ == "__main__":
    main()