"""Run `pip install yfinance` to install dependencies."""
# IMPORTANT: Before running this script, ensure that the (ANY MODEL )API_KEY environment variable is set.
# To set the API key, follow the instructions below:
# 
# On Windows:
# Open Command Prompt as Administrator and run:
# setx DEEPSEEK_API_KEY "your-api-key-here"
#
# On Unix/Linux:
# Open a terminal and run:
# export DEEPSEEK_API_KEY="your-api-key-here"
#
# NOTE: After setting the API key, restart your terminal or environment to apply the changes  by shuting down the terminal and run the script again.
from phi.agent import Agent, RunResponse  # noqa
from phi.model.deepseek import DeepSeekChat
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=DeepSeekChat(id="deepseek-chat"),
    tools=[
        YFinanceTools(
            company_info=True,
            stock_fundamentals=True,
        )
    ],
    show_tool_calls=True,
    debug_mode=True,
    markdown=True,
)

# Get the response in a variable
# run: RunResponse = agent.run("What is the stock price of NVDA and TSLA")
# print(run.content)

# Print the response on the terminal
agent.print_response("Give me in-depth analysis of NVDA and TSLA")
