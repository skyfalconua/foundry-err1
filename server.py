"""AG-UI server example."""

import os

from agent_framework import AIFunction, ChatAgent, ChatClientProtocol, MCPStreamableHTTPTool, ai_function
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from agent_framework.azure import AzureOpenAIChatClient
from azure.core.credentials import AccessToken, TokenCredential
from fastapi import FastAPI
import time

from dotenv import load_dotenv
load_dotenv()


api_key = os.environ.get("AZURE_OPENAI_API_KEY")
endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
deployment_name = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")

server_port = int(os.environ.get("PROJECT_SERVER_PORT") or "8585")

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - - 

class ApiKeyCredential(TokenCredential):
  """Custom TokenCredential that uses an API key as a token."""

  def __init__(self, api_key: str):
    self.api_key = api_key

  def get_token(self, *scopes, **kwargs) -> AccessToken:
    # Return the API key as the token
    # Set expiry far in the future since API keys don't expire like tokens
    expires_on = int(time.time()) + 3600 * 24  # 24 hours from now
    return AccessToken(self.api_key, expires_on)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -

def get_credentials():
  if api_key:
    return ApiKeyCredential(api_key)
  # return AzureCliCredential()

if not endpoint:
  raise ValueError("AZURE_OPENAI_ENDPOINT environment variable is required")
if not deployment_name:
  raise ValueError("AZURE_OPENAI_DEPLOYMENT_NAME environment variable is required")


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -

mcp_server = MCPStreamableHTTPTool(
  name="jira",
  url="http://0.0.0.0:9000/sse",
  load_tools=True,
  load_prompts=True
)

chat_client = AzureOpenAIChatClient(
  credential=get_credentials(),
  endpoint=endpoint,
  deployment_name=deployment_name,
)

agent = ChatAgent(
  name="AGUIAssistant",
  instructions="You are a helpful assistant.",
  chat_client=chat_client,
  tools=mcp_server.functions,
)

# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -

# Create FastAPI app
app = FastAPI(title="AG-UI Server")

# Register the AG-UI endpoint
add_agent_framework_fastapi_endpoint(app, agent, "/")

if __name__ == "__main__":
  import uvicorn

  uvicorn.run(app, host="127.0.0.1", port=server_port)
