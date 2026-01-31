---
layout: default
title: Cross-Fusion Distance: A Novel Metric for Measuring Fusion and Separability Between Data Groups in Representation Space
---

# Cross-Fusion Distance: A Novel Metric for Measuring Fusion and Separability Between Data Groups in Representation Space
**arXiv**：[2601.22036v1](https://arxiv.org/abs/2601.22036) · [PDF](https://arxiv.org/pdf/2601.22036.pdf)  
**作者**：Xiaolong Zhang, Jianwei Zhang, Xubo Song  

**一句话要点**：提出交叉融合距离以量化表示空间中数据组间的融合与可分性，适用于域偏移场景。

**关键词**：表示学习, 域偏移, 距离度量, 融合可分性, 几何位移, 泛化评估

## 3 点简述
- 核心问题：现有分布距离度量混淆融合改变与保留因素，无法准确反映数据组间的真实融合程度。
- 方法要点：设计交叉融合距离，隔离融合改变的几何位移，对全局缩放等保留因素保持鲁棒，计算复杂度线性。
- 实验或效果：理论验证不变性与敏感性，合成实验可控验证，真实数据集上比常用方法更贴近下游泛化退化。

## 摘要（原文）

> Quantifying degrees of fusion and separability between data groups in representation space is a fundamental problem in representation learning, particularly under domain shift. A meaningful metric should capture fusion-altering factors like geometric displacement between representation groups, whose variations change the extent of fusion, while remaining invariant to fusion-preserving factors such as global scaling and sampling-induced layout changes, whose variations do not. Existing distributional distance metrics conflate these factors, leading to measures that are not informative of the true extent of fusion between data groups. We introduce Cross-Fusion Distance (CFD), a principled measure that isolates fusion-altering geometry while remaining robust to fusion-preserving variations, with linear computational complexity. We characterize the invariance and sensitivity properties of CFD theoretically and validate them in controlled synthetic experiments. For practical utility on real-world datasets with domain shift, CFD aligns more closely with downstream generalization degradation than commonly used alternatives. Overall, CFD provides a theoretically grounded and interpretable distance measure for representation learning.

