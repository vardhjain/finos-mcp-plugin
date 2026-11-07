"""Add directory display metadata without changing upstream tool execution."""


async def tool_titles(ctx, call_next):
    # The locked SDK serializes handler results before returning to middleware.
    result = await call_next(ctx)
    if ctx.method == "tools/list" and isinstance(result, dict):
        tools = []
        for tool in result.get("tools", []):
            title = tool.get("title") or tool["name"].replace("_", " ").capitalize()
            updated = {**tool, "title": title}
            if tool.get("annotations") is not None:
                updated["annotations"] = {
                    **tool["annotations"],
                    "title": tool["annotations"].get("title") or title,
                }
            tools.append(updated)
        return {**result, "tools": tools}
    return result


def run(create_server):
    """Run the plugin's local stdio server with directory metadata."""
    server = create_server()
    server.middleware.append(tool_titles)
    server.run(transport="stdio")
