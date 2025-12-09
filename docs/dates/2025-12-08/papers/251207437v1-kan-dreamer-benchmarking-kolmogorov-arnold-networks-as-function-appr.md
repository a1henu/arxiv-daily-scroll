---
layout: default
title: KAN-Dreamer: Benchmarking Kolmogorov-Arnold Networks as Function Approximators in World Models
---

# KAN-Dreamer: Benchmarking Kolmogorov-Arnold Networks as Function Approximators in World Models
**arXiv**：[2512.07437v1](https://arxiv.org/abs/2512.07437) · [PDF](https://arxiv.org/pdf/2512.07437.pdf)  
**作者**：Chenwei Shi, Xueyu Luan  

**一句话要点**：提出KAN-Dreamer，将KAN架构集成到DreamerV3中作为函数逼近器进行基准测试。

**关键词**：基于模型的强化学习, Kolmogorov-Arnold网络, 世界模型, 函数逼近, 样本效率, JAX实现

## 3 点简述
- 研究将Kolmogorov-Arnold Networks（KANs）作为MLP替代品集成到DreamerV3世界模型中。
- 在JAX框架下实现向量化版本，用KAN和FastKAN替换特定MLP和卷积组件。
- 在DeepMind Control Suite上实验，FastKAN在奖励和继续预测器上性能与MLP相当。

## 摘要（原文）

> DreamerV3 is a state-of-the-art online model-based reinforcement learning (MBRL) algorithm known for remarkable sample efficiency. Concurrently, Kolmogorov-Arnold Networks (KANs) have emerged as a promising alternative to Multi-Layer Perceptrons (MLPs), offering superior parameter efficiency and interpretability. To mitigate KANs' computational overhead, variants like FastKAN leverage Radial Basis Functions (RBFs) to accelerate inference. In this work, we investigate integrating KAN architectures into the DreamerV3 framework. We introduce KAN-Dreamer, replacing specific MLP and convolutional components of DreamerV3 with KAN and FastKAN layers. To ensure efficiency within the JAX-based World Model, we implement a tailored, fully vectorized version with simplified grid management. We structure our investigation into three subsystems: Visual Perception, Latent Prediction, and Behavior Learning. Empirical evaluations on the DeepMind Control Suite (walker_walk) analyze sample efficiency, training time, and asymptotic performance. Experimental results demonstrate that utilizing our adapted FastKAN as a drop-in replacement for the Reward and Continue predictors yields performance on par with the original MLP-based architecture, maintaining parity in both sample efficiency and training speed. This report serves as a preliminary study for future developments in KAN-based world models.

