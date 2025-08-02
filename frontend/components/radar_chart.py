# app/frontend/components/radar_chart.py

import streamlit as st
import plotly.graph_objects as go

def render_radar_chart(labels, values, title="Psychometric Test Radar Chart"):
    """
    Renders a radar (spider) chart using Plotly and displays it in Streamlit.

    Parameters:
    - labels (List[str]): List of axes/categories (e.g., ["Logical", "Verbal", "Numerical"])
    - values (List[float]): Corresponding scores for each axis (e.g., [80, 65, 90])
    - title (str): Chart title (optional)
    """

    # Ensure the radar chart wraps around (close the polygon)
    if labels[0] != labels[-1]:
        labels.append(labels[0])
        values.append(values[0])

    # Create radar chart figure
    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name='Your Score',
                marker=dict(color='rgba(0,123,255,0.7)')
            )
        ]
    )

    # Update layout aesthetics
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=12)
            )
        ),
        title=title,
        showlegend=False,
        margin=dict(l=30, r=30, t=50, b=30)
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
