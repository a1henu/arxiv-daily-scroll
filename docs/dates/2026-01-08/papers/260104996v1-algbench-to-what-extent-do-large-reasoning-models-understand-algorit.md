---
layout: default
title: AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?
---

# AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?
**arXiv**：[2601.04996v1](https://arxiv.org/abs/2601.04996) · [PDF](https://arxiv.org/pdf/2601.04996.pdf)  
**作者**：Henan Sun, Kaichi Yu, Yuyao Wang, Bowen Liu, Xunkai Li, Rong-Hua Li, Nuo Chen, Jia Li  

**一句话要点**：提出AlgBench基准以评估大型推理模型在算法理解上的真实能力

**关键词**：算法推理基准, 大型推理模型评估, 算法中心范式, 动态编程, 战略过移, 专家策划问题集

## 3 点简述
- 核心问题：现有基准无法评估大型推理模型是否真正掌握算法推理
- 方法要点：构建专家策划的算法中心基准，涵盖27种算法和3000多个问题
- 实验或效果：模型在非优化任务表现良好，但在全局优化算法上准确率显著下降

## 摘要（原文）

> Reasoning ability has become a central focus in the advancement of Large Reasoning Models (LRMs). Although notable progress has been achieved on several reasoning benchmarks such as MATH500 and LiveCodeBench, existing benchmarks for algorithmic reasoning remain limited, failing to answer a critical question: Do LRMs truly master algorithmic reasoning? To answer this question, we propose AlgBench, an expert-curated benchmark that evaluates LRMs under an algorithm-centric paradigm.
>   AlgBench consists of over 3,000 original problems spanning 27 algorithms, constructed by ACM algorithmic experts and organized under a comprehensive taxonomy, including Euclidean-structured, non-Euclidean-structured, non-optimized, local-optimized, global-optimized, and heuristic-optimized categories. Empirical evaluations on leading LRMs (e.g., Gemini-3-Pro, DeepSeek-v3.2-Speciale and GPT-o3) reveal substantial performance heterogeneity: while models perform well on non-optimized tasks (up to 92%), accuracy drops sharply to around 49% on globally optimized algorithms such as dynamic programming. Further analysis uncovers \textbf{strategic over-shifts}, wherein models prematurely abandon correct algorithmic designs due to necessary low-entropy tokens. These findings expose fundamental limitations of problem-centric reinforcement learning and highlight the necessity of an algorithm-centric training paradigm for robust algorithmic reasoning.

