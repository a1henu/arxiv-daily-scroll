---
layout: default
title: The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety
---

# The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety
**arXiv**：[2602.15799v1](https://arxiv.org/abs/2602.15799) · [PDF](https://arxiv.org/pdf/2602.15799.pdf)  
**作者**：Max Springer, Chung Peng Lee, Blossom Metevier, Jane Castleman, Bohdan Turbal, Hayoung Jung, Zeyu Shen, Aleksandra Korolova  

**一句话要点**：揭示微调导致安全对齐崩溃的几何机制，提出对齐不稳定性条件与四次方缩放定律。

**关键词**：语言模型对齐, 微调安全, 几何分析, 梯度下降, 对齐崩溃, 缩放定律

## 3 点简述
- 核心问题：微调对齐语言模型时，即使使用良性数据，安全护栏也会不可预测地退化。
- 方法要点：通过几何分析证明对齐集中在低维子空间，梯度下降的二阶加速会驱动轨迹进入对齐敏感区域。
- 实验或效果：建立对齐不稳定性条件，推导出对齐损失随训练时间四次方增长的缩放定律。

## 摘要（原文）

> Fine-tuning aligned language models on benign tasks unpredictably degrades safety guardrails, even when training data contains no harmful content and developers have no adversarial intent. We show that the prevailing explanation, that fine-tuning updates should be orthogonal to safety-critical directions in high-dimensional parameter space, offers false reassurance: we show this orthogonality is structurally unstable and collapses under the dynamics of gradient descent. We then resolve this through a novel geometric analysis, proving that alignment concentrates in low-dimensional subspaces with sharp curvature, creating a brittle structure that first-order methods cannot detect or defend. While initial fine-tuning updates may indeed avoid these subspaces, the curvature of the fine-tuning loss generates second-order acceleration that systematically steers trajectories into alignment-sensitive regions. We formalize this mechanism through the Alignment Instability Condition, three geometric properties that, when jointly satisfied, lead to safety degradation. Our main result establishes a quartic scaling law: alignment loss grows with the fourth power of training time, governed by the sharpness of alignment geometry and the strength of curvature coupling between the fine-tuning task and safety-critical parameters. These results expose a structural blind spot in the current safety paradigm. The dominant approaches to safe fine-tuning address only the initial snapshot of a fundamentally dynamic problem. Alignment fragility is not a bug to be patched; it is an intrinsic geometric property of gradient descent on curved manifolds. Our results motivate the development of curvature-aware methods, and we hope will further enable a shift in alignment safety analysis from reactive red-teaming to predictive diagnostics for open-weight model deployment.

