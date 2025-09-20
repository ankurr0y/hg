from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent, ParallelAgent

GEMINI_MODEL = "gemini-2.5-flash"

agent_1 = LlmAgent(
    name="Agent1",
    model=GEMINI_MODEL,
  instruction = """
  """
)

agent_2 = LlmAgent(
    name="Agent2",
    model=GEMINI_MODEL,
    instruction="""
""",
    description="",
)

#Rewriter Agent
agent_3 = LlmAgent(
    name="Agent3",
    model=GEMINI_MODEL,
    instruction="""

""",
    description="",
)

root_agent = LoopAgent(name="",
    sub_agents=[
    ],
    max_iterations=5
)


writing_process_agent = SequentialAgent(
    name="WritingProcessAgent",
    sub_agents=[writer_agent, editor_loop_agent],
    description="Executes a sequence of writing, editing, and rewriting.",
)

root_agent = writing_process_agent
