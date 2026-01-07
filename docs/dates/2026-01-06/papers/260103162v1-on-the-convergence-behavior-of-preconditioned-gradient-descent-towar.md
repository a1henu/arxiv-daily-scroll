---
layout: default
title: On the Convergence Behavior of Preconditioned Gradient Descent Toward the Rich Learning Regime
---

# On the Convergence Behavior of Preconditioned Gradient Descent Toward the Rich Learning Regime
**arXiv**：[2601.03162v1](https://arxiv.org/abs/2601.03162) · [PDF](https://arxiv.org/pdf/2601.03162.pdf)  
**作者**：Shuai Jiang, Alexey Voronin, Eric Cyr, Ben Southworth  

**一句话要点**：研究预条件梯度下降对谱偏置和grokking现象的影响，以促进神经网络学习

**关键词**：谱偏置, 预条件梯度下降, grokking现象, 神经网络优化, NTK机制

## 3 点简述
- 核心问题：谱偏置和grokking现象限制神经网络在科学任务中的快速训练和精细结构捕捉。
- 方法要点：通过预条件梯度下降（如高斯-牛顿法）理论分析和实验验证其对谱偏置的缓解作用。
- 实验或效果：实验证实预条件梯度下降能减少grokking延迟，支持其作为NTK与丰富学习机制间过渡行为的假设。

## 摘要（原文）

> Spectral bias, the tendency of neural networks to learn low frequencies first, can be both a blessing and a curse. While it enhances the generalization capabilities by suppressing high-frequency noise, it can be a limitation in scientific tasks that require capturing fine-scale structures. The delayed generalization phenomenon known as grokking is another barrier to rapid training of neural networks. Grokking has been hypothesized to arise as learning transitions from the NTK to the feature-rich regime. This paper explores the impact of preconditioned gradient descent (PGD), such as Gauss-Newton, on spectral bias and grokking phenomena. We demonstrate through theoretical and empirical results how PGD can mitigate issues associated with spectral bias. Additionally, building on the rich learning regime grokking hypothesis, we study how PGD can be used to reduce delays associated with grokking. Our conjecture is that PGD, without the impediment of spectral bias, enables uniform exploration of the parameter space in the NTK regime. Our experimental results confirm this prediction, providing strong evidence that grokking represents a transitional behavior between the lazy regime characterized by the NTK and the rich regime. These findings deepen our understanding of the interplay between optimization dynamics, spectral bias, and the phases of neural network learning.

