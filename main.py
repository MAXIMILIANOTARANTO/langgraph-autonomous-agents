from graph.builder import build_graph

def main():
    print("=== Autonomous Agents Architecture ===\n")
    app = build_graph()

    initial_state = {
        "messages": [],
        "current_task": "Investigar LangGraph y crear un ejemplo simple de uso con herramientas.",
        "context": {},
        "next_agent": "supervisor",
        "is_complete": False,
        "iteration": 0
    }

    result = app.invoke(initial_state, {"configurable": {"thread_id": "project_001"}})
    print("\n=== Ejecución completada ===")
    print(result)

if __name__ == "__main__":
    main()