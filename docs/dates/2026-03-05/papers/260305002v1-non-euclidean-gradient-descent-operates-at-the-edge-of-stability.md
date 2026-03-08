---
layout: default
title: Non-Euclidean Gradient Descent Operates at the Edge of Stability
---

# Non-Euclidean Gradient Descent Operates at the Edge of Stability
**arXiv**：[2603.05002v1](https://arxiv.org/abs/2603.05002) · [PDF](https://arxiv.org/pdf/2603.05002.pdf)  
**作者**：Rustem Islamov, Michael Crawshaw, Jeremy Cohen, Robert Gower  

**一句话要点**：提出非欧几里得梯度下降的广义锐度框架，解释稳定性边缘现象并统一多种优化器分析。

**关键词**：稳定性边缘, 非欧几里得梯度下降, 广义锐度, 方向平滑性, 优化器统一分析, 神经网络训练

## 3 点简述
- 核心问题：稳定性边缘现象在深度学习中广泛存在，但理论基础不完整，需扩展至非欧几里得范数。
- 方法要点：基于方向平滑性定义广义锐度，涵盖vanilla GD、预处理GD、ℓ∞-下降等优化器。
- 实验或效果：在神经网络上验证非欧几里得GD也呈现锐度渐进和阈值振荡，提供几何感知谱度量。

## 摘要（原文）

> The Edge of Stability (EoS) is a phenomenon where the sharpness (largest eigenvalue) of the Hessian converges to $2/η$ during training with gradient descent (GD) with a step-size $η$. Despite (apparently) violating classical smoothness assumptions, EoS has been widely observed in deep learning, but its theoretical foundations remain incomplete. We provide an interpretation of EoS through the lens of Directional Smoothness Mishkin et al. [2024]. This interpretation naturally extends to non-Euclidean norms, which we use to define generalized sharpness under an arbitrary norm. Our generalized sharpness measure includes previously studied vanilla GD and preconditioned GD as special cases, as well as methods for which EoS has not been studied, such as $\ell_{\infty}$-descent, Block CD, Spectral GD, and Muon without momentum. Through experiments on neural networks, we show that non-Euclidean GD with our generalized sharpness also exhibits progressive sharpening followed by oscillations around or above the threshold $2/η$. Practically, our framework provides a single, geometry-aware spectral measure that works across optimizers.

