from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent

GEMINI_MODEL = "gemini-2.5-flash"

#For Agent
for_agent = LlmAgent(
    name="ForAgent",
    model=GEMINI_MODEL,
    instruction="""You are very in favor of the topic suggested.
Based on the user's prompt, write a paragraph that is in favor of the topic.
Output *only* the text. 
""",
    description="Writes a text in favor of the topic.",
    output_key="for_text"
)

#Against Agent
against_agent = LlmAgent(
    name="AgainstAgent",
    model=GEMINI_MODEL,
    instruction="""You are very against of the topic suggested.
Based on the user's prompt, write a paragraph that is against the topic.
Output *only* the text. 
""",
    description="Writes a text against the topic.",
    output_key="against_text"
)

parallel_argument_agent = ParallelAgent(
     name="ParallelArgumentAgent",
     sub_agents=[for_agent, against_agent],
     description="Runs multiple agents in parallel to gather information."
 )

#Compilation Agent
compilation_agent = LlmAgent(
    name="CompilationAgent",
    model=GEMINI_MODEL,
    instruction="""
    Compile the information from {for_text} and {against_text} and compare the two.
 Produce a neutral conclusion along with a summary of what each text discusses.
""",
    description="Produces a comparison of for and against texts.",
    output_key="compilation",
)

display_agent = SequentialAgent(
    name="DisplayAgent",
    sub_agents=[parallel_argument_agent, compilation_agent],
    description="Produces a final display of comparisons",
)

root_agent = display_agent