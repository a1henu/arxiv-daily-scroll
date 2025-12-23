---
layout: default
title: DFORD: Directional Feedback based Online Ordinal Regression Learning
---

# DFORD: Directional Feedback based Online Ordinal Regression Learning
**arXiv**：[2512.19550v1](https://arxiv.org/abs/2512.19550) · [PDF](https://arxiv.org/pdf/2512.19550.pdf)  
**作者**：Naresh Manwani, M Elamparithy, Tanish Taneja  

**一句话要点**：提出基于方向反馈的在线序数回归算法，以弱监督方式学习序数标签排序。

**关键词**：序数回归, 在线学习, 弱监督学习, 方向反馈, 核方法, 探索-利用策略

## 3 点简述
- 核心问题：在序数回归中，学习者仅接收预测标签相对于真实标签方向的弱反馈，而非完整标签信息。
- 方法要点：设计在线算法，结合探索-利用策略高效学习，并引入核变体以处理非线性模型，使用截断技巧优化内存效率。
- 实验或效果：在合成和真实数据集上，算法性能与完整信息方法相当或更优，预期遗憾为对数级。

## 摘要（原文）

> In this paper, we introduce directional feedback in the ordinal regression setting, in which the learner receives feedback on whether the predicted label is on the left or the right side of the actual label. This is a weak supervision setting for ordinal regression compared to the full information setting, where the learner can access the labels. We propose an online algorithm for ordinal regression using directional feedback. The proposed algorithm uses an exploration-exploitation scheme to learn from directional feedback efficiently. Furthermore, we introduce its kernel-based variant to learn non-linear ordinal regression models in an online setting. We use a truncation trick to make the kernel implementation more memory efficient. The proposed algorithm maintains the ordering of the thresholds in the expected sense. Moreover, it achieves the expected regret of $\mathcal{O}(\log T)$. We compare our approach with a full information and a weakly supervised algorithm for ordinal regression on synthetic and real-world datasets. The proposed approach, which learns using directional feedback, performs comparably (sometimes better) to its full information counterpart.

