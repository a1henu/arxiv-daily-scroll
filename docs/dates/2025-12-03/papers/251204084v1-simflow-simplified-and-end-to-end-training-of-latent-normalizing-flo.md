---
layout: default
title: SimFlow: Simplified and End-to-End Training of Latent Normalizing Flows
---

# SimFlow: Simplified and End-to-End Training of Latent Normalizing Flows
**arXiv**：[2512.04084v1](https://arxiv.org/abs/2512.04084) · [PDF](https://arxiv.org/pdf/2512.04084.pdf)  
**作者**：Qinyu Zhao, Guangting Zheng, Tao Yang, Rui Zhu, Xingjian Leng, Stephen Gould, Liang Zheng  

**一句话要点**：提出SimFlow，通过固定方差简化并端到端训练潜在归一化流，提升图像生成质量。

**关键词**：归一化流, 变分自编码器, 图像生成, 端到端训练, 固定方差

## 3 点简述
- 核心问题：现有方法依赖噪声增强或冻结VAE编码器，导致流程复杂且生成质量受限。
- 方法要点：固定VAE编码器输出的方差为常数，简化训练并实现端到端联合优化。
- 实验或效果：在ImageNet 256×256生成任务中，SimFlow取得gFID 2.15，优于STARFlow，结合REPA-E后达1.91，创NFs新纪录。

## 摘要（原文）

> Normalizing Flows (NFs) learn invertible mappings between the data and a Gaussian distribution. Prior works usually suffer from two limitations. First, they add random noise to training samples or VAE latents as data augmentation, introducing complex pipelines including extra noising and denoising steps. Second, they use a pretrained and frozen VAE encoder, resulting in suboptimal reconstruction and generation quality. In this paper, we find that the two issues can be solved in a very simple way: just fixing the variance (which would otherwise be predicted by the VAE encoder) to a constant (e.g., 0.5). On the one hand, this method allows the encoder to output a broader distribution of tokens and the decoder to learn to reconstruct clean images from the augmented token distribution, avoiding additional noise or denoising design. On the other hand, fixed variance simplifies the VAE evidence lower bound, making it stable to train an NF with a VAE jointly. On the ImageNet $256 \times 256$ generation task, our model SimFlow obtains a gFID score of 2.15, outperforming the state-of-the-art method STARFlow (gFID 2.40). Moreover, SimFlow can be seamlessly integrated with the end-to-end representation alignment (REPA-E) method and achieves an improved gFID of 1.91, setting a new state of the art among NFs.

