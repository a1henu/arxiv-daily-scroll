---
layout: default
title: Elimination-compensation pruning for fully-connected neural networks
---

# Elimination-compensation pruning for fully-connected neural networks
**arXiv**：[2602.20467v1](https://arxiv.org/abs/2602.20467) · [PDF](https://arxiv.org/pdf/2602.20467.pdf)  
**作者**：Enrico Ballini, Luca Muscarnera, Alessio Fumagalli, Anna Scotti, Francesco Regazzoni  

**一句话要点**：提出消除-补偿剪枝方法，通过偏置扰动优化全连接神经网络剪枝效果

**关键词**：神经网络剪枝, 全连接网络, 偏置补偿, 自动微分, 稀疏表示, 模型压缩

## 3 点简述
- 核心问题：传统剪枝假设权重重要性仅基于其对误差的影响，可能忽略权重与偏置的交互作用
- 方法要点：引入权重重要性度量，考虑移除权重后通过自动微分计算最优偏置扰动以补偿输出行为
- 实验或效果：在多种机器学习场景中，该方法相比流行剪枝策略展现出内在效率优势

## 摘要（原文）

> The unmatched ability of Deep Neural Networks in capturing complex patterns in large and noisy datasets is often associated with their large hypothesis space, and consequently to the vast amount of parameters that characterize model architectures. Pruning techniques affirmed themselves as valid tools to extract sparse representations of neural networks parameters, carefully balancing between compression and preservation of information. However, a fundamental assumption behind pruning is that expendable weights should have small impact on the error of the network, while highly important weights should tend to have a larger influence on the inference. We argue that this idea could be generalized; what if a weight is not simply removed but also compensated with a perturbation of the adjacent bias, which does not contribute to the network sparsity? Our work introduces a novel pruning method in which the importance measure of each weight is computed considering the output behavior after an optimal perturbation of its adjacent bias, efficiently computable by automatic differentiation. These perturbations can be then applied directly after the removal of each weight, independently of each other. After deriving analytical expressions for the aforementioned quantities, numerical experiments are conducted to benchmark this technique against some of the most popular pruning strategies, demonstrating an intrinsic efficiency of the proposed approach in very diverse machine learning scenarios. Finally, our findings are discussed and the theoretical implications of our results are presented.

