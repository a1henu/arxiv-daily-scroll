---
layout: default
title: One-step Latent-free Image Generation with Pixel Mean Flows
---

# One-step Latent-free Image Generation with Pixel Mean Flows
**arXiv**：[2601.22158v1](https://arxiv.org/abs/2601.22158) · [PDF](https://arxiv.org/pdf/2601.22158.pdf)  
**作者**：Yiyang Lu, Susie Lu, Qiao Sun, Hanhong Zhao, Zhicheng Jiang, Xianbang Wang, Tianhong Li, Zhengyang Geng, Kaiming He  

**一句话要点**：提出像素均值流以在图像生成中实现一步无潜在空间采样

**关键词**：图像生成, 一步采样, 无潜在空间, 均值流, 扩散模型, 流模型

## 3 点简述
- 核心问题：现有扩散/流模型依赖多步采样和潜在空间，阻碍高效图像生成。
- 方法要点：设计网络输出为图像流形预测，损失基于速度空间的均值流，通过简单变换连接两者。
- 实验或效果：在ImageNet 256x256和512x256分辨率上实现一步生成，FID分数分别为2.22和2.48。

## 摘要（原文）

> Modern diffusion/flow-based models for image generation typically exhibit two core characteristics: (i) using multi-step sampling, and (ii) operating in a latent space. Recent advances have made encouraging progress on each aspect individually, paving the way toward one-step diffusion/flow without latents. In this work, we take a further step towards this goal and propose "pixel MeanFlow" (pMF). Our core guideline is to formulate the network output space and the loss space separately. The network target is designed to be on a presumed low-dimensional image manifold (i.e., x-prediction), while the loss is defined via MeanFlow in the velocity space. We introduce a simple transformation between the image manifold and the average velocity field. In experiments, pMF achieves strong results for one-step latent-free generation on ImageNet at 256x256 resolution (2.22 FID) and 512x512 resolution (2.48 FID), filling a key missing piece in this regime. We hope that our study will further advance the boundaries of diffusion/flow-based generative models.

