---
layout: default
title: SoFlow: Solution Flow Models for One-Step Generative Modeling
---

# SoFlow: Solution Flow Models for One-Step Generative Modeling
**arXiv**：[2512.15657v1](https://arxiv.org/abs/2512.15657) · [PDF](https://arxiv.org/pdf/2512.15657.pdf)  
**作者**：Tianze Luo, Haotian Yuan, Zhuang Liu  

**一句话要点**：提出SoFlow框架，通过流匹配和一致性损失实现一步生成，解决扩散模型效率问题。

**关键词**：一步生成, 流匹配模型, 扩散模型, 图像生成, 效率优化, 无分类器引导

## 3 点简述
- 针对扩散和流匹配模型多步去噪导致的效率低下问题，研究一步生成方法。
- 通过分析速度ODE的解函数关系，设计流匹配损失和无需JVP计算的一致性损失训练模型。
- 在ImageNet 256x256上，使用相同DiT架构和训练轮次，SoFlow的FID-50K优于MeanFlow模型。

## 摘要（原文）

> The multi-step denoising process in diffusion and Flow Matching models causes major efficiency issues, which motivates research on few-step generation. We present Solution Flow Models (SoFlow), a framework for one-step generation from scratch. By analyzing the relationship between the velocity function and the solution function of the velocity ordinary differential equation (ODE), we propose a Flow Matching loss and a solution consistency loss to train our models. The Flow Matching loss allows our models to provide estimated velocity fields for Classifier-Free Guidance (CFG) during training, which improves generation performance. Notably, our consistency loss does not require the calculation of the Jacobian-vector product (JVP), a common requirement in recent works that is not well-optimized in deep learning frameworks like PyTorch. Experimental results indicate that, when trained from scratch using the same Diffusion Transformer (DiT) architecture and an equal number of training epochs, our models achieve better FID-50K scores than MeanFlow models on the ImageNet 256x256 dataset.

