---
layout: default
title: CURVE: Learning Causality-Inspired Invariant Representations for Robust Scene Understanding via Uncertainty-Guided Regularization
---

# CURVE: Learning Causality-Inspired Invariant Representations for Robust Scene Understanding via Uncertainty-Guided Regularization
**arXiv**：[2601.20355v1](https://arxiv.org/abs/2601.20355) · [PDF](https://arxiv.org/pdf/2601.20355.pdf)  
**作者**：Yue Liang, Jiatong Du, Ziyi Yang, Yanjun Huang, Hong Chen  

**一句话要点**：提出CURVE框架，通过不确定性引导正则化学习因果不变表示，以提升场景图在分布偏移下的鲁棒性。

**关键词**：场景图理解, 因果不变表示, 不确定性建模, 分布外泛化, 结构正则化

## 3 点简述
- 场景图常因虚假相关而过拟合，阻碍分布外泛化。
- CURVE结合变分不确定性建模与正则化，抑制环境特定关系，解耦不变交互动态。
- 在零样本迁移和低数据模拟到真实适应中验证，能学习域稳定稀疏拓扑并提供可靠不确定性估计。

## 摘要（原文）

> Scene graphs provide structured abstractions for scene understanding, yet they often overfit to spurious correlations, severely hindering out-of-distribution generalization. To address this limitation, we propose CURVE, a causality-inspired framework that integrates variational uncertainty modeling with uncertainty-guided structural regularization to suppress high-variance, environment-specific relations. Specifically, we apply prototype-conditioned debiasing to disentangle invariant interaction dynamics from environment-dependent variations, promoting a sparse and domain-stable topology. Empirically, we evaluate CURVE in zero-shot transfer and low-data sim-to-real adaptation, verifying its ability to learn domain-stable sparse topologies and provide reliable uncertainty estimates to support risk prediction under distribution shifts.

