---
layout: default
title: When More Experts Hurt: Underfitting in Multi-Expert Learning to Defer
---

# When More Experts Hurt: Underfitting in Multi-Expert Learning to Defer
**arXiv**：[2602.17144v1](https://arxiv.org/abs/2602.17144) · [PDF](https://arxiv.org/pdf/2602.17144.pdf)  
**作者**：Shuqi Liu, Yuzhou Cao, Lei Feng, Bo An, Luke Ong  

**一句话要点**：提出PiCCE方法以解决多专家学习延迟中的固有欠拟合问题

**关键词**：学习延迟, 多专家系统, 欠拟合, 专家可识别性, 代理方法, 分类器性能

## 3 点简述
- 多专家学习延迟中，分类器因专家可识别性问题导致固有欠拟合，性能下降
- PiCCE通过经验证据自适应识别可靠专家，将多专家问题简化为类单专家学习
- 理论证明一致性，实验验证在多种设置下提升性能，包括真实专家场景

## 摘要（原文）

> Learning to Defer (L2D) enables a classifier to abstain from predictions and defer to an expert, and has recently been extended to multi-expert settings. In this work, we show that multi-expert L2D is fundamentally more challenging than the single-expert case. With multiple experts, the classifier's underfitting becomes inherent, which seriously degrades prediction performance, whereas in the single-expert setting it arises only under specific conditions. We theoretically reveal that this stems from an intrinsic expert identifiability issue: learning which expert to trust from a diverse pool, a problem absent in the single-expert case and renders existing underfitting remedies failed. To tackle this issue, we propose PiCCE (Pick the Confident and Correct Expert), a surrogate-based method that adaptively identifies a reliable expert based on empirical evidence. PiCCE effectively reduces multi-expert L2D to a single-expert-like learning problem, thereby resolving multi expert underfitting. We further prove its statistical consistency and ability to recover class probabilities and expert accuracies. Extensive experiments across diverse settings, including real-world expert scenarios, validate our theoretical results and demonstrate improved performance.

