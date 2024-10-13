from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

task = "Write a report on TSLA."

finance_agent = Agent(
    model=OpenAIChat(id="gpt-4o-2024-08-06"),
    tools=[YFinanceTools(enable_all=True)],
    show_tool_calls=True,
    markdown=True,
    reasoning=True,
    # debug_mode=True,
)

finance_agent.print_response(task, stream=True, show_full_reasoning=True)