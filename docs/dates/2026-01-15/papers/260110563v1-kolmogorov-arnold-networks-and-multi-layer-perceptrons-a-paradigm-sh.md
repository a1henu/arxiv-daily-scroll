---
layout: default
title: Kolmogorov Arnold Networks and Multi-Layer Perceptrons: A Paradigm Shift in Neural Modelling
---

# Kolmogorov Arnold Networks and Multi-Layer Perceptrons: A Paradigm Shift in Neural Modelling
**arXiv**：[2601.10563v1](https://arxiv.org/abs/2601.10563) · [PDF](https://arxiv.org/pdf/2601.10563.pdf)  
**作者**：Aradhya Gaonkar, Nihal Jain, Vignesh Chougule, Nikhil Deshpande, Sneha Varur, Channabasappa Muttal  

**一句话要点**：提出Kolmogorov-Arnold网络，在非线性函数逼近等任务中超越多层感知机，实现计算效率与精度的平衡。

**关键词**：Kolmogorov-Arnold网络, 多层感知机, 非线性函数逼近, 计算效率, 自适应激活函数, 资源受限环境

## 3 点简述
- 核心问题：比较KAN与MLP在非线性函数逼近、时间序列预测和多变量分类中的性能差异。
- 方法要点：KAN基于Kolmogorov表示定理，采用自适应样条激活函数和网格结构，提升模型表达能力。
- 实验或效果：在多个数据集上，KAN在预测精度和计算成本（如MSE和FLOPs）上均优于MLP，适用于资源受限场景。

## 摘要（原文）

> The research undertakes a comprehensive comparative analysis of Kolmogorov-Arnold Networks (KAN) and Multi-Layer Perceptrons (MLP), highlighting their effectiveness in solving essential computational challenges like nonlinear function approximation, time-series prediction, and multivariate classification. Rooted in Kolmogorov's representation theorem, KANs utilize adaptive spline-based activation functions and grid-based structures, providing a transformative approach compared to traditional neural network frameworks. Utilizing a variety of datasets spanning mathematical function estimation (quadratic and cubic) to practical uses like predicting daily temperatures and categorizing wines, the proposed research thoroughly assesses model performance via accuracy measures like Mean Squared Error (MSE) and computational expense assessed through Floating Point Operations (FLOPs). The results indicate that KANs reliably exceed MLPs in every benchmark, attaining higher predictive accuracy with significantly reduced computational costs. Such an outcome highlights their ability to maintain a balance between computational efficiency and accuracy, rendering them especially beneficial in resource-limited and real-time operational environments. By elucidating the architectural and functional distinctions between KANs and MLPs, the paper provides a systematic framework for selecting the most suitable neural architectures for specific tasks. Furthermore, the proposed study highlights the transformative capabilities of KANs in progressing intelligent systems, influencing their use in situations that require both interpretability and computational efficiency.

