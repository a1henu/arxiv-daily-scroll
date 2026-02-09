---
layout: default
title: Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning
---

# Designing a Robust, Bounded, and Smooth Loss Function for Improved Supervised Learning
**arXiv**：[2602.06858v1](https://arxiv.org/abs/2602.06858) · [PDF](https://arxiv.org/pdf/2602.06858.pdf)  
**作者**：Soumi Mahato, Lineesh M. C  

**一句话要点**：提出RoBoS-NN损失函数以提升监督学习在异常值敏感数据集中的性能

**关键词**：损失函数设计, 鲁棒学习, 监督学习, 时间序列预测, 神经网络

## 3 点简述
- 传统损失函数在处理高维和异常值敏感数据集时存在性能下降和收敛慢的问题
- 开发了鲁棒、有界且平滑的RoBoS-NN损失函数，并理论分析其泛化能力
- 在时间序列预测实验中，RoBoS-NN算法在含异常值数据上优于基准模型

## 摘要（原文）

> The loss function is crucial to machine learning, especially in supervised learning frameworks. It is a fundamental component that controls the behavior and general efficacy of learning algorithms. However, despite their widespread use, traditional loss functions have significant drawbacks when dealing with high-dimensional and outlier-sensitive datasets, which frequently results in reduced performance and slower convergence during training. In this work, we develop a robust, bounded, and smooth (RoBoS-NN) loss function to resolve the aforementioned hindrances. The generalization ability of the loss function has also been theoretically analyzed to rigorously justify its robustness. Moreover, we implement RoboS-NN loss in the framework of a neural network (NN) to forecast time series and present a new robust algorithm named $\mathcal{L}_{\text{RoBoS}}$-NN. To assess the potential of $\mathcal{L}_{\text{RoBoS}}$-NN, we conduct experiments on multiple real-world datasets. In addition, we infuse outliers into data sets to evaluate the performance of $\mathcal{L}_{\text{RoBoS}}$-NN in more challenging scenarios. Numerical results show that $\mathcal{L}_{\text{RoBoS}}$-NN outperforms the other benchmark models in terms of accuracy measures.

