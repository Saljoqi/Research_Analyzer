import reflex as rx
import asyncio
# Import your existing logic (adjust the path if necessary)
# from src.main import run_research_assistant 

class State(rx.State):
    """The app state handles data and interaction logic."""
    topic: str = ""
    question: str = ""
    is_working: bool = False
    summary: str = ""
    answer: str = ""
    sources: list[dict] = []

    # async def run_analysis(self):
    #     """Triggers your research assistant logic."""
    #     if not self.topic or not self.question:
    #         return rx.window_alert("Please enter both a topic and a question!")

    #     self.is_working = True
    #     yield  # Refresh UI to show loading state

    #     # Mocking the call to your logic for now
    #     # result = run_research_assistant(self.topic, self.question)
        
    #     # Simulate processing time
    #     await asyncio.sleep(2) 
        
    #     self.summary = "Executive Summary: LoRA significantly reduces VRAM usage..."
    #     self.answer = "LoRA saves approximately 70-80% VRAM compared to full fine-tuning."
    #     self.sources = [
    #         {"title": "LoRA: Low-Rank Adaptation", "page": 4, "url": "https://arxiv.org/abs/2106.09685"},
    #     ]
        
    #     self.is_working = False


    async def run_analysis(self):
        """Triggers your research assistant logic."""
        if not self.topic or not self.question:
        # 1. Logic check: Show alert
        # In Reflex, you can't return a component from a state method.
        # Instead, we just exit or trigger another event.
            return rx.window_alert("Please enter both a topic and a question!")

    # 2. START OF PROCESS
        self.is_working = True
        yield  # This 'yield' updates the UI to show the loading spinner

        try:
            # Simulate processing time or call your real logic here
            # result = run_research_assistant(self.topic, self.question)
            await asyncio.sleep(2) 
        
            self.summary = "Executive Summary: LoRA significantly reduces VRAM usage..."
            self.answer = "LoRA saves approximately 70-80% VRAM compared to full fine-tuning."
            self.sources = [
            {"title": "LoRA: Low-Rank Adaptation", "page": 4, "url": "https://arxiv.org/abs/2106.09685"},
            ]
        finally:
            # 3. END OF PROCESS
            self.is_working = False
            # No 'yield' needed here unless you want to update UI 
            # before the function fully finishes.











def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("🔬 AI Research Assistant", size="9", color_scheme="blue"),
            rx.text("Deep analysis of arXiv papers using Local Llama3", color_scheme="gray"),
            
            # Input Section
            rx.card(
                rx.vstack(
                    rx.input(placeholder="Enter Research Topic...", on_blur=State.set_topic, width="100%"),
                    rx.input(placeholder="What is your specific question?", on_blur=State.set_question, width="100%"),
                    rx.button(
                        "Start Deep Analysis", 
                        on_click=State.run_analysis, 
                        loading=State.is_working,
                        width="100%",
                        color_scheme="blue"
                    ),
                    spacing="4",
                ),
                width="100%",
                padding="6",
            ),

            # Results Section (Only shows if there is an answer)
            rx.cond(
                State.answer != "",
                rx.vstack(
                    rx.divider(),
                    rx.heading("Analysis Results", size="7"),
                    rx.text(State.summary, font_weight="bold"),
                    rx.text(State.answer),
                    rx.heading("Verified Sources", size="4"),
                    rx.foreach(
                        State.sources,
                        lambda s: rx.link(
                            f"-> {s['title']} [Page {s['page']}]",
                            href=s["url"],
                            is_external=True,
                            color_scheme="blue"
                        )
                    ),
                    spacing="5",
                    width="100%",
                    align="start"
                )
            ),
            width="600px",
            spacing="7",
            padding_top="10%",
        ),
        width="100%",
        height="100vh",
        background_color="var(--gray-2)",
    )

app = rx.App()
app.add_page(index)