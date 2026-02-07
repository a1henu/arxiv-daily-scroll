---
layout: default
title: Anchored Policy Optimization: Mitigating Exploration Collapse Via Support-Constrained Rectification
---

# Anchored Policy Optimization: Mitigating Exploration Collapse Via Support-Constrained Rectification
**arXiv**：[2602.05717v1](https://arxiv.org/abs/2602.05717) · [PDF](https://arxiv.org/pdf/2602.05717.pdf)  
**作者**：Tianyi Wang, Long Li, Hongcan Guo, Yibiao Chen, Yixia Li, Yong Wang, Yun Chen, Guanhua Chen  

**一句话要点**：提出锚定策略优化以解决强化学习中探索崩溃问题，通过支持约束校正实现高效学习。

**关键词**：强化学习, 策略优化, 探索崩溃, 支持约束, 梯度对齐, 弹性恢复

## 3 点简述
- 核心问题：强化学习验证奖励中递归空间收缩导致探索崩溃，KL正则化引发梯度冲突。
- 方法要点：从全局形状匹配转向支持覆盖，定义安全流形允许激进锐化并选择性恢复。
- 实验或效果：在数学基准上打破准确率-多样性权衡，显著提升Pass@1并恢复多样性。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) is increasingly viewed as a tree pruning mechanism. However, we identify a systemic pathology termed Recursive Space Contraction (RSC), an irreversible collapse driven by the combined dynamics of positive sharpening and negative squeezing, where the sampling probability of valid alternatives vanishes. While Kullback-Leibler (KL) regularization aims to mitigate this, it imposes a rigid Shape Matching constraint that forces the policy to mimic the reference model's full density, creating a gradient conflict with the sharpening required for correctness. We propose Anchored Policy Optimization (APO), shifting the paradigm from global Shape Matching to Support Coverage. By defining a Safe Manifold based on the reference model's high-confidence support, APO permits aggressive sharpening for efficiency while selectively invoking a restorative force during error correction to prevent collapse. We theoretically derive that APO serves as a gradient-aligned mechanism to maximize support coverage, enabling an Elastic Recovery that re-inflates valid branches. Empirical evaluations on mathematical benchmarks demonstrate that APO breaks the accuracy-diversity trade-off, significantly improving Pass@1 while restoring the Pass@K diversity typically lost by standard policy gradient methods.

