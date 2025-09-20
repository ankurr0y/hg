from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent

GEMINI_MODEL = "gemini-2.5-flash"

#Writer Agent
writer_agent = LlmAgent(
    name="WriterAgent",
    model=GEMINI_MODEL,
    instruction="""You are a story writer.
Based on the user's prompt, write a short story around 1000 words.
Output *only* the text from the story. 
""",
    description="Writes a short story based on user input.",
    output_key="story_text"
)

#Editor Agent
editor_agent = LlmAgent(
    name="EditorAgent",
    model=GEMINI_MODEL,
    instruction="""You are an experienced literary editor with a keen eye for storytelling.
Your task is to provide constructive feedback on the provided short story.

**Story to Review:**
{story_text}

**Review Criteria:**
1.  **Plot and Pacing:** Is the story engaging? Does the plot unfold at a good pace? Are there any plot holes or inconsistencies?
2.  **Character Development:** Are the characters compelling and believable? Are their motivations clear and consistent?
3.  **Prose and Style:** Is the writing clear, vivid, and evocative? Are there issues with grammar, spelling, or punctuation?
4.  **Dialogue:** Does the dialogue sound natural for the characters? Does it effectively reveal character and advance the plot?
5.  **Theme and Tone:** Is there a central theme? Is the tone consistent and effective for the story being told?

**Output:**
Provide your feedback as a concise, bulleted list. Focus on the most important points for improvement, offering specific examples from the text where possible.
If the story is excellent and requires no major changes, simply state: "An excellent story with no major issues found."
Output *only* the review comments or the "no major issues" statement.

""",
    description="Edits the story and provides feedback",
    output_key="review_comments",
)

#Rewriter Agent
rewriter_agent = LlmAgent(
    name="RewriterAgent",
    model=GEMINI_MODEL,
    instruction="""You are a creative writing AI.
Your goal is to improve the given short story based on the provided editorial comments.

**Original Story:**
{story_text}

**Editorial Comments:**
{review_comments}

**Task:**
Carefully apply the suggestions from the comments to rewrite the original story.
If the comments state "An excellent story with no major issues found," return the original story unchanged.
Preserve the core plot and characters while improving the prose, pacing, and dialogue as suggested.

**Output:**
Output *only* the final, rewritten story.
Do not add any other text before or after the story.

""",
    description="Rewritten story based on feedback",
    output_key="story_text",
)

editor_loop_agent = LoopAgent(name="RefinementLoop",
    sub_agents=[
        editor_agent,
        rewriter_agent,
    ],
    max_iterations=5
)


writing_process_agent = SequentialAgent(
    name="WritingProcessAgent",
    sub_agents=[writer_agent, editor_loop_agent],
    description="Executes a sequence of writing, editing, and rewriting.",
)

root_agent = writing_process_agent