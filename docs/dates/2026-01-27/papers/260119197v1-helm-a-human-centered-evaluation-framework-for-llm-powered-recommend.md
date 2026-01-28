---
layout: default
title: HELM: A Human-Centered Evaluation Framework for LLM-Powered Recommender Systems
---

# HELM: A Human-Centered Evaluation Framework for LLM-Powered Recommender Systems
**arXiv**：[2601.19197v1](https://arxiv.org/abs/2601.19197) · [PDF](https://arxiv.org/pdf/2601.19197.pdf)  
**作者**：Sushant Mehta  

**一句话要点**：提出HELM框架以评估LLM推荐系统的人本质量维度

**关键词**：推荐系统评估, 大语言模型, 人本计算, 解释质量, 公平性分析

## 3 点简述
- 问题：现有评估方法侧重传统准确度，忽略影响用户体验的人本质量维度。
- 方法：构建HELM框架，系统评估意图对齐、解释质量、交互自然度、信任透明度、公平多样性五个维度。
- 实验：在三个领域测试三种LLM推荐器，专家评估显示HELM揭示传统指标未覆盖的关键质量差异。

## 摘要（原文）

> The integration of Large Language Models (LLMs) into recommendation systems has introduced unprecedented capabilities for natural language understanding, explanation generation, and conversational interactions. However, existing evaluation methodologies focus predominantly on traditional accuracy metrics, failing to capture the multifaceted human-centered qualities that determine the real-world user experience. We introduce \framework{} (\textbf{H}uman-centered \textbf{E}valuation for \textbf{L}LM-powered reco\textbf{M}menders), a comprehensive evaluation framework that systematically assesses LLM-powered recommender systems across five human-centered dimensions: \textit{Intent Alignment}, \textit{Explanation Quality}, \textit{Interaction Naturalness}, \textit{Trust \& Transparency}, and \textit{Fairness \& Diversity}. Through extensive experiments involving three state-of-the-art LLM-based recommenders (GPT-4, LLaMA-3.1, and P5) across three domains (movies, books, and restaurants), and rigorous evaluation by 12 domain experts using 847 recommendation scenarios, we demonstrate that \framework{} reveals critical quality dimensions invisible to traditional metrics. Our results show that while GPT-4 achieves superior explanation quality (4.21/5.0) and interaction naturalness (4.35/5.0), it exhibits a significant popularity bias (Gini coefficient 0.73) compared to traditional collaborative filtering (0.58). We release \framework{} as an open-source toolkit to advance human-centered evaluation practices in the recommender systems community.

