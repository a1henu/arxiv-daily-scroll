---
layout: default
title: One-step Latent-free Image Generation with Pixel Mean Flows
---

# One-step Latent-free Image Generation with Pixel Mean Flows
**arXiv**：[2601.22158v1](https://arxiv.org/abs/2601.22158) · [PDF](https://arxiv.org/pdf/2601.22158.pdf)  
**作者**：Yiyang Lu, Susie Lu, Qiao Sun, Hanhong Zhao, Zhicheng Jiang, Xianbang Wang, Tianhong Li, Zhengyang Geng, Kaiming He  

**一句话要点**：提出像素均值流以在无潜空间下实现一步图像生成

**关键词**：图像生成, 一步采样, 无潜空间, 扩散模型, 流模型, 像素均值流

## 3 点简述
- 核心问题：现有扩散/流模型依赖多步采样和潜空间，阻碍高效一步生成
- 方法要点：分离网络输出与损失空间，通过图像流形与速度场变换实现一步预测
- 实验或效果：在ImageNet 256x256和512x256分辨率上取得低FID，验证无潜空间一步生成可行性

## 摘要（原文）

> Modern diffusion/flow-based models for image generation typically exhibit two core characteristics: (i) using multi-step sampling, and (ii) operating in a latent space. Recent advances have made encouraging progress on each aspect individually, paving the way toward one-step diffusion/flow without latents. In this work, we take a further step towards this goal and propose "pixel MeanFlow" (pMF). Our core guideline is to formulate the network output space and the loss space separately. The network target is designed to be on a presumed low-dimensional image manifold (i.e., x-prediction), while the loss is defined via MeanFlow in the velocity space. We introduce a simple transformation between the image manifold and the average velocity field. In experiments, pMF achieves strong results for one-step latent-free generation on ImageNet at 256x256 resolution (2.22 FID) and 512x512 resolution (2.48 FID), filling a key missing piece in this regime. We hope that our study will further advance the boundaries of diffusion/flow-based generative models.

