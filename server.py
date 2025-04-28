## Copyright (c) 2025 Cloudera, Inc. All Rights Reserved.
##
## This file is licensed under the Apache License Version 2.0 (the "License").
## You may not use this file except in compliance with the License.
## You may obtain a copy of the License at http:##www.apache.org/licenses/LICENSE-2.0.
##
## This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
## OF ANY KIND, either express or implied. Refer to the License for the specific
## permissions and limitations governing your use of the file.

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

from tools import impala_tools
import os

mcp = FastMCP(name="Cloudera Iceberg MCP Server via Impala")

# Register functions as MCP tools
@mcp.tool()
def execute_query(query: str) -> str:
    """
    Execute a SQL query on the Impala database and return results as JSON.
    """
    return impala_tools.execute_query(query)

@mcp.tool()
def get_schema() -> str:
    """
    Retrieve the list of table names in the current Impala database.
    """
    return impala_tools.get_schema()

if __name__ == "__main__":
    # Get transport type from environment variable or default to 'stdio'
    transport = os.getenv('MCP_TRANSPORT', 'stdio')

    # Initialize and run the server
    mcp.run(transport=transport)
