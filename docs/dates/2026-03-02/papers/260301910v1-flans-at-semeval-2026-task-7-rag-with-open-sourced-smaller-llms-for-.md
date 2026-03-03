---
layout: default
title: FLANS at SemEval-2026 Task 7: RAG with Open-Sourced Smaller LLMs for Everyday Knowledge Across Diverse Languages and Cultures
---

# FLANS at SemEval-2026 Task 7: RAG with Open-Sourced Smaller LLMs for Everyday Knowledge Across Diverse Languages and Cultures
**arXiv**：[2603.01910v1](https://arxiv.org/abs/2603.01910) · [PDF](https://arxiv.org/pdf/2603.01910.pdf)  
**作者**：Liliia Bogdanova, Shiran Sun, Lifeng Han, Natalia Amat Lefort, Flor Miriam Plaza-del-Arco  

**一句话要点**：提出基于开源小语言模型的检索增强生成方法，用于多语言文化日常知识问答任务

**关键词**：检索增强生成, 开源小语言模型, 文化感知知识库, 多语言问答, 日常知识理解

## 3 点简述
- 核心问题：解决多语言文化背景下的日常知识问答，涉及英语、西班牙语和中文
- 方法要点：构建文化感知知识库，结合本地提取和在线搜索，使用开源小语言模型进行检索增强生成
- 实验或效果：参与SemEval-2025任务7的两个子任务，分享提示词优化和资源代码

## 摘要（原文）

> This system paper describes our participation in the SemEval-2025 Task-7 ``Everyday Knowledge Across Diverse Languages and Cultures''. We attended two subtasks, i.e., Track 1: Short Answer Questions (SAQ), and Track 2: Multiple-Choice Questions (MCQ). The methods we used are retrieval augmented generation (RAGs) with open-sourced smaller LLMs (OS-sLLMs). To better adapt to this shared task, we created our own culturally aware knowledge base (CulKBs) by extracting Wikipedia content using keyword lists we prepared. We extracted both culturally-aware wiki-text and country-specific wiki-summary. In addition to the local CulKBs, we also have one system integrating live online search output via DuckDuckGo. Towards better privacy and sustainability, we aimed to deploy smaller LLMs (sLLMs) that are open-sourced on the Ollama platform. We share the prompts we developed using refinement techniques and report the learning curve of such prompts. The tested languages are English, Spanish, and Chinese for both tracks. Our resources and codes are shared via https://github.com/aaronlifenghan/FLANS-2026

