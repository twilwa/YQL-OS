def approve_code(tool_to_use):
    print(f"Generated code: {tool_to_use}")
    user_approval = input("Approve code? (yes/no): ")
    if user_approval.lower() == "yes":
        return f"Code approved: {tool_to_use}"
    else:
        return "Code not approved"
