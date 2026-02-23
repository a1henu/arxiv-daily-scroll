---
layout: default
title: Aurora: Neuro-Symbolic AI Driven Advising Agent
---

# Aurora: Neuro-Symbolic AI Driven Advising Agent
**arXiv**：[2602.17999v1](https://arxiv.org/abs/2602.17999) · [PDF](https://arxiv.org/pdf/2602.17999.pdf)  
**作者**：Lorena Amanda Quincoso Lugones, Christopher Kverne, Nityam Sharadkumar Bhimani, Ana Carolina Oliveira, Agoritsa Polyzou, Christine Lisetti, Janki Bhimani  

**一句话要点**：提出Aurora神经符号AI咨询代理，以解决高等教育学术咨询资源不足问题

**关键词**：神经符号AI, 学术咨询代理, 检索增强生成, 符号推理, 规范化数据库, 可扩展AI

## 3 点简述
- 高等教育学术咨询面临师生比过高（如300:1）导致的指导延迟和不公平问题
- Aurora结合检索增强生成、符号推理和规范化课程数据库，提供合规且可验证的建议
- 在多样化评估中，Aurora将语义对齐从0.68提升至0.93，平均延迟0.71秒，比原始LLM快83倍

## 摘要（原文）

> Academic advising in higher education is under severe strain, with advisor-to-student ratios commonly exceeding 300:1. These structural bottlenecks limit timely access to guidance, increase the risk of delayed graduation, and contribute to inequities in student support. We introduce Aurora, a modular neuro-symbolic advising agent that unifies retrieval-augmented generation (RAG), symbolic reasoning, and normalized curricular databases to deliver policy-compliant, verifiable recommendations at scale. Aurora integrates three components: (i) a Boyce-Codd Normal Form (BCNF) catalog schema for consistent program rules, (ii) a Prolog engine for prerequisite and credit enforcement, and (iii) an instruction-tuned large language model for natural-language explanations of its recommendations. To assess performance, we design a structured evaluation suite spanning common and edge-case advising scenarios, including short-term scheduling, long-term roadmapping, skill-aligned pathways, and out-of-scope requests. Across this diverse set, Aurora improves semantic alignment with expert-crafted answers from 0.68 (Raw LLM baseline) to 0.93 (+36%), achieves perfect precision and recall in nearly half of in-scope cases, and consistently produces correct fallbacks for unanswerable prompts. On commodity hardware, Aurora delivers sub-second mean latency (0.71s across 20 queries), approximately 83X faster than a Raw LLM baseline (59.2s). By combining symbolic rigor with neural fluency, Aurora advances a paradigm for accurate, explainable, and scalable AI-driven advising.

