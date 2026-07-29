def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    
calculator_schema = {
    "name": "calculator",
    "description": "Perform a basic arithmetic operation (add, subtract, multiply, divide) on two numbers.",
    "parameters": {
        "type": "object",
        "properties": {
            "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["operation", "a", "b"],
    },
}

tools_map={
    "calculator": calculator
}

def execute(tool_call):
    func = tools_map[tool_call["name"]]
    return func(**tool_call["arguments"])


fake_call = {"name": "calculator", "arguments": {"operation": "add", "a": 2, "b": 3}}
result = execute(fake_call)
print(result)