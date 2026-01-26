---
layout: default
title: Sycophancy Hides Linearly in the Attention Heads
---

# Sycophancy Hides Linearly in the Attention Heads
**arXiv**：[2601.16644v1](https://arxiv.org/abs/2601.16644) · [PDF](https://arxiv.org/pdf/2601.16644.pdf)  
**作者**：Rifo Genadi, Munachiso Nwadike, Nurdaulet Mukhituly, Hilal Alquabeh, Tatsuya Hiraoka, Kentaro Inui  

**一句话要点**：发现谄媚信号在注意力头中线性可分，通过线性探针实现针对性干预以缓解谄媚行为。

**关键词**：线性可分性, 注意力头, 线性探针, 谄媚缓解, 事实问答, 模型可解释性

## 3 点简述
- 核心问题：分析大语言模型中正确到错误谄媚信号的线性可分性及其在模型内部的分布。
- 方法要点：基于线性表示假设，在残差流、MLP和注意力层训练线性探针，识别信号最可分的稀疏注意力头子集。
- 实验或效果：在TruthfulQA上训练的探针可迁移至其他事实QA基准，干预有效减少谄媚，与已有“真实”方向重叠有限。

## 摘要（原文）

> We find that correct-to-incorrect sycophancy signals are most linearly separable within multi-head attention activations. Motivated by the linear representation hypothesis, we train linear probes across the residual stream, multilayer perceptron (MLP), and attention layers to analyze where these signals emerge. Although separability appears in the residual stream and MLPs, steering using these probes is most effective in a sparse subset of middle-layer attention heads. Using TruthfulQA as the base dataset, we find that probes trained on it transfer effectively to other factual QA benchmarks. Furthermore, comparing our discovered direction to previously identified "truthful" directions reveals limited overlap, suggesting that factual accuracy, and deference resistance, arise from related but distinct mechanisms. Attention-pattern analysis further indicates that the influential heads attend disproportionately to expressions of user doubt, contributing to sycophantic shifts. Overall, these findings suggest that sycophancy can be mitigated through simple, targeted linear interventions that exploit the internal geometry of attention activations.

