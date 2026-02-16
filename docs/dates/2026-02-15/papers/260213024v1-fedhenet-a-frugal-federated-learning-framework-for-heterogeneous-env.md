---
layout: default
title: FedHENet: A Frugal Federated Learning Framework for Heterogeneous Environments
---

# FedHENet: A Frugal Federated Learning Framework for Heterogeneous Environments
**arXiv**：[2602.13024v1](https://arxiv.org/abs/2602.13024) · [PDF](https://arxiv.org/pdf/2602.13024.pdf)  
**作者**：Alejandro Dopico-Castro, Oscar Fontenla-Romero, Bertha Guijarro-Berdiñas, Amparo Alonso-Betanzos, Iván Pérez Digón  

**一句话要点**：提出FedHENet以解决异构环境下联邦学习的隐私、效率和稳定性问题

**关键词**：联邦学习, 同态加密, 异构环境, 能效优化, 图像分类, 隐私保护

## 3 点简述
- 核心问题：传统联邦学习依赖迭代优化，隐私风险高且能耗大，尤其在异构环境中。
- 方法要点：使用预训练特征提取器固定，仅学习输出层，通过同态加密单轮通信聚合知识。
- 实验或效果：在图像分类中达到竞争性准确率，稳定性更优，能效提升达70%，且无需超参数调优。

## 摘要（原文）

> Federated Learning (FL) enables collaborative training without centralizing data, essential for privacy compliance in real-world scenarios involving sensitive visual information. Most FL approaches rely on expensive, iterative deep network optimization, which still risks privacy via shared gradients. In this work, we propose FedHENet, extending the FedHEONN framework to image classification. By using a fixed, pre-trained feature extractor and learning only a single output layer, we avoid costly local fine-tuning. This layer is learned by analytically aggregating client knowledge in a single round of communication using homomorphic encryption (HE). Experiments show that FedHENet achieves competitive accuracy compared to iterative FL baselines while demonstrating superior stability performance and up to 70\% better energy efficiency. Crucially, our method is hyperparameter-free, removing the carbon footprint associated with hyperparameter tuning in standard FL. Code available in https://github.com/AlejandroDopico2/FedHENet/

