---
layout: default
title: An Agentic AI System for Multi-Framework Communication Coding
---

# An Agentic AI System for Multi-Framework Communication Coding
**arXiv**：[2512.08659v1](https://arxiv.org/abs/2512.08659) · [PDF](https://arxiv.org/pdf/2512.08659.pdf)  
**作者**：Bohao Yang, Rui Yang, Joshua M. Biro, Haoyuan Wang, Jessica L. Handley, Brianna Richardson, Sophia Bessias, Nicoleta Economou-Zavlanos, Armando D. Bedoya, Monica Agrawal, Michael M. Zavlanos, Anand Chowdhury, Raj M. Ratwani, Kai Sun, Kathryn I. Pollak, Michael J. Pencina, Chuan Hong  

**一句话要点**：提出基于多智能体架构的MOSAIC系统，用于临床沟通编码以解决标注可扩展性问题。

**关键词**：临床沟通编码, 多智能体系统, 检索增强生成, 动态少样本提示, LangGraph架构

## 3 点简述
- 核心问题：临床沟通标注依赖人工，存在劳动密集、不一致和难以扩展的挑战。
- 方法要点：采用LangGraph架构协调四个核心智能体，结合检索增强生成和动态少样本提示进行编码。
- 实验或效果：在风湿病和妇产科领域测试，整体F1分数达0.928，优于基准方法。

## 摘要（原文）

> Clinical communication is central to patient outcomes, yet large-scale human annotation of patient-provider conversation remains labor-intensive, inconsistent, and difficult to scale. Existing approaches based on large language models typically rely on single-task models that lack adaptability, interpretability, and reliability, especially when applied across various communication frameworks and clinical domains. In this study, we developed a Multi-framework Structured Agentic AI system for Clinical Communication (MOSAIC), built on a LangGraph-based architecture that orchestrates four core agents, including a Plan Agent for codebook selection and workflow planning, an Update Agent for maintaining up-to-date retrieval databases, a set of Annotation Agents that applies codebook-guided retrieval-augmented generation (RAG) with dynamic few-shot prompting, and a Verification Agent that provides consistency checks and feedback. To evaluate performance, we compared MOSAIC outputs against gold-standard annotations created by trained human coders. We developed and evaluated MOSAIC using 26 gold standard annotated transcripts for training and 50 transcripts for testing, spanning rheumatology and OB/GYN domains. On the test set, MOSAIC achieved an overall F1 score of 0.928. Performance was highest in the Rheumatology subset (F1 = 0.962) and strongest for Patient Behavior (e.g., patients asking questions, expressing preferences, or showing assertiveness). Ablations revealed that MOSAIC outperforms baseline benchmarking.

