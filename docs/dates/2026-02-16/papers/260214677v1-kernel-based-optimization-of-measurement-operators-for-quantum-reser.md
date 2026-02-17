---
layout: default
title: Kernel-based optimization of measurement operators for quantum reservoir computers
---

# Kernel-based optimization of measurement operators for quantum reservoir computers
**arXiv**：[2602.14677v1](https://arxiv.org/abs/2602.14677) · [PDF](https://arxiv.org/pdf/2602.14677.pdf)  
**作者**：Markus Gross, Hans-Martin Rieser  

**一句话要点**：提出基于核优化的测量算子训练方法，以提升量子储层计算机性能

**关键词**：量子储层计算机, 核岭回归, 测量算子优化, 量子机器学习, 图像分类, 时间序列预测

## 3 点简述
- 核心问题：量子储层计算机中固定量子特征映射需优化测量算子以最小化预测误差
- 方法要点：在核岭回归框架下训练无状态和有状态量子储层计算机，实现高效优化
- 实验或效果：在图像分类和时间序列预测任务中验证方法有效性，适用于其他量子机器学习模型

## 摘要（原文）

> Finding optimal measurement operators is crucial for the performance of quantum reservoir computers (QRCs), since they employ a fixed quantum feature map. We formulate the training of both stateless (quantum extreme learning machines, QELMs) and stateful (memory dependent) QRCs in the framework of kernel ridge regression. This approach renders an optimal measurement operator that minimizes prediction error for a given reservoir and training dataset. For large qubit numbers, this method is more efficient than the conventional training of QRCs. We discuss efficiency and practical implementation strategies, including Pauli basis decomposition and operator diagonalization, to adapt the optimal observable to hardware constraints. Numerical experiments on image classification and time series prediction tasks demonstrate the effectiveness of this approach, which can also be applied to other quantum ML models.

