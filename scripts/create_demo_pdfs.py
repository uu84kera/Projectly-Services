from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

OUTPUT_DIR = Path("/Users/huangxin/Downloads/projectly/output/pdf")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

docs = {
    "rag-learning-summary.pdf": [
        "RAG Learning Summary",
        "Retrieval augmented generation finds relevant context before asking a language model to answer.",
        "A typical RAG flow is parse documents, chunk text, create embeddings, retrieve relevant chunks, build a prompt, and generate an answer with sources.",
    ],
    "projectly-requirements-note.pdf": [
        "Projectly Requirements Note",
        "Projectly supports workspaces, projects, epics, sprints, cards, comments, labels, attachments, and GitHub events.",
        "The RAG answer API should return an answer and source citations.",
    ],
    "elasticsearch-search-design.pdf": [
        "Elasticsearch Search Design",
        "Projectly uses Elasticsearch for full text search across projects, cards, comments, and GitHub events.",
        "Card search includes title, description, display ID, labels, status, workspace name, and project name.",
    ],
    "kafka-search-sync-architecture.pdf": [
        "Kafka Search Sync Architecture",
        "FastAPI publishes search events to Kafka after database writes.",
        "The search service consumes projectly.search.events and updates Elasticsearch.",
    ],
    "supabase-attachment-storage-design.pdf": [
        "Supabase Attachment Storage Design",
        "Projectly stores attachment files in the Supabase Storage bucket named projectly-attachments.",
        "Postgres stores attachment metadata including file name, type, size, and storage object key.",
    ],
    "github-integration-notes.pdf": [
        "GitHub Integration Notes",
        "Projectly receives GitHub App webhook events for push and pull request activity.",
        "GitHub events can be matched to cards when commit messages include a card display ID.",
    ],
    "api-error-handling-guide.pdf": [
        "API Error Handling Guide",
        "Projectly APIs return structured error messages for validation, authentication, and duplicate resource conflicts.",
        "Workspace name already exists should be shown below the workspace name input.",
    ],
    "sprint-planning-notes.pdf": [
        "Sprint Planning Notes",
        "A sprint groups cards for a fixed date range.",
        "Sprint cards can be todo, in progress, or done.",
    ],
    "user-feedback-summary.pdf": [
        "User Feedback Summary",
        "Users want sidebar search results to show display ID, title, status, author, and created time.",
        "Users also want comment search results to open card detail and focus the comments section.",
    ],
    "rag-evaluation-questions.pdf": [
        "RAG Evaluation Questions",
        "Good RAG tests include exact lookup questions, summary questions, cross-document questions, and not-found questions.",
        "Answers should cite the attachment file and page number when possible.",
    ],
}

styles = getSampleStyleSheet()

for filename, paragraphs in docs.items():
    path = OUTPUT_DIR / filename
    pdf = SimpleDocTemplate(str(path), pagesize=letter)
    story = []

    story.append(Paragraph(paragraphs[0], styles["Title"]))
    story.append(Spacer(1, 16))

    for text in paragraphs[1:]:
        story.append(Paragraph(text, styles["BodyText"]))
        story.append(Spacer(1, 12))

    story.append(Spacer(1, 24))
    story.append(Paragraph("Generated for Projectly RAG attachment testing.", styles["Italic"]))

    pdf.build(story)
    print(path)
