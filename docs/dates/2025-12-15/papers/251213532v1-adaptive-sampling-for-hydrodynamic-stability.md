---
layout: default
title: Adaptive Sampling for Hydrodynamic Stability
---

# Adaptive Sampling for Hydrodynamic Stability
**arXiv**：[2512.13532v1](https://arxiv.org/abs/2512.13532) · [PDF](https://arxiv.org/pdf/2512.13532.pdf)  
**作者**：Anshima Singh, David J. Silvester  

**一句话要点**：提出自适应采样方法以高效检测参数化流体流动中的分岔边界

**关键词**：自适应采样, 流体稳定性分析, 分岔边界检测, 深度生成模型, 概率密度估计, 机器学习应用

## 3 点简述
- 核心问题：参数化流体流动中分岔边界检测的计算成本高，需高效采样策略。
- 方法要点：结合分类网络和概率密度估计（KRnet），通过熵引导自适应采样，形成反馈驱动学习过程。
- 实验或效果：从均匀分布出发，显著减少Navier-Stokes模拟次数，实现准确分岔边界识别，支持高维稳定性分析。

## 摘要（原文）

> An adaptive sampling approach for efficient detection of bifurcation boundaries in parametrized fluid flow problems is presented herein. The study extends the machine-learning approach of Silvester (Machine Learning for Hydrodynamic Stability, arXiv:2407.09572), where a classifier network was trained on preselected simulation data to identify bifurcated and nonbifurcated flow regimes. In contrast, the proposed methodology introduces adaptivity through a flow-based deep generative model that automatically refines the sampling of the parameter space. The strategy has two components: a classifier network maps the flow parameters to a bifurcation probability, and a probability density estimation technique (KRnet) for the generation of new samples at each adaptive step. The classifier output provides a probabilistic measure of flow stability, and the Shannon entropy of these predictions is employed as an uncertainty indicator. KRnet is trained to approximate a probability density function that concentrates sampling in regions of high entropy, thereby directing computational effort towards the evolving bifurcation boundary. This coupling between classification and generative modeling establishes a feedback-driven adaptive learning process analogous to error-indicator based refinement in contemporary partial differential equation solution strategies. Starting from a uniform parameter distribution, the new approach achieves accurate bifurcation boundary identification with significantly fewer Navier--Stokes simulations, providing a scalable foundation for high-dimensional stability analysis.

