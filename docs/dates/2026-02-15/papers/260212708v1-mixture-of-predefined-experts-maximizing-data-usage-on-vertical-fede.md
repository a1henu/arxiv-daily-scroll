---
layout: default
title: Mixture of Predefined Experts: Maximizing Data Usage on Vertical Federated Learning
---

# Mixture of Predefined Experts: Maximizing Data Usage on Vertical Federated Learning
**arXiv**：[2602.12708v1](https://arxiv.org/abs/2602.12708) · [PDF](https://arxiv.org/pdf/2602.12708.pdf)  
**作者**：Jon Irureta, Gorka Azkune, Jon Imaz, Aizea Lojo, Javier Fernandez-Marques  

**一句话要点**：提出Split-MoPE框架以解决垂直联邦学习中样本不对齐问题，最大化数据使用。

**关键词**：垂直联邦学习, 样本不对齐, 预定义专家混合, Split Learning, 通信效率, 鲁棒性

## 3 点简述
- 核心问题：垂直联邦学习依赖全样本对齐假设，现实场景中样本常不对齐。
- 方法要点：结合Split Learning与预定义专家混合架构，处理特定数据对齐，无需全样本重叠。
- 实验或效果：在视觉和表格数据集上优于LASER和Vertical SplitNN，减少通信开销并增强鲁棒性。

## 摘要（原文）

> Vertical Federated Learning (VFL) has emerged as a critical paradigm for collaborative model training in privacy-sensitive domains such as finance and healthcare. However, most existing VFL frameworks rely on the idealized assumption of full sample alignment across participants, a premise that rarely holds in real-world scenarios. To bridge this gap, this work introduces Split-MoPE, a novel framework that integrates Split Learning with a specialized Mixture of Predefined Experts (MoPE) architecture. Unlike standard Mixture of Experts (MoE), where routing is learned dynamically, MoPE uses predefined experts to process specific data alignments, effectively maximizing data usage during both training and inference without requiring full sample overlap. By leveraging pretrained encoders for target data domains, Split-MoPE achieves state-of-the-art performance in a single communication round, significantly reducing the communication footprint compared to multi-round end-to-end training. Furthermore, unlike existing proposals that address sample misalignment, this novel architecture provides inherent robustness against malicious or noisy participants and offers per-sample interpretability by quantifying each collaborator's contribution to each prediction. Extensive evaluations on vision (CIFAR-10/100) and tabular (Breast Cancer Wisconsin) datasets demonstrate that Split-MoPE consistently outperforms state-of-the-art systems such as LASER and Vertical SplitNN, particularly in challenging scenarios with high data missingness.

