---
layout: default
title: Assessing the performance of correlation-based multi-fidelity neural emulators
---

# Assessing the performance of correlation-based multi-fidelity neural emulators
**arXiv**：[2512.02868v1](https://arxiv.org/abs/2512.02868) · [PDF](https://arxiv.org/pdf/2512.02868.pdf)  
**作者**：Cristian J. Villatoro, Gianluca Geraci, Daniele E. Schiavazzi  

**一句话要点**：评估基于相关性的多保真度神经模拟器性能，以降低高保真模型计算成本

**关键词**：多保真度模拟器, 神经网络性能评估, 计算成本降低, 数据融合, 谱偏置网络, 不确定性量化

## 3 点简述
- 研究多保真度神经模拟器，结合低保真度数据与稀缺高保真度数据，提升预测效率
- 测试多种网络架构和数据集配置，包括不同谱偏置网络和坐标编码机制
- 通过单保真度对比实验，量化多保真度方法在性能增益上的优势

## 摘要（原文）

> Outer loop tasks such as optimization, uncertainty quantification or inference can easily become intractable when the underlying high-fidelity model is computationally expensive. Similarly, data-driven architectures typically require large datasets to perform predictive tasks with sufficient accuracy. A possible approach to mitigate these challenges is the development of multi-fidelity emulators, leveraging potentially biased, inexpensive low-fidelity information while correcting and refining predictions using scarce, accurate high-fidelity data. This study investigates the performance of multi-fidelity neural emulators, neural networks designed to learn the input-to-output mapping by integrating limited high-fidelity data with abundant low-fidelity model solutions. We investigate the performance of such emulators for low and high-dimensional functions, with oscillatory character, in the presence of discontinuities, for collections of models with equal and dissimilar parametrization, and for a possibly large number of potentially corrupted low-fidelity sources. In doing so, we consider a large number of architectural, hyperparameter, and dataset configurations including networks with a different amount of spectral bias (Multi-Layered Perceptron, Siren and Kolmogorov Arnold Network), various mechanisms for coordinate encoding, exact or learnable low-fidelity information, and for varying training dataset size. We further analyze the added value of the multi-fidelity approach by conducting equivalent single-fidelity tests for each case, quantifying the performance gains achieved through fusing multiple sources of information.

