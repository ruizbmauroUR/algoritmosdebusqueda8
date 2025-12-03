import streamlit as st
import pandas as pd
import time
from maze_solver import MAZE, START, END, solve_maze_bfs, solve_maze_dfs, solve_maze_a_star

st.title("Visualizador de Algoritmo de Busqueda en Laberinto")
st.title("Mauro Ruiz Bernal 744817")

# FunciÃ³n para renderizar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    # Convertir el laberinto a un formato que Streamlit pueda mostrar fÃ¡cilmente,
    # por ejemplo, una tabla o usando st.markdown con emojis/colores.
    # Para una mejor visualizaciÃ³n interactiva, podrÃ­as usar bibliotecas como Pygame o Plotly, 
    # pero para un inicio, un enfoque simple es suficiente.

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀") # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁") # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🔹") # Camino resuelto
            elif col == 1:
                display_row.append("⬛") # Muro
            else:
                display_row.append("⬜") # Camino libre
        display_maze.append("".join(display_row))
    
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar para controles
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS", "DFS", "A*"])
solve_button = st.sidebar.button("Resolver Laberinto")

render_maze(MAZE)
#aqui va la opcion de Resolver Laberinto
if solve_button:
    if algorithm == "BFS":
        start_time = time.time()
        path = solve_maze_bfs(MAZE, START, END)
        if path:
            st.success(f"¡Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
            end_time = time.time()
            tiempo_ejecucion = end_time - start_time
            st.write(f"Tiempo tomado: {tiempo_ejecucion:.5f} segundos")
    elif algorithm == "DFS":
        start_time = time.time()
        path = solve_maze_dfs(MAZE, START, END)
        if path:
            st.success(f"¡Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
            end_time = time.time()
            tiempo_ejecucion = end_time - start_time
            st.write(f"Tiempo tomado: {tiempo_ejecucion:.5f} segundos")
    elif algorithm == "A*":
        start_time = time.time()
        path = solve_maze_a_star(MAZE, START, END)
        if path:
            st.success(f"¡Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
            end_time = time.time()
            tiempo_ejecucion = end_time - start_time
            st.write(f"Tiempo tomado: {tiempo_ejecucion:.5f} segundos")
    else:
        st.warning(f"El algoritmo {algorithm} aÃºn no estÃ¡ implementado. Usa BFS.")
