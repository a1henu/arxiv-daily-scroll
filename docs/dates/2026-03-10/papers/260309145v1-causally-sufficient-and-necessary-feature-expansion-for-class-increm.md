---
layout: default
title: Causally Sufficient and Necessary Feature Expansion for Class-Incremental Learning
---

# Causally Sufficient and Necessary Feature Expansion for Class-Incremental Learning
**arXiv**：[2603.09145v1](https://arxiv.org/abs/2603.09145) · [PDF](https://arxiv.org/pdf/2603.09145.pdf)  
**作者**：Zhen Zhang, Jielei Chu, Tianrui Li  

**一句话要点**：提出基于概率必要充分性的正则化方法，以解决类增量学习中特征碰撞问题。

**关键词**：类增量学习, 因果推理, 特征扩展, 反事实生成, 正则化方法

## 3 点简述
- 核心问题：扩展方法中任务特定特征与旧特征碰撞，源于任务内和任务间的伪相关。
- 方法要点：定义CPNS量化因果完整性，使用双范围反事实生成器最小化PNS风险。
- 实验或效果：理论分析可靠，正则化即插即用，实验验证有效性。

## 摘要（原文）

> Current expansion-based methods for Class Incremental Learning (CIL) effectively mitigate catastrophic forgetting by freezing old features. However, such task-specific features learned from the new task may collide with the old features. From a causal perspective, spurious feature correlations are the main cause of this collision, manifesting in two scopes: (i) guided by empirical risk minimization (ERM), intra-task spurious correlations cause task-specific features to rely on shortcut features. These non-robust features are vulnerable to interference, inevitably drifting into the feature space of other tasks; (ii) inter-task spurious correlations induce semantic confusion between visually similar classes across tasks. To address this, we propose a Probability of Necessity and Sufficiency (PNS)-based regularization method to guide feature expansion in CIL. Specifically, we first extend the definition of PNS to expansion-based CIL, termed CPNS, which quantifies both the causal completeness of intra-task representations and the separability of inter-task representations. We then introduce a dual-scope counterfactual generator based on twin networks to ensure the measurement of CPNS, which simultaneously generates: (i) intra-task counterfactual features to minimize intra-task PNS risk and ensure causal completeness of task-specific features, and (ii) inter-task interfering features to minimize inter-task PNS risk, ensuring the separability of inter-task representations. Theoretical analyses confirm its reliability. The regularization is a plug-and-play method for expansion-based CIL to mitigate feature collision. Extensive experiments demonstrate the effectiveness of the proposed method.

