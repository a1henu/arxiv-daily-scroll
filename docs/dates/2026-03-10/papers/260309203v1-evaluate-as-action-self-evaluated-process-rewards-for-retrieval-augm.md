---
layout: default
title: Evaluate-as-Action: Self-Evaluated Process Rewards for Retrieval-Augmented Agents
---

# Evaluate-as-Action: Self-Evaluated Process Rewards for Retrieval-Augmented Agents
**arXiv**：[2603.09203v1](https://arxiv.org/abs/2603.09203) · [PDF](https://arxiv.org/pdf/2603.09203.pdf)  
**作者**：Jiangming Shu, Yuxiang Zhang, Ye Ma, Xueyuan Lin, Jitao Sang  

**一句话要点**：提出EvalAct方法，将检索质量评估转化为显式动作，以提升检索增强代理在多步推理中的可靠性。

**关键词**：检索增强代理, 多步推理, 过程奖励, 强化学习优化, 开放域问答

## 3 点简述
- 核心问题：检索增强代理在多步推理中因噪声检索和粗粒度奖励信号而可靠性受限。
- 方法要点：引入显式评估动作和Search-to-Evaluate协议，结合PCAR优化方法校准过程奖励。
- 实验或效果：在七个开放域QA基准上实现最佳平均准确率，多跳任务提升显著。

## 摘要（原文）

> Retrieval-augmented agents can query external evidence, yet their reliability in multi-step reasoning remains limited: noisy retrieval may derail multi-hop question answering, while outcome-only reinforcement learning provides credit signals that are too coarse to optimize intermediate steps. We propose \textsc{EvalAct} (Evaluate-as-Action), which converts implicit retrieval quality assessment into an explicit action and enforces a coupled Search-to-Evaluate protocol so that each retrieval is immediately followed by a structured evaluation score, yielding process signals aligned with the interaction trajectory. To leverage these signals, we introduce Process-Calibrated Advantage Rescaling (PCAR), a GRPO-based optimization method that rescales advantages at the segment level according to evaluation scores, emphasizing reliable segments while updating uncertain ones conservatively. Experiments on seven open-domain QA benchmarks show that \textsc{EvalAct} achieves the best average accuracy, with the largest gains on multi-hop tasks, and ablations verify that the explicit evaluation loop drives the primary improvements while PCAR provides consistent additional benefits.

