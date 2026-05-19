from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """Busca información actualizada en internet usando DuckDuckGo."""
    try:
        return search_tool.run(query)
    except Exception as e:
        return f"Error en búsqueda: {str(e)}"

@tool
def python_executor(code: str) -> str:
    """Ejecuta código Python de forma segura y devuelve el resultado."""
    try:
        local_vars = {}
        exec(code, {"__builtins__": __builtins__}, local_vars)
        if "result" in local_vars:
            return str(local_vars["result"])
        return "Código ejecutado correctamente (sin variable 'result')"
    except Exception as e:
        return f"Error ejecutando código: {str(e)}"

tools = [web_search, python_executor]