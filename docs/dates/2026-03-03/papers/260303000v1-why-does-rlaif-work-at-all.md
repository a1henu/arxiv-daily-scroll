---
layout: default
title: Why Does RLAIF Work At All?
---

# Why Does RLAIF Work At All?
**arXiv**：[2603.03000v1](https://arxiv.org/abs/2603.03000) · [PDF](https://arxiv.org/pdf/2603.03000.pdf)  
**作者**：Robin Young  

**一句话要点**：提出潜在价值假说以解释RLAIF在价值学习中的有效性

**关键词**：强化学习从AI反馈, 潜在价值假说, 表示空间, 宪法提示, 价值对齐, 模型容量

## 3 点简述
- 核心问题：RLAIF为何能通过AI反馈实现自我改进，缺乏理论解释
- 方法要点：假设预训练编码人类价值为表示空间方向，宪法提示激活潜在价值
- 实验或效果：分析表明RLAIF改善对齐，质量上限取决于表示编码价值的能力

## 摘要（原文）

> Reinforcement Learning from AI Feedback (RLAIF) enables language models to improve by training on their own preference judgments, yet no theoretical account explains why this self-improvement seemingly works for value learning. We propose the latent value hypothesis, that pretraining on internet-scale data encodes human values as directions in representation space, and constitutional prompts elicit these latent values into preference judgments. We formalize this intuition under a linear model where the constitution acts as a projection operator selecting value-relevant directions. Our analysis yields several results. RLAIF improves alignment when the constitution-activated direction correlates with true values better than the model's default generation direction thus explaining the generation-judgment gap; the ceiling on RLAIF quality is determined by how well representations encode values, which scales with model capacity; and adversarial constitutions exist that can activate anti-social value directions encoded from harmful pretraining data. Our account unifies scattered empirical findings including the refusal direction, low-rank safety subspaces, and RLAIF scaling behavior.

