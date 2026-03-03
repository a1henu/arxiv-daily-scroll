---
layout: default
title: Probabilistic Retrofitting of Learned Simulators
---

# Probabilistic Retrofitting of Learned Simulators
**arXiv**：[2603.01949v1](https://arxiv.org/abs/2603.01949) · [PDF](https://arxiv.org/pdf/2603.01949.pdf)  
**作者**：Cristiana Diaconu, Miles Cranmer, Richard E. Turner, Tanya Marwah, Payel Mukhopadhyay  

**一句话要点**：提出基于CRPS的确定性模型概率化改造方法，以高效建模混沌偏微分方程系统。

**关键词**：概率建模, 偏微分方程, 模型改造, 连续排名概率分数, 混沌系统, 训练效率

## 3 点简述
- 核心问题：确定性模型难以处理混沌物理系统的不确定性，从头训练概率模型成本高。
- 方法要点：通过连续排名概率分数（CRPS）对预训练确定性模型进行架构无关的改造。
- 实验或效果：在单系统和多系统上，CRPS降低20-54%，VRMSE提升达30%，训练成本低。

## 摘要（原文）

> Dominant approaches for modelling Partial Differential Equations (PDEs) rely on deterministic predictions, yet many physical systems of interest are inherently chaotic and uncertain. While training probabilistic models from scratch is possible, it is computationally expensive and fails to leverage the significant resources already invested in high-performing deterministic backbones. In this work, we adopt a training-efficient strategy to transform pre-trained deterministic models into probabilistic ones via retrofitting with a proper scoring rule: the Continuous Ranked Probability Score (CRPS). Crucially, this approach is architecture-agnostic: it applies the same adaptation mechanism across distinct model backbones with minimal code modifications. The method proves highly effective across different scales of pre-training: for models trained on single dynamical systems, we achieve 20-54% reductions in rollout CRPS and up to 30% improvements in variance-normalised RMSE (VRMSE) relative to compute-matched deterministic fine-tuning. We further validate our approach on a PDE foundation model, trained on multiple systems and retrofitted on the dataset of interest, to show that our probabilistic adaptation yields an improvement of up to 40% in CRPS and up to 15% in VRMSE compared to deterministic fine-tuning. Validated across diverse architectures and dynamics, our results show that probabilistic PDE modelling need not require retraining from scratch, but can be unlocked from existing deterministic backbones with modest additional training cost.

