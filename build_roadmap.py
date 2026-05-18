#!/usr/bin/env python3
"""
AI ENGINEER 180-DAY ROADMAP PDF GENERATOR
Caveman build - pure execution focus
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from datetime import datetime, timedelta

# PDF setup
OUTPUT_FILE = "/home/error28/Desktop/ai-backend-foundation/AI_ENGINEER_ROADMAP_180_DAYS.pdf"
doc = SimpleDocTemplate(OUTPUT_FILE, pagesize=A4, 
                       rightMargin=0.5*inch, leftMargin=0.5*inch,
                       topMargin=0.5*inch, bottomMargin=0.5*inch)

# Styles
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

phase_style = ParagraphStyle(
    'Phase',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#d32f2f'),
    spaceAfter=8,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

week_style = ParagraphStyle(
    'Week',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#1976d2'),
    spaceAfter=6,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

task_style = ParagraphStyle(
    'Task',
    parent=styles['Normal'],
    fontSize=9,
    spaceAfter=3,
    leftIndent=20
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontSize=8,
    fontName='Courier',
    textColor=colors.HexColor('#424242'),
    leftIndent=25,
    spaceAfter=2
)

checkpoint_style = ParagraphStyle(
    'Checkpoint',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#f57c00'),
    fontName='Helvetica-Bold',
    spaceAfter=4,
    leftIndent=20
)

# Title page
story.append(Paragraph("AI INTEGRATION ENGINEER", title_style))
story.append(Paragraph("180-DAY MASTERY ROADMAP", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("TARGET: Production AI Engineer by July 2026", styles['Normal']))
story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# Mission statement
mission = """
<b>MISSION:</b> Transform from CSE student to hireable AI Integration Engineer in 6 months.
Build real deployed systems. Reach teaching-level understanding. No tutorial addiction.
"""
story.append(Paragraph(mission, styles['Normal']))
story.append(Spacer(1, 0.2*inch))

# Core rules
rules_data = [
    ["RULE", "ENFORCEMENT"],
    ["NO new projects", "Only Pathly v2 until Phase 6"],
    ["Weekly deployment", "Live URL required every Sunday"],
    ["Daily GitHub commit", "Meaningful code, not doc updates"],
    ["Break & Rebuild", "Every 2 weeks - delete & rebuild from memory"],
    ["Teaching proof", "Video/blog/diagram every week"],
    ["No tutorial >30min/day", "Build first, watch after 3 failures"],
]

rules_table = Table(rules_data, colWidths=[2*inch, 3.5*inch])
rules_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#d32f2f')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
]))
story.append(rules_table)
story.append(PageBreak())

# Overview timeline
story.append(Paragraph("TIMELINE OVERVIEW", phase_style))

timeline_data = [
    ["PHASE", "WEEKS", "DELIVERABLE", "KEY SKILL"],
    ["Backend Foundation", "Week 1-8", "Pathly API + DB", "FastAPI + Supabase"],
    ["RAG Systems", "Week 9-12", "Doc QA Engine", "Embeddings + Vector DB"],
    ["Agent Systems", "Week 13-16", "AI Career Agent", "Tool calling + Orchestration"],
    ["Production Systems", "Week 17-20", "Scaled Pathly", "Monitoring + Optimization"],
    ["Interview Prep", "Week 21-24", "Mock interviews", "System design + Algorithms"],
    ["Job Hunt", "Week 25-26", "20+ applications", "Portfolio polish"],
]

timeline_table = Table(timeline_data, colWidths=[1.5*inch, 1*inch, 1.8*inch, 1.7*inch])
timeline_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976d2')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
]))
story.append(timeline_table)
story.append(Spacer(1, 0.2*inch))

# Stack
story.append(Paragraph("<b>TECH STACK (NO CHANGES ALLOWED):</b>", styles['Normal']))
stack = "Backend: FastAPI, Python | Database: Supabase (PostgreSQL + pgvector) | AI: OpenRouter API | Frontend: Flutter/Dart | Deploy: Railway/Render | Tools: Git, Docker, pytest"
story.append(Paragraph(stack, styles['Normal']))
story.append(PageBreak())

# DETAILED ROADMAP
story.append(Paragraph("DETAILED EXECUTION PLAN", phase_style))

# PHASE 1: BACKEND FOUNDATION (Weeks 1-8) - Mostly complete, just finish
story.append(Paragraph("PHASE 1: BACKEND FOUNDATION (Days 1-56)", phase_style))
story.append(Paragraph("STATUS: 40% COMPLETE - FINISH THIS FIRST", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

# Week 8: Complete Foundation
story.append(Paragraph("□ Week 8: Complete Backend Foundation", week_style))
tasks_w8 = [
    "□ Day 1-2: Supabase integration + database.py client",
    "□ Day 3-4: User CRUD repository + routes",
    "□ Day 5: Learning path CRUD operations",
    "□ Day 6: Error handling + logging middleware",
    "□ Day 7: Testing setup (pytest) + coverage >70%",
]
for task in tasks_w8:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("CHECKPOINT: Sunday 8PM", checkpoint_style))
checkpoint_w8 = [
    "✓ Supabase has real user data (screenshot)",
    "✓ All API routes working (curl/Postman)",
    "✓ Tests passing (pytest output)",
    "✓ GitHub: 25+ commits this week",
]
for item in checkpoint_w8:
    story.append(Paragraph(item, task_style))
story.append(Spacer(1, 0.1*inch))

# ChatGPT prompts
story.append(Paragraph("<b>ChatGPT Prompts for Week 8:</b>", styles['Normal']))
prompts_w8 = [
    '"Help me debug this Supabase connection error: [paste error]"',
    '"Review this repository pattern code for best practices"',
    '"Explain async vs sync database calls in FastAPI"',
    '"What tests should I write for user CRUD endpoints?"',
]
for p in prompts_w8:
    story.append(Paragraph(p, code_style))
story.append(PageBreak())

# PHASE 3: RAG PIPELINE (Weeks 9-12)
story.append(Paragraph("PHASE 3: RAG PIPELINE MASTERY (Days 61-90)", phase_style))
story.append(Spacer(1, 0.1*inch))

# Week 9-10
story.append(Paragraph("□ Week 9: Document Processing Engine", week_style))
tasks_w9 = [
    "□ Day 1-2: Build text chunker (sliding window, 512 tokens, 50 overlap)",
    "  └ Code: rag/chunker.py - NO libraries, pure Python",
    "  └ Test: 100-page PDF → 500 chunks in <2sec",
    "□ Day 3-4: Embedding pipeline (sentence-transformers)",
    "  └ Code: rag/embedder.py",
    "  └ Benchmark: 1000 chunks embedded in <30sec",
    "□ Day 5-6: Supabase pgvector integration",
    "  └ SQL: CREATE TABLE + vector index (HNSW)",
    "  └ Code: db/vector_ops.py - bulk upsert",
    "□ Day 7: BREAK & REBUILD - Delete all RAG code, rebuild in 4hrs",
]
for task in tasks_w9:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("DEPLOY: POST /rag/ingest endpoint on Railway", checkpoint_style))
story.append(Paragraph("TEACH: 5-min video on 'Why chunk size matters'", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 10: Retrieval System", week_style))
tasks_w10 = [
    "□ Day 1-2: Hybrid search (vector similarity + BM25 keyword)",
    "  └ Implement reciprocal rank fusion",
    "□ Day 3-4: Context assembly + token counting (tiktoken)",
    "  └ Handle context window (8k tokens max)",
    "  └ Chunk reordering (lost-in-middle fix)",
    "□ Day 5-6: Generation pipeline (OpenRouter streaming)",
    "  └ Citation extraction from sources",
    "  └ Rate limiting + retry logic",
    "□ Day 7: Integration testing + deployment",
]
for task in tasks_w10:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("DEPLOY: Pathly feature 'Ask about career advice'", checkpoint_style))
story.append(Paragraph("TEACH: Blog post 'Why most RAG systems fail'", checkpoint_style))
story.append(PageBreak())

# Week 11-12
story.append(Paragraph("□ Week 11: Advanced RAG Patterns", week_style))
tasks_w11 = [
    "□ Day 1-2: Query expansion + rewriting",
    "□ Day 3-4: Reranking with cross-encoder",
    "□ Day 5-6: Caching embeddings + responses",
    "□ Day 7: Performance optimization (<2sec queries)",
]
for task in tasks_w11:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("□ Week 12: RAG Deep-Dive Project", week_style))
tasks_w12 = [
    "□ Build 'DocuMind' - standalone RAG system",
    "□ Support PDF/DOCX/TXT upload",
    "□ Compare 3 retrieval strategies (document in notebook)",
    "□ Cost analysis per 1000 queries",
    "□ Deploy as separate repo (portfolio project #2)",
]
for task in tasks_w12:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("CHECKPOINT: Bi-weekly assessment", checkpoint_style))
assessment_rag = [
    "✓ Build RAG system for job postings in 60min (timed)",
    "✓ No Google, only bookmarked docs",
    "✓ Score >70% or repeat weeks 11-12",
]
for item in assessment_rag:
    story.append(Paragraph(item, task_style))
story.append(PageBreak())

# PHASE 4: AGENT SYSTEMS (Weeks 13-16)
story.append(Paragraph("PHASE 4: AGENTIC SYSTEMS (Days 91-120)", phase_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 13: Function Calling & Tools", week_style))
tasks_w13 = [
    "□ Day 1-3: Build ToolRegistry from scratch",
    "  └ Tools: web_search, code_executor, db_query, file_reader",
    "  └ Parameter validation + execution sandbox",
    "□ Day 4-6: Agent execution loop",
    "  └ LLM decides action → validate → execute → feed back",
    "  └ Max iterations, timeout, cost tracking",
    "  └ Test: 'Find top 3 AI papers this week + summarize'",
    "□ Day 7: BREAK & REBUILD - New agent for GitHub repo analysis",
]
for task in tasks_w13:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("DEPLOY: Pathly AI Career Agent", checkpoint_style))
story.append(Paragraph("TEACH: Jupyter notebook 'Build AI agent in 30min'", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 14: Multi-Agent Orchestration", week_style))
tasks_w14 = [
    "□ Day 1-3: Router + specialized agents architecture",
    "  └ Agents: Research, Gap Analysis, Curriculum, Resource",
    "□ Day 4-6: Pathly AI Mentor system",
    "  └ User: 'Become ML engineer'",
    "  └ Output: 12-week personalized roadmap in <60sec",
    "□ Day 7: Performance optimization (parallel execution)",
]
for task in tasks_w14:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("DEPLOY: Full AI Mentor in Pathly v2", checkpoint_style))
story.append(PageBreak())

story.append(Paragraph("□ Week 15-16: Agent Project + Optimization", week_style))
tasks_w15_16 = [
    "□ Build 'CodeReviewBot' (portfolio project #3)",
    "  └ GitHub App: automated PR analysis",
    "  └ Multi-step reasoning, tool integration",
    "  └ Async processing, cost monitoring",
    "□ Complete 10+ example PR reviews",
    "□ Write technical deep-dive blog post",
    "□ Architecture diagram + deployment",
]
for task in tasks_w15_16:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("CHECKPOINT: Bi-weekly assessment", checkpoint_style))
assessment_agent = [
    "✓ Explain multi-agent system (20-min recorded presentation)",
    "✓ Identify when to use single vs multi-agent",
    "✓ Cost comparison table documented",
]
for item in assessment_agent:
    story.append(Paragraph(item, task_style))
story.append(PageBreak())

# PHASE 5: PRODUCTION SYSTEMS (Weeks 17-20)
story.append(Paragraph("PHASE 5: PRODUCTION ENGINEERING (Days 121-150)", phase_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 17: Observability", week_style))
tasks_w17 = [
    "□ Day 1-2: Structured logging (correlation IDs, JSON format)",
    "□ Day 3-4: Metrics (latency p50/p95/p99, error rate, cost tracking)",
    "  └ Setup Prometheus + Grafana OR custom dashboard",
    "□ Day 5-6: Error recovery patterns",
    "  └ Exponential backoff, circuit breaker, graceful degradation",
    "□ Day 7: Chaos engineering (kill services, inject delays)",
]
for task in tasks_w17:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("DEPLOY: Public status page (status.pathly.app)", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 18: Scaling & Cost Optimization", week_style))
tasks_w18 = [
    "□ Day 1-2: Database optimization (indexes, query tuning)",
    "□ Day 3-4: Caching strategy (Redis, CDN, LLM response cache)",
    "  └ Target: 60% reduction in OpenRouter calls",
    "□ Day 5-6: Async task processing (Celery/RQ + WebSockets)",
    "□ Day 7: Load testing (Locust - 1000 concurrent users)",
]
for task in tasks_w18:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("BENCHMARK: 50 concurrent users, <2sec latency", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 19-20: Production Hardening", week_style))
tasks_w19_20 = [
    "□ Security audit (API auth, rate limiting, input sanitization)",
    "□ Deployment automation (CI/CD with GitHub Actions)",
    "□ Backup strategy (DB snapshots, disaster recovery)",
    "□ Documentation (API docs, architecture diagrams, runbooks)",
    "□ Cost calculator tool (HTML widget for Pathly)",
]
for task in tasks_w19_20:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("TEACH: Build 'Production Readiness Checklist' (20 points)", checkpoint_style))
story.append(PageBreak())

# PHASE 6: INTERVIEW WARFARE (Weeks 21-26)
story.append(Paragraph("PHASE 6: INTERVIEW & JOB HUNT (Days 151-180)", phase_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 21-22: System Design Mastery", week_style))
tasks_w21_22 = [
    "□ Design exercises (no coding, only diagrams):",
    "  └ Day 1-2: RAG system for 10M users",
    "  └ Day 3-4: Code review agent architecture",
    "  └ Day 5-6: A/B testing framework for LLM prompts",
    "□ Day 7: 3 mock interviews on Pramp/Interviewing.io",
    "□ Record feedback, identify weak areas",
]
for task in tasks_w21_22:
    story.append(Paragraph(task, task_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 23-24: Algorithms & Python Deep-Dive", week_style))
tasks_w23_24 = [
    "□ Day 1-3: LeetCode (15 problems - AI use cases)",
    "  └ LRU Cache, Search Autocomplete, Rate Limiter",
    "  └ Sliding Window, Trie Implementation",
    "□ Day 4-5: Python internals (decorators, async, generators)",
    "□ Day 6-7: FastAPI deep-dive (DI, middleware, background tasks)",
]
for task in tasks_w23_24:
    story.append(Paragraph(task, task_style))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("□ Week 25-26: Portfolio Polish + Applications", week_style))
tasks_w25_26 = [
    "□ Day 1-2: GitHub profile optimization",
    "  └ Pathly v2 README (demo video, architecture, benchmarks)",
    "  └ Pin 3 repos: Pathly, DocuMind, CodeReviewBot",
    "□ Day 3-4: Write 3 technical blog posts",
    "  └ Publish on dev.to, Medium, Hashnode, LinkedIn",
    "□ Day 5-7: Job applications (TARGET: 20 applications)",
    "  └ Companies: Sarvam AI, Krutrim, Haptik, Yellow.ai",
    "  └ Fractal Analytics, HighRadius, Gupshup",
    "  └ Custom cover letters + portfolio links",
    "  └ Cold emails to engineering teams",
]
for task in tasks_w25_26:
    story.append(Paragraph(task, task_style))

story.append(Paragraph("FINAL CHECKPOINT: Portfolio review", checkpoint_style))
final_check = [
    "✓ 3 deployed projects with public URLs",
    "✓ 5+ technical blog posts published",
    "✓ GitHub profile polished (100+ commits visible)",
    "✓ 20+ job applications sent with follow-ups",
    "✓ 5+ mock interviews completed",
]
for item in final_check:
    story.append(Paragraph(item, task_style))
story.append(PageBreak())

# PORTFOLIO REQUIREMENTS
story.append(Paragraph("PORTFOLIO REQUIREMENTS (NON-NEGOTIABLE)", phase_style))

portfolio_data = [
    ["PROJECT", "TECH STACK", "PROVES", "MUST HAVE"],
    ["Pathly v2\n(Flagship)", 
     "FastAPI, Flutter,\nSupabase, OpenRouter", 
     "Full-stack AI,\nRAG, Agents,\nProduction deploy",
     "5+ AI features,\nDemo video,\nBenchmarks,\n500+ test lines"],
    ["DocuMind\n(RAG Deep-Dive)",
     "FastAPI,\npgvector,\nsentence-transformers",
     "RAG expertise,\nVector DB,\nEmbedding optimization",
     "Jupyter walkthrough,\n3 retrieval strategies,\nCost analysis"],
    ["CodeReviewBot\n(Agent System)",
     "FastAPI,\nGitHub API,\nAsync workers",
     "Multi-step reasoning,\nTool integration,\nProduction agent",
     "GitHub App deployed,\n10+ example reviews,\nTechnical writeup"],
]

portfolio_table = Table(portfolio_data, colWidths=[1.3*inch, 1.5*inch, 1.7*inch, 1.5*inch])
portfolio_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e7d32')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 1), (-1, -1), 7),
]))
story.append(portfolio_table)
story.append(PageBreak())

# WEEKLY CHECKPOINT TEMPLATE
story.append(Paragraph("WEEKLY CHECKPOINT TEMPLATE", phase_style))
story.append(Paragraph("EVERY SUNDAY 8PM - MANDATORY REPORT", checkpoint_style))
story.append(Spacer(1, 0.1*inch))

checkpoint_template = """
<b>WEEK X CHECKPOINT:</b>

□ What did you deploy this week? (URL required)
  └ _________________________________

□ GitHub commits this week: _____ (min: 14, target: 21)

□ Teaching content created:
  └ Type: ☐ Video  ☐ Blog  ☐ Diagram  ☐ Tutorial
  └ Link: _________________________________

□ What broke and how did you fix it?
  └ _________________________________

□ Can you rebuild this week's work from memory in <4 hours?
  └ ☐ Yes (tested)  ☐ No (REPEAT WEEK)

□ Next week's build target (1 sentence):
  └ _________________________________

<b>FAILURE CONDITIONS:</b>
• GitHub commits <14 → REPEAT WEEK
• No deployment → REPEAT WEEK  
• Cannot rebuild → REPEAT WEEK
• No teaching content → REPEAT WEEK
"""
story.append(Paragraph(checkpoint_template, task_style))
story.append(PageBreak())

# CHATGPT USAGE GUIDE
story.append(Paragraph("HOW TO USE CHATGPT WITH THIS ROADMAP", phase_style))
story.append(Spacer(1, 0.1*inch))

chatgpt_guide = """
<b>DAILY WORKFLOW:</b>

1. <b>Morning (Start of coding session):</b>
   Prompt: "I'm on Day X of Week Y. Today's tasks are: [paste from PDF]. 
   Help me break down the first task into 30-minute chunks."

2. <b>During coding (when stuck):</b>
   Prompt: "I'm implementing [task]. Got this error: [paste error]. 
   Here's my code: [paste code]. What's wrong?"

3. <b>Code review (after implementing):</b>
   Prompt: "Review this code for best practices: [paste code]. 
   Focus on: performance, error handling, and FastAPI patterns."

4. <b>Concept clarification:</b>
   Prompt: "Explain [concept] like I need to teach it to a beginner. 
   Include: analogy, common mistakes, and how it applies to my RAG system."

5. <b>Testing help:</b>
   Prompt: "I built [feature]. What tests should I write? 
   Generate pytest test cases covering: happy path, edge cases, errors."

6. <b>Evening (daily review):</b>
   Prompt: "Here's what I built today: [describe]. 
   What should I focus on tomorrow to stay on track for Week X goals?"

<b>PROMPTS TO AVOID:</b>
✗ "Teach me everything about RAG" (too broad)
✗ "Build this for me" (no learning)
✗ "Is this good?" without context (vague)

<b>EFFECTIVE PROMPTS:</b>
✓ "Debug this specific error in my chunker.py"
✓ "Explain why my embeddings are slow (1000 chunks takes 2min)"
✓ "Review my error handling - am I catching the right exceptions?"
✓ "How do I test async database operations in pytest?"
"""
story.append(Paragraph(chatgpt_guide, task_style))
story.append(PageBreak())

# DEBUGGING FLOWCHART
story.append(Paragraph("DEBUGGING PROTOCOL (WHEN STUCK)", phase_style))

debug_steps = [
    ["STEP", "ACTION", "TIME LIMIT"],
    ["1. Read error", "Copy full traceback, identify line number", "5 min"],
    ["2. Google error", "Search exact error message", "10 min"],
    ["3. Check docs", "Read official docs for that function/library", "15 min"],
    ["4. Minimal repro", "Isolate problem in 10-line script", "20 min"],
    ["5. Ask ChatGPT", "Paste error + minimal code + what you tried", "15 min"],
    ["6. Discord/Forums", "Post on FastAPI/Python Discord with context", "30 min"],
    ["7. Rubber duck", "Explain problem out loud to yourself", "10 min"],
    ["8. Take break", "Walk away for 15 minutes", "15 min"],
    ["TOTAL", "If not solved in 2 hours → mark blocker, move to next task", "2 hrs"],
]

debug_table = Table(debug_steps, colWidths=[0.8*inch, 3.5*inch, 1.2*inch])
debug_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#d32f2f')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
]))
story.append(debug_table)
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph("<b>NEVER:</b> Spend >2 hours on one bug. Mark it, move on, ask mentor/senior dev.", checkpoint_style))
story.append(PageBreak())

# SUCCESS METRICS
story.append(Paragraph("SUCCESS METRICS BY MONTH", phase_style))

metrics_data = [
    ["MONTH", "GITHUB", "DEPLOYS", "BLOG POSTS", "TESTS", "MOCK INTERVIEWS"],
    ["Month 1\n(Wk 1-4)", "60+", "2", "1", "20+", "0"],
    ["Month 2\n(Wk 5-8)", "60+", "2", "1", "50+", "0"],
    ["Month 3\n(Wk 9-12)", "70+", "3", "2", "80+", "0"],
    ["Month 4\n(Wk 13-16)", "70+", "3", "2", "100+", "0"],
    ["Month 5\n(Wk 17-20)", "60+", "2", "2", "120+", "2"],
    ["Month 6\n(Wk 21-26)", "40+", "1", "3", "150+", "5"],
    ["TOTAL", "360+", "13", "11", "150+", "7+"],
]

metrics_table = Table(metrics_data, colWidths=[1*inch, 0.9*inch, 0.9*inch, 1*inch, 0.8*inch, 1.1*inch])
metrics_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976d2')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#2e7d32')),
    ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),
]))
story.append(metrics_table)
story.append(PageBreak())

# FINAL PAGE: IMMEDIATE NEXT STEPS
story.append(Paragraph("YOUR NEXT 48 HOURS (START NOW)", phase_style))
story.append(Spacer(1, 0.1*inch))

next_48 = """
<b>HOUR 0-2 (RIGHT NOW):</b>

□ Install dependencies:
  <font face="Courier" size=8>pip install supabase python-dotenv bcrypt</font>

□ Create files:
  <font face="Courier" size=8>
  cd ~/pathly-v2/backend
  mkdir -p app/core
  touch app/core/database.py
  touch .env
  </font>

□ Setup Supabase:
  • Go to supabase.com → Create project
  • Copy URL and anon key to .env
  • Test connection

□ First commit:
  <font face="Courier" size=8>git commit -m "feat: add Supabase client setup"</font>

<b>HOUR 2-4:</b>

□ Run SQL schema in Supabase dashboard:
  • Create users table
  • Create learning_paths table
  • Verify tables exist

□ Create app/models/user.py (Pydantic models)

□ Create app/repositories/user_repository.py (CRUD operations)

<b>HOUR 4-8 (TOMORROW):</b>

□ Update app/routes/users.py with database integration

□ Test endpoints:
  <font face="Courier" size=8>curl -X POST http://localhost:8000/users/ ...</font>

□ Verify user created in Supabase dashboard

□ Commit + push to GitHub

<b>HOUR 8-12:</b>

□ Add error handling middleware

□ Add logging system

□ Write first tests (pytest)

□ Commit + push

<b>HOUR 12-48 (NEXT 36 HOURS):</b>

□ Complete all Week 8 tasks from roadmap

□ Deploy to Railway/Render

□ Record teaching video

□ Sunday 8PM: Submit checkpoint report

<b>FAILURE = REPEAT WEEK 8</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>IMMEDIATE ACTION (NEXT 30 MINUTES):</b>

1. Close all other tabs
2. Open terminal
3. Run first command above
4. Do NOT watch tutorials
5. Build → Break → Fix → Learn

<b>THE CLOCK IS TICKING.</b>

<b>Target deadline: July 2026</b>
<b>Days remaining: ~150</b>
<b>Your competition is watching tutorials.</b>
<b>You will be building.</b>

<b>START NOW.</b>
"""
story.append(Paragraph(next_48, task_style))

# Build PDF
doc.build(story)
print(f"✅ PDF generated: {OUTPUT_FILE}")
print(f"📄 Total pages: ~{len(story) // 30}")  # Rough estimate
print("🚀 Ready to download!")
