---
layout: default
title: OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents
---

# OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents
**arXiv**：[2601.13722v1](https://arxiv.org/abs/2601.13722) · [PDF](https://arxiv.org/pdf/2601.13722.pdf)  
**作者**：Yulin Hu, Zimo Long, Jiahe Guo, Xingyu Sui, Xing Fu, Weixiang Zhao, Yanyan Zhao, Bing Qin  

**一句话要点**：提出OP-Bench基准和Self-ReCheck机制以解决记忆增强对话系统中的过度个性化问题

**关键词**：记忆增强对话系统, 过度个性化, 基准评测, 记忆过滤, 长时对话历史, 模型无关方法

## 3 点简述
- 核心问题：记忆增强对话系统存在过度个性化，导致响应不相关、重复或谄媚
- 方法要点：将过度个性化形式化为三类，并构建包含1700个实例的OP-Bench基准
- 实验或效果：评估显示过度个性化普遍，Self-ReCheck能缓解问题并保持个性化性能

## 摘要（原文）

> Memory-augmented conversational agents enable personalized interactions using long-term user memory and have gained substantial traction. However, existing benchmarks primarily focus on whether agents can recall and apply user information, while overlooking whether such personalization is used appropriately. In fact, agents may overuse personal information, producing responses that feel forced, intrusive, or socially inappropriate to users. We refer to this issue as \emph{over-personalization}. In this work, we formalize over-personalization into three types: Irrelevance, Repetition, and Sycophancy, and introduce \textbf{OP-Bench} a benchmark of 1,700 verified instances constructed from long-horizon dialogue histories. Using \textbf{OP-Bench}, we evaluate multiple large language models and memory-augmentation methods, and find that over-personalization is widespread when memory is introduced. Further analysis reveals that agents tend to retrieve and over-attend to user memories even when unnecessary. To address this issue, we propose \textbf{Self-ReCheck}, a lightweight, model-agnostic memory filtering mechanism that mitigates over-personalization while preserving personalization performance. Our work takes an initial step toward more controllable and appropriate personalization in memory-augmented dialogue systems.

