---
layout: default
title: Learning Continuous Wasserstein Barycenter Space for Generalized All-in-One Image Restoration
---

# Learning Continuous Wasserstein Barycenter Space for Generalized All-in-One Image Restoration
**arXiv**：[2602.23169v1](https://arxiv.org/abs/2602.23169) · [PDF](https://arxiv.org/pdf/2602.23169.pdf)  
**作者**：Xiaole Tang, Xiaoyi He, Jiayi Xu, Xiang Gu, Jian Sun  

**一句话要点**：提出BaryIR框架，通过Wasserstein重心空间对齐多源退化特征以提升全合一图像修复的泛化能力。

**关键词**：全合一图像修复, Wasserstein重心, 特征解耦, 泛化学习, 退化无关表示

## 3 点简述
- 现有全合一图像修复方法对分布外退化泛化不足，限制实际应用。
- BaryIR利用Wasserstein重心空间建模退化无关分布，并引入正交残差子空间解耦退化无关与退化特定知识。
- 实验显示BaryIR在未见退化和真实混合退化场景中表现优异，泛化性强。

## 摘要（原文）

> Despite substantial advances in all-in-one image restoration for addressing diverse degradations within a unified model, existing methods remain vulnerable to out-of-distribution degradations, thereby limiting their generalization in real-world scenarios. To tackle the challenge, this work is motivated by the intuition that multisource degraded feature distributions are induced by different degradation-specific shifts from an underlying degradation-agnostic distribution, and recovering such a shared distribution is thus crucial for achieving generalization across degradations. With this insight, we propose BaryIR, a representation learning framework that aligns multisource degraded features in the Wasserstein barycenter (WB) space, which models a degradation-agnostic distribution by minimizing the average of Wasserstein distances to multisource degraded distributions. We further introduce residual subspaces, whose embeddings are mutually contrasted while remaining orthogonal to the WB embeddings. Consequently, BaryIR explicitly decouples two orthogonal spaces: a WB space that encodes the degradation-agnostic invariant contents shared across degradations, and residual subspaces that adaptively preserve the degradation-specific knowledge. This disentanglement mitigates overfitting to in-distribution degradations and enables adaptive restoration grounded on the degradation-agnostic shared invariance. Extensive experiments demonstrate that BaryIR performs competitively against state-of-the-art all-in-one methods. Notably, BaryIR generalizes well to unseen degradations (\textit{e.g.,} types and levels) and shows remarkable robustness in learning generalized features, even when trained on limited degradation types and evaluated on real-world data with mixed degradations.

