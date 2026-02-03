---
layout: default
title: Towards AI Evaluation in Domain-Specific RAG Systems: The AgriHubi Case Study
---

# Towards AI Evaluation in Domain-Specific RAG Systems: The AgriHubi Case Study
**arXiv**：[2602.02208v1](https://arxiv.org/abs/2602.02208) · [PDF](https://arxiv.org/pdf/2602.02208.pdf)  
**作者**：Md. Toufique Hasan, Ayman Asad Khan, Mika Saari, Vaishnavi Bankhele, Pekka Abrahamsson  

**一句话要点**：提出AgriHubi系统以解决芬兰语农业决策支持中RAG系统的领域适应与评估问题。

**关键词**：检索增强生成, 领域适应, 低资源语言, 农业决策支持, 用户反馈迭代

## 3 点简述
- 核心问题：大语言模型在农业领域应用受限，包括弱基础、英语中心数据和低资源语言访问困难。
- 方法要点：集成芬兰农业文档与PORO模型，结合显式源基础和用户反馈进行迭代优化。
- 实验或效果：通过八次迭代和用户研究，系统在答案完整性、语言准确性和可靠性方面有显著提升。

## 摘要（原文）

> Large language models show promise for knowledge-intensive domains, yet their use in agriculture is constrained by weak grounding, English-centric training data, and limited real-world evaluation. These issues are amplified for low-resource languages, where high-quality domain documentation exists but remains difficult to access through general-purpose models. This paper presents AgriHubi, a domain-adapted retrieval-augmented generation (RAG) system for Finnish-language agricultural decision support. AgriHubi integrates Finnish agricultural documents with open PORO family models and combines explicit source grounding with user feedback to support iterative refinement. Developed over eight iterations and evaluated through two user studies, the system shows clear gains in answer completeness, linguistic accuracy, and perceived reliability. The results also reveal practical trade-offs between response quality and latency when deploying larger models. This study provides empirical guidance for designing and evaluating domain-specific RAG systems in low-resource language settings.

