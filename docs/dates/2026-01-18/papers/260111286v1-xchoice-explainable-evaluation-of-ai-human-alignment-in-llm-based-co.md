---
layout: default
title: XChoice: Explainable Evaluation of AI-Human Alignment in LLM-based Constrained Choice Decision Making
---

# XChoice: Explainable Evaluation of AI-Human Alignment in LLM-based Constrained Choice Decision Making
**arXiv**：[2601.11286v1](https://arxiv.org/abs/2601.11286) · [PDF](https://arxiv.org/pdf/2601.11286.pdf)  
**作者**：Weihong Qi, Fan Huang, Rasika Muralidharan, Jisun An, Haewoon Kwak  

**一句话要点**：提出XChoice框架，基于机制模型评估LLM在约束决策中与人类的对齐性

**关键词**：AI-人类对齐, 约束决策, 可解释评估, 机制建模, LLM评估

## 3 点简述
- 核心问题：超越准确率等表面指标，评估AI与人类在约束决策中的深层对齐性
- 方法要点：拟合机制决策模型，恢复可解释参数如因素重要性、约束敏感性和权衡
- 实验或效果：以美国时间使用调查为基准，揭示模型间和群体间的异质对齐与错位

## 摘要（原文）

> We present XChoice, an explainable framework for evaluating AI-human alignment in constrained decision making. Moving beyond outcome agreement such as accuracy and F1 score, XChoice fits a mechanism-based decision model to human data and LLM-generated decisions, recovering interpretable parameters that capture the relative importance of decision factors, constraint sensitivity, and implied trade-offs. Alignment is assessed by comparing these parameter vectors across models, options, and subgroups. We demonstrate XChoice on Americans' daily time allocation using the American Time Use Survey (ATUS) as human ground truth, revealing heterogeneous alignment across models and activities and salient misalignment concentrated in Black and married groups. We further validate robustness of XChoice via an invariance analysis and evaluate targeted mitigation with a retrieval augmented generation (RAG) intervention. Overall, XChoice provides mechanism-based metrics that diagnose misalignment and support informed improvements beyond surface outcome matching.

