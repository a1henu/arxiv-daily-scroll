---
layout: default
title: Agentic Multi-Persona Framework for Evidence-Aware Fake News Detection
---

# Agentic Multi-Persona Framework for Evidence-Aware Fake News Detection
**arXiv**：[2512.21039v1](https://arxiv.org/abs/2512.21039) · [PDF](https://arxiv.org/pdf/2512.21039.pdf)  
**作者**：Roopa Bukke, Soumya Pandey, Suraj Kumar, Soumi Chattopadhyay, Chandranath Adak  

**一句话要点**：提出AMPEND-LS框架，通过多模态证据融合与LLM-SLM协同解决假新闻检测问题。

**关键词**：假新闻检测, 多模态融合, LLM-SLM协同, 证据增强, 可解释性, 鲁棒性

## 3 点简述
- 核心问题：在线虚假信息快速传播，现有方法在多模态内容处理、领域泛化和可解释性方面存在不足。
- 方法要点：结合文本、视觉和上下文信号，利用LLM进行结构化推理，并引入反向图像搜索、知识图谱路径和说服策略分析。
- 实验或效果：在三个基准数据集上，AMPEND-LS在准确性、F1分数和鲁棒性方面优于现有方法，并通过定性案例展示其透明推理能力。

## 摘要（原文）

> The rapid proliferation of online misinformation poses significant risks to public trust, policy, and safety, necessitating reliable automated fake news detection. Existing methods often struggle with multimodal content, domain generalization, and explainability. We propose AMPEND-LS, an agentic multi-persona evidence-grounded framework with LLM-SLM synergy for multimodal fake news detection. AMPEND-LS integrates textual, visual, and contextual signals through a structured reasoning pipeline powered by LLMs, augmented with reverse image search, knowledge graph paths, and persuasion strategy analysis. To improve reliability, we introduce a credibility fusion mechanism combining semantic similarity, domain trustworthiness, and temporal context, and a complementary SLM classifier to mitigate LLM uncertainty and hallucinations. Extensive experiments across three benchmark datasets demonstrate that AMPEND-LS consistently outperformed state-of-the-art baselines in accuracy, F1 score, and robustness. Qualitative case studies further highlight its transparent reasoning and resilience against evolving misinformation. This work advances the development of adaptive, explainable, and evidence-aware systems for safeguarding online information integrity.

