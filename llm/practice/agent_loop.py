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


# fake_call = {"name": "calculator", "arguments": {"operation": "add", "a": 2, "b": 3}}
# result = execute(fake_call)
# print(result)


def fake_llm(messages, tools):
    # Look at the last message to decide what to "pretend" to respond with
    last_message = messages[-1]

    if last_message["role"] == "user":
        # pretend the model wants to call the calculator tool
        return {
            "tool_calls": [
                {"name": "calculator", "arguments": {"operation": "add", "a": 2, "b": 3}}
            ],
            "text": None,
        }
    else:
        # pretend the model is now ready to answer using the tool result
        return {
            "tool_calls": None,
            "text": "The answer is 5.",
        }
        
        
messages = [{"role": "user", "content": "What is 2 + 3?"}]

while True:
    response = fake_llm(messages, [calculator_schema])

    if response["tool_calls"]:
        for call in response["tool_calls"]:
            result = execute(call)
            messages.append({"role": "tool", "content": str(result)})
    else:
        print(response["text"])
        break

