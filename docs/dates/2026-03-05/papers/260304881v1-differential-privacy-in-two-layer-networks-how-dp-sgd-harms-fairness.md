---
layout: default
title: Differential Privacy in Two-Layer Networks: How DP-SGD Harms Fairness and Robustness
---

# Differential Privacy in Two-Layer Networks: How DP-SGD Harms Fairness and Robustness
**arXiv**：[2603.04881v1](https://arxiv.org/abs/2603.04881) · [PDF](https://arxiv.org/pdf/2603.04881.pdf)  
**作者**：Ruichen Xu, Kexin Chen  

**一句话要点**：提出特征中心框架分析DP-SGD在双层ReLU卷积网络中的特征学习动态，揭示隐私噪声如何损害公平性和鲁棒性。

**关键词**：差分隐私学习, 特征学习动态, 公平性分析, 对抗鲁棒性, 双层神经网络, 特征噪声比

## 3 点简述
- 核心问题：差分隐私学习在现代非凸神经网络中导致性能下降、公平性问题和对抗鲁棒性降低的理论机制未知。
- 方法要点：引入特征中心框架，基于特征噪声比（FNR）分析DP-SGD的特征学习动态，建立测试损失界限。
- 实验或效果：在合成和真实数据上验证理论发现，包括类间FNR不平衡导致差异影响、噪声对语义长尾数据负面影响更大，以及公共预训练-私有微调范式在特征分布偏移下可能无效。

## 摘要（原文）

> Differentially private learning is essential for training models on sensitive data, but empirical studies consistently show that it can degrade performance, introduce fairness issues like disparate impact, and reduce adversarial robustness. The theoretical underpinnings of these phenomena in modern, non-convex neural networks remain largely unexplored. This paper introduces a unified feature-centric framework to analyze the feature learning dynamics of differentially private stochastic gradient descent (DP-SGD) in two-layer ReLU convolutional neural networks. Our analysis establishes test loss bounds governed by a crucial metric: the feature-to-noise ratio (FNR). We demonstrate that the noise required for privacy leads to suboptimal feature learning, and specifically show that: 1) imbalanced FNRs across classes and subpopulations cause disparate impact; 2) even in the same class, noise has a greater negative impact on semantically long-tailed data; and 3) noise injection exacerbates vulnerability to adversarial attacks. Furthermore, our analysis reveals that the popular paradigm of public pre-training and private fine-tuning does not guarantee improvement, particularly under significant feature distribution shifts between datasets. Experiments on synthetic and real-world data corroborate our theoretical findings.

