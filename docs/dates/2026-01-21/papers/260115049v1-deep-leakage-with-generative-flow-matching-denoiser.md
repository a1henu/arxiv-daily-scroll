---
layout: default
title: Deep Leakage with Generative Flow Matching Denoiser
---

# Deep Leakage with Generative Flow Matching Denoiser
**arXiv**：[2601.15049v1](https://arxiv.org/abs/2601.15049) · [PDF](https://arxiv.org/pdf/2601.15049.pdf)  
**作者**：Isaac Baglin, Xiatian Zhu, Simon Hadfield  

**一句话要点**：提出基于生成流匹配先验的深度泄漏攻击，以提升联邦学习中数据重建的保真度与鲁棒性。

**关键词**：联邦学习, 深度泄漏攻击, 生成流匹配, 数据重建, 鲁棒性, 隐私保护

## 3 点简述
- 核心问题：联邦学习易受深度泄漏攻击，现有方法在保真度、稳定性或鲁棒性上不足。
- 方法要点：引入生成流匹配先验，引导优化朝向真实图像分布，无需私有数据知识。
- 实验或效果：在多个数据集和模型上优于现有攻击，对训练轮次、批次大小和常见防御保持有效。

## 摘要（原文）

> Federated Learning (FL) has emerged as a powerful paradigm for decentralized model training, yet it remains vulnerable to deep leakage (DL) attacks that reconstruct private client data from shared model updates. While prior DL methods have demonstrated varying levels of success, they often suffer from instability, limited fidelity, or poor robustness under realistic FL settings. We introduce a new DL attack that integrates a generative Flow Matching (FM) prior into the reconstruction process. By guiding optimization toward the distribution of realistic images (represented by a flow matching foundation model), our method enhances reconstruction fidelity without requiring knowledge of the private data. Extensive experiments on multiple datasets and target models demonstrate that our approach consistently outperforms state-of-the-art attacks across pixel-level, perceptual, and feature-based similarity metrics. Crucially, the method remains effective across different training epochs, larger client batch sizes, and under common defenses such as noise injection, clipping, and sparsification. Our findings call for the development of new defense strategies that explicitly account for adversaries equipped with powerful generative priors.

