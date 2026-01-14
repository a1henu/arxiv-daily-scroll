---
layout: default
title: Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge
---

# Multiplex Thinking: Reasoning via Token-wise Branch-and-Merge
**arXiv**：[2601.08808v1](https://arxiv.org/abs/2601.08808) · [PDF](https://arxiv.org/pdf/2601.08808.pdf)  
**作者**：Yao Tang, Li Dong, Yaru Hao, Qingxiu Dong, Furu Wei, Jiatao Gu  

**一句话要点**：提出Multiplex Thinking，通过软推理机制提升大语言模型在复杂推理任务中的效率和性能。

**关键词**：软推理机制, 多路令牌聚合, 强化学习优化, 数学推理基准, 序列长度压缩, 自适应推理

## 3 点简述
- 核心问题：大语言模型使用Chain-of-Thought推理时序列长、带宽低，而人类推理更灵活。
- 方法要点：在每个推理步采样K个候选词，聚合为单个连续多路令牌，保持词汇先验和采样动态。
- 实验或效果：在数学推理基准上优于离散CoT和强化学习基线，序列更短，性能从Pass@1到Pass@1024一致提升。

## 摘要（原文）

> Large language models often solve complex reasoning tasks more effectively with Chain-of-Thought (CoT), but at the cost of long, low-bandwidth token sequences. Humans, by contrast, often reason softly by maintaining a distribution over plausible next steps. Motivated by this, we propose Multiplex Thinking, a stochastic soft reasoning mechanism that, at each thinking step, samples K candidate tokens and aggregates their embeddings into a single continuous multiplex token. This preserves the vocabulary embedding prior and the sampling dynamics of standard discrete generation, while inducing a tractable probability distribution over multiplex rollouts. Consequently, multiplex trajectories can be directly optimized with on-policy reinforcement learning (RL). Importantly, Multiplex Thinking is self-adaptive: when the model is confident, the multiplex token is nearly discrete and behaves like standard CoT; when it is uncertain, it compactly represents multiple plausible next steps without increasing sequence length. Across challenging math reasoning benchmarks, Multiplex Thinking consistently outperforms strong discrete CoT and RL baselines from Pass@1 through Pass@1024, while producing shorter sequences. The code and checkpoints are available at https://github.com/GMLR-Penn/Multiplex-Thinking.

