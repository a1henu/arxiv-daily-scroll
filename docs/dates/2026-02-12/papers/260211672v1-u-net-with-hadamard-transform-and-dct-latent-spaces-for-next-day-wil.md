---
layout: default
title: U-Net with Hadamard Transform and DCT Latent Spaces for Next-day Wildfire Spread Prediction
---

# U-Net with Hadamard Transform and DCT Latent Spaces for Next-day Wildfire Spread Prediction
**arXiv**：[2602.11672v1](https://arxiv.org/abs/2602.11672) · [PDF](https://arxiv.org/pdf/2602.11672.pdf)  
**作者**：Yingyi Luo, Shuaiang Rong, Adam Watts, Ahmet Enis Cetin  

**一句话要点**：提出TD-FusionUNet模型，结合可训练Hadamard变换和DCT层，用于轻量级次日野火蔓延预测。

**关键词**：野火蔓延预测, 轻量级模型, 变换域融合, 潜在空间学习, 多模态数据, 实时应用

## 3 点简述
- 核心问题：基于多模态卫星数据，开发轻量高效的次日野火蔓延预测工具。
- 方法要点：引入可训练Hadamard变换和DCT层，在正交化潜在空间中捕获频率成分，并采用随机边缘裁剪和高斯混合模型预处理。
- 实验或效果：在WildfireSpreadTS数据集上，以37万参数实现F1分数0.591，优于UNet基线，平衡准确性与效率。

## 摘要（原文）

> We developed a lightweight and computationally efficient tool for next-day wildfire spread prediction using multimodal satellite data as input. The deep learning model, which we call Transform Domain Fusion UNet (TD-FusionUNet), incorporates trainable Hadamard Transform and Discrete Cosine Transform layers that apply two-dimensional transforms, enabling the network to capture essential "frequency" components in orthogonalized latent spaces. Additionally, we introduce custom preprocessing techniques, including random margin cropping and a Gaussian mixture model, to enrich the representation of the sparse pre-fire masks and enhance the model's generalization capability. The TD-FusionUNet is evaluated on two datasets which are the Next-Day Wildfire Spread dataset released by Google Research in 2023, and WildfireSpreadTS dataset. Our proposed TD-FusionUNet achieves an F1 score of 0.591 with 370k parameters, outperforming the UNet baseline using ResNet18 as the encoder reported in the WildfireSpreadTS dataset while using substantially fewer parameters. These results show that the proposed latent space fusion model balances accuracy and efficiency under a lightweight setting, making it suitable for real time wildfire prediction applications in resource limited environments.

