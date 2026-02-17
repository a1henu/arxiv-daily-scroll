---
layout: default
title: Unbiased Approximate Vector-Jacobian Products for Efficient Backpropagation
---

# Unbiased Approximate Vector-Jacobian Products for Efficient Backpropagation
**arXiv**：[2602.14701v1](https://arxiv.org/abs/2602.14701) · [PDF](https://arxiv.org/pdf/2602.14701.pdf)  
**作者**：Killian Bakong, Laurent Massoulié, Edouard Oyallon, Kevin Scaman  

**一句话要点**：提出无偏近似向量-雅可比积方法以降低深度神经网络训练成本

**关键词**：反向传播优化, 无偏近似, 向量-雅可比积, 训练成本降低, 深度神经网络, 随机方法

## 3 点简述
- 核心问题：深度神经网络训练中向量-雅可比积计算成本高，影响计算和内存效率
- 方法要点：在反向传播中使用随机无偏近似替代精确向量-雅可比积，分析精度与成本权衡
- 实验或效果：在多层感知机、BagNets和视觉Transformer上验证理论，显示成本降低潜力

## 摘要（原文）

> In this work we introduce methods to reduce the computational and memory costs of training deep neural networks. Our approach consists in replacing exact vector-jacobian products by randomized, unbiased approximations thereof during backpropagation. We provide a theoretical analysis of the trade-off between the number of epochs needed to achieve a target precision and the cost reduction for each epoch. We then identify specific unbiased estimates of vector-jacobian products for which we establish desirable optimality properties of minimal variance under sparsity constraints. Finally we provide in-depth experiments on multi-layer perceptrons, BagNets and Visual Transfomers architectures. These validate our theoretical results, and confirm the potential of our proposed unbiased randomized backpropagation approach for reducing the cost of deep learning.

