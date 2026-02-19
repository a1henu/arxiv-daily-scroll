---
layout: default
title: Conjugate Learning Theory: Uncovering the Mechanisms of Trainability and Generalization in Deep Neural Networks
---

# Conjugate Learning Theory: Uncovering the Mechanisms of Trainability and Generalization in Deep Neural Networks
**arXiv**：[2602.16177v1](https://arxiv.org/abs/2602.16177) · [PDF](https://arxiv.org/pdf/2602.16177.pdf)  
**作者**：Binchuan Qi  

**一句话要点**：提出共轭学习理论框架，基于凸共轭对偶性分析深度神经网络的训练性与泛化性。

**关键词**：共轭学习理论, 深度神经网络训练, 泛化误差分析, 凸共轭对偶性, 非凸优化

## 3 点简述
- 核心问题：在有限样本下定义实际可学习性，并分析深度神经网络训练与泛化的理论机制。
- 方法要点：利用共轭对偶性推导训练收敛定理和泛化误差界，量化模型结构、数据等因素的影响。
- 实验或效果：通过广泛实验验证理论预测，确认框架的正确性和一致性。

## 摘要（原文）

> In this work, we propose a notion of practical learnability grounded in finite sample settings, and develop a conjugate learning theoretical framework based on convex conjugate duality to characterize this learnability property. Building on this foundation, we demonstrate that training deep neural networks (DNNs) with mini-batch stochastic gradient descent (SGD) achieves global optima of empirical risk by jointly controlling the extreme eigenvalues of a structure matrix and the gradient energy, and we establish a corresponding convergence theorem. We further elucidate the impact of batch size and model architecture (including depth, parameter count, sparsity, skip connections, and other characteristics) on non-convex optimization. Additionally, we derive a model-agnostic lower bound for the achievable empirical risk, theoretically demonstrating that data determines the fundamental limit of trainability. On the generalization front, we derive deterministic and probabilistic bounds on generalization error based on generalized conditional entropy measures. The former explicitly delineates the range of generalization error, while the latter characterizes the distribution of generalization error relative to the deterministic bounds under independent and identically distributed (i.i.d.) sampling conditions. Furthermore, these bounds explicitly quantify the influence of three key factors: (i) information loss induced by irreversibility in the model, (ii) the maximum attainable loss value, and (iii) the generalized conditional entropy of features with respect to labels. Moreover, they offer a unified theoretical lens for understanding the roles of regularization, irreversible transformations, and network depth in shaping the generalization behavior of deep neural networks. Extensive experiments validate all theoretical predictions, confirming the framework's correctness and consistency.

