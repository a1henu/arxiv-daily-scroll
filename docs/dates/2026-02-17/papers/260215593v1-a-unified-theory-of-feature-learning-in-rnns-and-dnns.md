---
layout: default
title: A unified theory of feature learning in RNNs and DNNs
---

# A unified theory of feature learning in RNNs and DNNs
**arXiv**：[2602.15593v1](https://arxiv.org/abs/2602.15593) · [PDF](https://arxiv.org/pdf/2602.15593.pdf)  
**作者**：Jan P. Bauer, Kirsten Fischer, Moritz Helias, Agostina Palmigiano  

**一句话要点**：提出基于表示核的统一平均场理论，以解释RNNs和DNNs在特征学习中的功能差异。

**关键词**：表示核, 平均场理论, 特征学习, 权重共享, 贝叶斯推断, 归纳偏置

## 3 点简述
- 核心问题：RNNs和DNNs结构相似但功能不同，如何统一解释其差异？
- 方法要点：使用表示核的平均场理论，将训练建模为序列和模式的贝叶斯推断。
- 实验或效果：在DNN任务中识别相变，RNNs在时序任务中通过权重共享诱导归纳偏置。

## 摘要（原文）

> Recurrent and deep neural networks (RNNs/DNNs) are cornerstone architectures in machine learning. Remarkably, RNNs differ from DNNs only by weight sharing, as can be shown through unrolling in time. How does this structural similarity fit with the distinct functional properties these networks exhibit? To address this question, we here develop a unified mean-field theory for RNNs and DNNs in terms of representational kernels, describing fully trained networks in the feature learning ($μ$P) regime. This theory casts training as Bayesian inference over sequences and patterns, directly revealing the functional implications induced by the RNNs' weight sharing. In DNN-typical tasks, we identify a phase transition when the learning signal overcomes the noise due to randomness in the weights: below this threshold, RNNs and DNNs behave identically; above it, only RNNs develop correlated representations across timesteps. For sequential tasks, the RNNs' weight sharing furthermore induces an inductive bias that aids generalization by interpolating unsupervised time steps. Overall, our theory offers a way to connect architectural structure to functional biases.

