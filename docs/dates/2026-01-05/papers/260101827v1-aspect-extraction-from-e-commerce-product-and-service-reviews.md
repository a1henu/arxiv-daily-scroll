---
layout: default
title: Aspect Extraction from E-Commerce Product and Service Reviews
---

# Aspect Extraction from E-Commerce Product and Service Reviews
**arXiv**：[2601.01827v1](https://arxiv.org/abs/2601.01827) · [PDF](https://arxiv.org/pdf/2601.01827.pdf)  
**作者**：Valiant Lance D. Dionela, Fatima Kriselle S. Dy, Robin James M. Hombrebueno, Aaron Rae M. Nicolas, Charibeth K. Cheng, Raphael W. Gonda  

**一句话要点**：提出面向Taglish电商评论的混合方法框架，以解决低资源代码混合环境中的方面提取难题

**关键词**：方面提取, 代码混合语言处理, 分层方面框架, 大语言模型应用, 电商评论分析, 低资源自然语言处理

## 3 点简述
- 核心问题：Taglish（他加禄语-英语混合）电商评论的方面提取在低资源场景中具有挑战性
- 方法要点：结合规则方法、大语言模型和微调技术，开发分层方面框架和双模式标注方案
- 实验效果：生成式大语言模型在隐式方面处理上表现最佳（Macro F1 0.91），微调模型受数据集不平衡限制

## 摘要（原文）

> Aspect Extraction (AE) is a key task in Aspect-Based Sentiment Analysis (ABSA), yet it remains difficult to apply in low-resource and code-switched contexts like Taglish, a mix of Tagalog and English commonly used in Filipino e-commerce reviews. This paper introduces a comprehensive AE pipeline designed for Taglish, combining rule-based, large language model (LLM)-based, and fine-tuning techniques to address both aspect identification and extraction. A Hierarchical Aspect Framework (HAF) is developed through multi-method topic modeling, along with a dual-mode tagging scheme for explicit and implicit aspects. For aspect identification, four distinct models are evaluated: a Rule-Based system, a Generative LLM (Gemini 2.0 Flash), and two Fine-Tuned Gemma-3 1B models trained on different datasets (Rule-Based vs. LLM-Annotated). Results indicate that the Generative LLM achieved the highest performance across all tasks (Macro F1 0.91), demonstrating superior capability in handling implicit aspects. In contrast, the fine-tuned models exhibited limited performance due to dataset imbalance and architectural capacity constraints. This work contributes a scalable and linguistically adaptive framework for enhancing ABSA in diverse, code-switched environments.

