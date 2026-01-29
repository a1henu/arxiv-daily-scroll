---
layout: default
title: MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization
---

# MeCo: Enhancing LLM-Empowered Multi-Robot Collaboration via Similar Task Memoization
**arXiv**：[2601.20577v1](https://arxiv.org/abs/2601.20577) · [PDF](https://arxiv.org/pdf/2601.20577.pdf)  
**作者**：Baiqing Wang, Helei Cui, Bo Zhang, Xiaolong Zheng, Bin Guo, Zhiwen Yu  

**一句话要点**：提出MeCo框架，通过相似任务记忆化提升多机器人协作效率

**关键词**：多机器人协作, 大型语言模型, 任务记忆化, 相似性测试, 规划优化

## 3 点简述
- 现有LLM赋能方法在相似任务中需重复规划，效率低下
- MeCo引入相似性测试方法，检索并复用历史任务解决方案
- 实验显示MeCo显著降低规划成本并提高成功率

## 摘要（原文）

> Multi-robot systems have been widely deployed in real-world applications, providing significant improvements in efficiency and reductions in labor costs. However, most existing multi-robot collaboration methods rely on extensive task-specific training, which limits their adaptability to new or diverse scenarios. Recent research leverages the language understanding and reasoning capabilities of large language models (LLMs) to enable more flexible collaboration without specialized training. Yet, current LLM-empowered approaches remain inefficient: when confronted with identical or similar tasks, they must replan from scratch because they omit task-level similarities. To address this limitation, we propose MeCo, a similarity-aware multi-robot collaboration framework that applies the principle of ``cache and reuse'' (a.k.a., memoization) to reduce redundant computation. Unlike simple task repetition, identifying and reusing solutions for similar but not identical tasks is far more challenging, particularly in multi-robot settings. To this end, MeCo introduces a new similarity testing method that retrieves previously solved tasks with high relevance, enabling effective plan reuse without re-invoking LLMs. Furthermore, we present MeCoBench, the first benchmark designed to evaluate performance on similar-task collaboration scenarios. Experimental results show that MeCo substantially reduces planning costs and improves success rates compared with state-of-the-art approaches.

