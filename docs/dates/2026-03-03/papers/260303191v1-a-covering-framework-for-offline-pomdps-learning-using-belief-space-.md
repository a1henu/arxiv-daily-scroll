---
layout: default
title: A Covering Framework for Offline POMDPs Learning using Belief Space Metric
---

# A Covering Framework for Offline POMDPs Learning using Belief Space Metric
**arXiv**：[2603.03191v1](https://arxiv.org/abs/2603.03191) · [PDF](https://arxiv.org/pdf/2603.03191.pdf)  
**作者**：Youheng Zhu, Yiping Lu  

**一句话要点**：提出基于信念空间度量的覆盖分析框架，以缓解离线POMDP评估中的指数爆炸问题。

**关键词**：离线策略评估, 部分可观测马尔可夫决策过程, 信念空间度量, 覆盖分析, 误差界, 样本效率

## 3 点简述
- 核心问题：离线POMDP评估中，隐状态推断加剧了现有方法的视野和记忆诅咒。
- 方法要点：利用信念空间的度量结构，假设值函数Lipschitz连续，推导更紧的误差界。
- 实验或效果：应用于双采样Bellman误差最小化和基于记忆的未来依赖值函数，提升样本效率。

## 摘要（原文）

> In off policy evaluation (OPE) for partially observable Markov decision processes (POMDPs), an agent must infer hidden states from past observations, which exacerbates both the curse of horizon and the curse of memory in existing OPE methods. This paper introduces a novel covering analysis framework that exploits the intrinsic metric structure of the belief space (distributions over latent states) to relax traditional coverage assumptions. By assuming value relevant functions are Lipschitz continuous in the belief space, we derive error bounds that mitigate exponential blow ups in horizon and memory length. Our unified analysis technique applies to a broad class of OPE algorithms, yielding concrete error bounds and coverage requirements expressed in terms of belief space metrics rather than raw history coverage. We illustrate the improved sample efficiency of this framework via case studies: the double sampling Bellman error minimization algorithm, and the memory based future dependent value functions (FDVF). In both cases, our coverage definition based on the belief space metric yields tighter bounds.

