---
layout: default
title: Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?
---

# Securing the AI Supply Chain: What Can We Learn From Developer-Reported Security Issues and Solutions of AI Projects?
**arXiv**：[2512.23385v1](https://arxiv.org/abs/2512.23385) · [PDF](https://arxiv.org/pdf/2512.23385.pdf)  
**作者**：The Anh Nguyen, Triet Huynh Minh Le, M. Ali Babar  

**一句话要点**：基于开发者报告构建AI供应链安全分类法，揭示模型与数据安全挑战

**关键词**：AI供应链安全, 安全分类法, 开发者报告分析, distilBERT分类器, 模型安全, 数据安全

## 3 点简述
- 核心问题：AI供应链安全威胁复杂，缺乏实际安全问题和解决方案的系统知识
- 方法要点：结合关键词匹配与优化distilBERT分类器，从Hugging Face和GitHub收集312,868条安全讨论
- 实验或效果：主题分析753个样本，提出32个安全问题和24个解决方案的细粒度分类法

## 摘要（原文）

> The rapid growth of Artificial Intelligence (AI) models and applications has led to an increasingly complex security landscape. Developers of AI projects must contend not only with traditional software supply chain issues but also with novel, AI-specific security threats. However, little is known about what security issues are commonly encountered and how they are resolved in practice. This gap hinders the development of effective security measures for each component of the AI supply chain. We bridge this gap by conducting an empirical investigation of developer-reported issues and solutions, based on discussions from Hugging Face and GitHub. To identify security-related discussions, we develop a pipeline that combines keyword matching with an optimal fine-tuned distilBERT classifier, which achieved the best performance in our extensive comparison of various deep learning and large language models. This pipeline produces a dataset of 312,868 security discussions, providing insights into the security reporting practices of AI applications and projects. We conduct a thematic analysis of 753 posts sampled from our dataset and uncover a fine-grained taxonomy of 32 security issues and 24 solutions across four themes: (1) System and Software, (2) External Tools and Ecosystem, (3) Model, and (4) Data. We reveal that many security issues arise from the complex dependencies and black-box nature of AI components. Notably, challenges related to Models and Data often lack concrete solutions. Our insights can offer evidence-based guidance for developers and researchers to address real-world security threats across the AI supply chain.

