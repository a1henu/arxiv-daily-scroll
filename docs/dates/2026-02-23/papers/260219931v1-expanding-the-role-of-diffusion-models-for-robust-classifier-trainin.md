---
layout: default
title: Expanding the Role of Diffusion Models for Robust Classifier Training
---

# Expanding the Role of Diffusion Models for Robust Classifier Training
**arXiv**：[2602.19931v1](https://arxiv.org/abs/2602.19931) · [PDF](https://arxiv.org/pdf/2602.19931.pdf)  
**作者**：Pin-Han Huang, Shang-Tse Chen, Hsuan-Tien Lin  

**一句话要点**：提出利用扩散模型内部表征作为辅助学习信号，以增强对抗训练中鲁棒图像分类器的性能。

**关键词**：扩散模型, 对抗训练, 鲁棒分类器, 表征学习, 合成数据, 特征解耦

## 3 点简述
- 核心问题：扩散模型在对抗训练中仅用于生成合成数据，其内部表征的潜在价值未被充分探索。
- 方法要点：系统分析扩散模型表征的多样性和部分鲁棒性，并将其作为辅助信号融入对抗训练过程。
- 实验或效果：在CIFAR-10、CIFAR-100和ImageNet上验证，联合使用扩散表征和合成数据能提升鲁棒性并促进特征解耦。

## 摘要（原文）

> Incorporating diffusion-generated synthetic data into adversarial training (AT) has been shown to substantially improve the training of robust image classifiers. In this work, we extend the role of diffusion models beyond merely generating synthetic data, examining whether their internal representations, which encode meaningful features of the data, can provide additional benefits for robust classifier training. Through systematic experiments, we show that diffusion models offer representations that are both diverse and partially robust, and that explicitly incorporating diffusion representations as an auxiliary learning signal during AT consistently improves robustness across settings. Furthermore, our representation analysis indicates that incorporating diffusion models into AT encourages more disentangled features, while diffusion representations and diffusion-generated synthetic data play complementary roles in shaping representations. Experiments on CIFAR-10, CIFAR-100, and ImageNet validate these findings, demonstrating the effectiveness of jointly leveraging diffusion representations and synthetic data within AT.

