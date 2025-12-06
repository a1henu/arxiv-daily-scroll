---
layout: default
title: LatentFM: A Latent Flow Matching Approach for Generative Medical Image Segmentation
---

# LatentFM: A Latent Flow Matching Approach for Generative Medical Image Segmentation
**arXiv**：[2512.04821v1](https://arxiv.org/abs/2512.04821) · [PDF](https://arxiv.org/pdf/2512.04821.pdf)  
**作者**：Huynh Trinh Ngoc, Hoang Anh Nguyen Kim, Toan Nguyen Hai, Long Tran Quoc  

**一句话要点**：提出LatentFM，一种基于潜在流匹配的生成式医学图像分割方法

**关键词**：医学图像分割, 流匹配, 潜在空间建模, 不确定性估计, 生成模型

## 3 点简述
- 核心问题：医学图像分割需高精度和不确定性感知，传统方法可能缺乏多样性或效率。
- 方法要点：使用两个VAE编码图像和掩码到潜在空间，通过条件流匹配生成多样分割输出。
- 实验或效果：在ISIC-2018和CVC-Clinic数据集上验证，实现高精度分割并生成置信度图。

## 摘要（原文）

> Generative models have achieved remarkable progress with the emergence of flow matching (FM). It has demonstrated strong generative capabilities and attracted significant attention as a simulation-free flow-based framework capable of learning exact data densities. Motivated by these advances, we propose LatentFM, a flow-based model operating in the latent space for medical image segmentation. To model the data distribution, we first design two variational autoencoders (VAEs) to encode both medical images and their corresponding masks into a lower-dimensional latent space. We then estimate a conditional velocity field that guides the flow based on the input image. By sampling multiple latent representations, our method synthesizes diverse segmentation outputs whose pixel-wise variance reliably captures the underlying data distribution, enabling both highly accurate and uncertainty-aware predictions. Furthermore, we generate confidence maps that quantify the model certainty, providing clinicians with richer information for deeper analysis. We conduct experiments on two datasets, ISIC-2018 and CVC-Clinic, and compare our method with several prior baselines, including both deterministic and generative approach models. Through comprehensive evaluations, both qualitative and quantitative results show that our approach achieves superior segmentation accuracy while remaining highly efficient in the latent space.

