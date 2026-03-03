---
layout: default
title: On the Rate of Convergence of GD in Non-linear Neural Networks: An Adversarial Robustness Perspective
---

# On the Rate of Convergence of GD in Non-linear Neural Networks: An Adversarial Robustness Perspective
**arXiv**：[2603.02095v1](https://arxiv.org/abs/2603.02095) · [PDF](https://arxiv.org/pdf/2603.02095.pdf)  
**作者**：Guy Smorodinsky, Sveta Gimpleson, Itay Safran  

**一句话要点**：证明GD在最小二神经元ReLU网络中收敛至最优鲁棒性边界的速率极慢，为Θ(1/ln(t))。

**关键词**：梯度下降收敛, 非线性神经网络, 鲁棒性分析, 二分类, ReLU网络, 理论保证

## 3 点简述
- 研究GD在二分类任务中，针对两神经元ReLU网络和两个训练实例的收敛动力学。
- 通过严格分析GD轨迹和激活模式，推导出鲁棒性边界收敛速率的显式下界。
- 实证模拟显示该慢收敛现象在多种自然初始化下普遍存在，速率紧密匹配理论界。

## 摘要（原文）

> We study the convergence dynamics of Gradient Descent (GD) in a minimal binary classification setting, consisting of a two-neuron ReLU network and two training instances. We prove that even under these strong simplifying assumptions, while GD successfully converges to an optimal robustness margin, effectively maximizing the distance between the decision boundary and the training points, this convergence occurs at a prohibitively slow rate, scaling strictly as $Θ(1/\ln(t))$. To the best of our knowledge, this establishes the first explicit lower bound on the convergence rate of the robustness margin in a non-linear model. Through empirical simulations, we further demonstrate that this inherent failure mode is pervasive, exhibiting the exact same tight convergence rate across multiple natural network initializations. Our theoretical guarantees are derived via a rigorous analysis of the GD trajectories across the distinct activation patterns of the model. Specifically, we develop tight control over the system's dynamics to bound the trajectory of the decision boundary, overcoming the primary technical challenge introduced by the non-linear nature of the architecture.

