---
layout: default
title: Optimal Transport Group Counterfactual Explanations
---

# Optimal Transport Group Counterfactual Explanations
**arXiv**：[2601.20692v1](https://arxiv.org/abs/2601.20692) · [PDF](https://arxiv.org/pdf/2601.20692.pdf)  
**作者**：Enrique Valero-Leal, Bernd Bischl, Pedro Larrañaga, Concha Bielza, Giuseppe Casalicchio  

**一句话要点**：提出基于最优传输的群体反事实解释方法，以解决现有方法泛化性差、假设强和几何失真问题。

**关键词**：群体反事实解释, 最优传输, 可解释人工智能, 泛化学习, 几何失真控制

## 3 点简述
- 现有群体反事实解释方法存在泛化性不足、依赖强模型假设或几何控制不佳的问题。
- 本方法学习显式最优传输映射，最小化群体总传输成本，实现无需重新优化的泛化解释。
- 实验表明，该方法能准确泛化、保持群体几何结构，并在线性或非线性模型中优于基线。

## 摘要（原文）

> Group counterfactual explanations find a set of counterfactual instances to explain a group of input instances contrastively. However, existing methods either (i) optimize counterfactuals only for a fixed group and do not generalize to new group members, (ii) strictly rely on strong model assumptions (e.g., linearity) for tractability or/and (iii) poorly control the counterfactual group geometry distortion. We instead learn an explicit optimal transport map that sends any group instance to its counterfactual without re-optimization, minimizing the group's total transport cost. This enables generalization with fewer parameters, making it easier to interpret the common actionable recourse. For linear classifiers, we prove that functions representing group counterfactuals are derived via mathematical optimization, identifying the underlying convex optimization type (QP, QCQP, ...). Experiments show that they accurately generalize, preserve group geometry and incur only negligible additional transport cost compared to baseline methods. If model linearity cannot be exploited, our approach also significantly outperforms the baselines.

