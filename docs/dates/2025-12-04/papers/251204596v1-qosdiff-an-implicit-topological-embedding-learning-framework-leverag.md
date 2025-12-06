---
layout: default
title: QoSDiff: An Implicit Topological Embedding Learning Framework Leveraging Denoising Diffusion and Adversarial Attention for Robust QoS Prediction
---

# QoSDiff: An Implicit Topological Embedding Learning Framework Leveraging Denoising Diffusion and Adversarial Attention for Robust QoS Prediction
**arXiv**：[2512.04596v1](https://arxiv.org/abs/2512.04596) · [PDF](https://arxiv.org/pdf/2512.04596.pdf)  
**作者**：Guanchen Du, Jianlong Xu, Wei Wei  

**一句话要点**：提出QoSDiff框架，利用去噪扩散和对抗注意力进行隐式拓扑嵌入学习，以解决QoS预测中的图依赖和噪声问题。

**关键词**：QoS预测, 去噪扩散模型, 对抗学习, 注意力机制, 隐式拓扑嵌入, 服务计算

## 3 点简述
- 核心问题：现有QoS预测方法依赖显式用户-服务交互图，导致可扩展性瓶颈和噪声敏感。
- 方法要点：结合去噪扩散模型恢复潜在结构，并引入对抗交互模块通过双向混合注意力捕获高阶关联。
- 实验或效果：在真实数据集上超越基线，展现出强泛化能力和对数据稀疏与噪声的鲁棒性。

## 摘要（原文）

> Accurate Quality of Service (QoS) prediction is fundamental to service computing, providing essential data-driven guidance for service selection and ensuring superior user experiences. However, prevalent approaches, particularly Graph Neural Networks (GNNs), heavily rely on constructing explicit user--service interaction graphs. This dependency introduces severe scalability bottlenecks and limits performance when explicit connections are sparse or corrupted by noise. To address these challenges, this paper introduces \emph{QoSDiff}, a novel embedding learning framework that bypasses the prerequisite of explicit graph construction. Specifically, it leverages a denoising diffusion probabilistic model to recover intrinsic latent structures from noisy initializations. To further capture high-order interactions, we propose an adversarial interaction module that integrates a bidirectional hybrid attention mechanism. This adversarial paradigm dynamically distinguishes informative patterns from noise, enabling a dual-perspective modeling of intricate user--service associations. Extensive experiments on two large-scale real-world datasets demonstrate that QoSDiff significantly outperforms state-of-the-art baselines. Notably, the results highlight the framework's superior cross-dataset generalization capability and exceptional robustness against data sparsity and observational noise.

