---
layout: default
title: Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning
---

# Data-Centric Interpretability for LLM-based Multi-Agent Reinforcement Learning
**arXiv**：[2602.05183v1](https://arxiv.org/abs/2602.05183) · [PDF](https://arxiv.org/pdf/2602.05183.pdf)  
**作者**：John Yan, Michael Yu, Yuqi Sun, Alexander Duffy, Tyler Marques, Matthew Lyle Olson  

**一句话要点**：提出Meta-Autointerp方法，结合稀疏自编码器和LLM摘要器，分析多智能体强化学习中LLM行为动态。

**关键词**：多智能体强化学习, 稀疏自编码器, LLM解释性, 数据中心分析, 训练动态, Meta-Autointerp

## 3 点简述
- 核心问题：LLM在多智能体强化学习训练中行为变化难以理解，需数据中心的解释性方法。
- 方法要点：应用预训练稀疏自编码器和LLM摘要器，开发Meta-Autointerp分组特征为可解释假设。
- 实验或效果：发现细粒度行为如角色扮演和奖励黑客，验证90%元特征显著，系统提示增强提升分数14.2%。

## 摘要（原文）

> Large language models (LLMs) are increasingly trained in complex Reinforcement Learning, multi-agent environments, making it difficult to understand how behavior changes over training. Sparse Autoencoders (SAEs) have recently shown to be useful for data-centric interpretability. In this work, we analyze large-scale reinforcement learning training runs from the sophisticated environment of Full-Press Diplomacy by applying pretrained SAEs, alongside LLM-summarizer methods. We introduce Meta-Autointerp, a method for grouping SAE features into interpretable hypotheses about training dynamics. We discover fine-grained behaviors including role-playing patterns, degenerate outputs, language switching, alongside high-level strategic behaviors and environment-specific bugs. Through automated evaluation, we validate that 90% of discovered SAE Meta-Features are significant, and find a surprising reward hacking behavior. However, through two user studies, we find that even subjectively interesting and seemingly helpful SAE features may be worse than useless to humans, along with most LLM generated hypotheses. However, a subset of SAE-derived hypotheses are predictively useful for downstream tasks. We further provide validation by augmenting an untrained agent's system prompt, improving the score by +14.2%. Overall, we show that SAEs and LLM-summarizer provide complementary views into agent behavior, and together our framework forms a practical starting point for future data-centric interpretability work on ensuring trustworthy LLM behavior throughout training.

