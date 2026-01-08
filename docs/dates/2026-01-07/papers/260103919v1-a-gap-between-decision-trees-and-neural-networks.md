---
layout: default
title: A Gap Between Decision Trees and Neural Networks
---

# A Gap Between Decision Trees and Neural Networks
**arXiv**：[2601.03919v1](https://arxiv.org/abs/2601.03919) · [PDF](https://arxiv.org/pdf/2601.03919.pdf)  
**作者**：Akash Kumar  

**一句话要点**：分析决策树与浅层神经网络在几何复杂度上的差距，提出平滑屏障分数以平衡分类准确性与解释性。

**关键词**：决策树, 浅层神经网络, Radon总变差, 几何复杂度, 分类校准, 解释性机器学习

## 3 点简述
- 研究决策树与浅层ReLU网络在决策边界几何复杂度上的冲突，使用Radon总变差半范作为度量工具。
- 证明决策树指示函数及其常见平滑替代具有无限Radon总变差，而构造的平滑屏障分数具有有限Radon总变差并能精确恢复决策区域。
- 在合成矩形数据集上实验，展示准确性与复杂度之间的权衡，以及阈值选择对训练结果的影响。

## 摘要（原文）

> We study when geometric simplicity of decision boundaries, used here as a notion of interpretability, can conflict with accurate approximation of axis-aligned decision trees by shallow neural networks. Decision trees induce rule-based, axis-aligned decision regions (finite unions of boxes), whereas shallow ReLU networks are typically trained as score models whose predictions are obtained by thresholding. We analyze the infinite-width, bounded-norm, single-hidden-layer ReLU class through the Radon total variation ($\mathrm{R}\mathrm{TV}$) seminorm, which controls the geometric complexity of level sets.
>   We first show that the hard tree indicator $1_A$ has infinite $\mathrm{R}\mathrm{TV}$. Moreover, two natural split-wise continuous surrogates--piecewise-linear ramp smoothing and sigmoidal (logistic) smoothing--also have infinite $\mathrm{R}\mathrm{TV}$ in dimensions $d>1$, while Gaussian convolution yields finite $\mathrm{R}\mathrm{TV}$ but with an explicit exponential dependence on $d$.
>   We then separate two goals that are often conflated: classification after thresholding (recovering the decision set) versus score learning (learning a calibrated score close to $1_A$). For classification, we construct a smooth barrier score $S_A$ with finite $\mathrm{R}\mathrm{TV}$ whose fixed threshold $τ=1$ exactly recovers the box. Under a mild tube-mass condition near $\partial A$, we prove an $L_1(P)$ calibration bound that decays polynomially in a sharpness parameter, along with an explicit $\mathrm{R}\mathrm{TV}$ upper bound in terms of face measures. Experiments on synthetic unions of rectangles illustrate the resulting accuracy--complexity tradeoff and how threshold selection shifts where training lands along it.

