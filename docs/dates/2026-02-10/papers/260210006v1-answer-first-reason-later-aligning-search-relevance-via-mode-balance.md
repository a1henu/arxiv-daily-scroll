---
layout: default
title: Answer First, Reason Later: Aligning Search Relevance via Mode-Balanced Reinforcement Learning
---

# Answer First, Reason Later: Aligning Search Relevance via Mode-Balanced Reinforcement Learning
**arXiv**：[2602.10006v1](https://arxiv.org/abs/2602.10006) · [PDF](https://arxiv.org/pdf/2602.10006.pdf)  
**作者**：Shijie Zhang, Xiang Guo, Rujun Guo, Shaoyu Liu, Xiaozhao Wang, Guanjun Jiang, Kevin Zhang  

**一句话要点**：提出AFRL范式与模式平衡优化，以解决搜索相关性任务中低延迟与高性能的平衡问题。

**关键词**：搜索相关性, 强化学习, 模式平衡优化, 知识蒸馏, 低延迟推理

## 3 点简述
- 核心问题：搜索相关性模型需在低延迟与高性能间取得平衡，现有RL训练易导致模式崩溃。
- 方法要点：采用AFRL范式，结合SFT与RL，引入模式平衡优化策略以平衡KL散度。
- 实验或效果：32B教师模型达到SOTA性能，并通过蒸馏将知识迁移至0.6B模型，实现推理深度与部署延迟的调和。

## 摘要（原文）

> Building a search relevance model that achieves both low latency and high performance is a long-standing challenge in the search industry. To satisfy the millisecond-level response requirements of online systems while retaining the interpretable reasoning traces of Large Language Models (LLMs), we propose a novel \textbf{Answer-First, Reason Later (AFRL)} paradigm. This paradigm requires the model to output the definitive relevance score in the very first token, followed by a structured logical explanation. Inspired by the success of reasoning models, we adopt a "Supervised Fine-Tuning (SFT) + Reinforcement Learning (RL)" pipeline to achieve AFRL. However, directly applying existing RL training often leads to \textbf{mode collapse} in the search relevance task, where the model forgets complex long-tail rules in pursuit of high rewards. From an information theory perspective: RL inherently minimizes the \textbf{Reverse KL divergence}, which tends to seek probability peaks (mode-seeking) and is prone to "reward hacking." On the other hand, SFT minimizes the \textbf{Forward KL divergence}, forcing the model to cover the data distribution (mode-covering) and effectively anchoring expert rules. Based on this insight, we propose a \textbf{Mode-Balanced Optimization} strategy, incorporating an SFT auxiliary loss into Stepwise-GRPO training to balance these two properties. Furthermore, we construct an automated instruction evolution system and a multi-stage curriculum to ensure expert-level data quality. Extensive experiments demonstrate that our 32B teacher model achieves state-of-the-art performance. Moreover, the AFRL architecture enables efficient knowledge distillation, successfully transferring expert-level logic to a 0.6B model, thereby reconciling reasoning depth with deployment latency.

