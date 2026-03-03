---
layout: default
title: Meta-Learning Hyperparameters for Parameter Efficient Fine-Tuning
---

# Meta-Learning Hyperparameters for Parameter Efficient Fine-Tuning
**arXiv**：[2603.01759v1](https://arxiv.org/abs/2603.01759) · [PDF](https://arxiv.org/pdf/2603.01759.pdf)  
**作者**：Zichen Tian, Yaoyao Liu, Qianru Sun  

**一句话要点**：提出MetaPEFT方法，通过自适应缩放器动态调整PEFT模块影响，以解决遥感图像微调中固定超参数限制性能的问题。

**关键词**：参数高效微调, 元学习, 遥感图像, 自适应缩放, 尾类性能, 迁移学习

## 3 点简述
- 核心问题：固定超参数（如插入位置和缩放因子）在遥感图像微调中显著限制参数高效微调（PEFT）性能。
- 方法要点：MetaPEFT引入自适应缩放器，动态调整模块插入、层选择和模块学习率，优化PEFT模块在网络中的影响。
- 实验或效果：在三个迁移学习场景和五个数据集上验证，MetaPEFT以少量可训练参数实现最先进性能，显著提升尾类准确率。

## 摘要（原文）

> Training large foundation models from scratch for domain-specific applications is almost impossible due to data limits and long-tailed distributions -- taking remote sensing (RS) as an example. Fine-tuning natural image pre-trained models on RS images is a straightforward solution. To reduce computational costs and improve performance on tail classes, existing methods apply parameter-efficient fine-tuning (PEFT) techniques, such as LoRA and AdaptFormer. However, we observe that fixed hyperparameters -- such as intra-layer positions, layer depth, and scaling factors, can considerably hinder PEFT performance, as fine-tuning on RS images proves highly sensitive to these settings. To address this, we propose MetaPEFT, a method incorporating adaptive scalers that dynamically adjust module influence during fine-tuning. MetaPEFT dynamically adjusts three key factors of PEFT on RS images: module insertion, layer selection, and module-wise learning rates, which collectively control the influence of PEFT modules across the network. We conduct extensive experiments on three transfer-learning scenarios and five datasets in both RS and natural image domains. The results show that MetaPEFT achieves state-of-the-art performance in cross-spectral adaptation, requiring only a small amount of trainable parameters and improving tail-class accuracy significantly.

