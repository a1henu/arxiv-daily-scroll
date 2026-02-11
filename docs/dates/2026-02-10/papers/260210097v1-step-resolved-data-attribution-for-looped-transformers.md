---
layout: default
title: Step-resolved data attribution for looped transformers
---

# Step-resolved data attribution for looped transformers
**arXiv**：[2602.10097v1](https://arxiv.org/abs/2602.10097) · [PDF](https://arxiv.org/pdf/2602.10097.pdf)  
**作者**：Georgios Kaissis, David Mildenberger, Juan Felipe Gomez, Martin J. Menten, Eleni Triantafillou  

**一句话要点**：提出步分解影响方法以分析循环Transformer训练数据在推理步骤中的影响

**关键词**：循环Transformer, 数据归因, 可解释性, 训练影响分析, TensorSketch, 算法推理

## 3 点简述
- 研究循环Transformer中训练数据如何影响内部计算，现有方法聚合所有循环步骤，掩盖具体影响时机
- 引入步分解影响方法，通过展开循环计算图，将影响分解为各步骤轨迹，实现细粒度归因
- 提出TensorSketch实现，避免存储每样本梯度，实验验证方法可扩展、误差低，支持数据归因和可解释性任务

## 摘要（原文）

> We study how individual training examples shape the internal computation of looped transformers, where a shared block is applied for $τ$ recurrent iterations to enable latent reasoning. Existing training-data influence estimators such as TracIn yield a single scalar score that aggregates over all loop iterations, obscuring when during the recurrent computation a training example matters. We introduce \textit{Step-Decomposed Influence (SDI)}, which decomposes TracIn into a length-$τ$ influence trajectory by unrolling the recurrent computation graph and attributing influence to specific loop iterations. To make SDI practical at transformer scale, we propose a TensorSketch implementation that never materialises per-example gradients. Experiments on looped GPT-style models and algorithmic reasoning tasks show that SDI scales excellently, matches full-gradient baselines with low error and supports a broad range of data attribution and interpretability tasks with per-step insights into the latent reasoning process.

