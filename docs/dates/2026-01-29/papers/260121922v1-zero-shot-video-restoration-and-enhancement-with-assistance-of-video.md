---
layout: default
title: Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models
---

# Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models
**arXiv**：[2601.21922v1](https://arxiv.org/abs/2601.21922) · [PDF](https://arxiv.org/pdf/2601.21922.pdf)  
**作者**：Cong Cao, Huanjing Yue, Shangbin Xie, Xin Liu, Jingyu Yang  

**一句话要点**：提出利用视频扩散模型辅助图像方法，以解决零样本视频恢复与增强中的时间闪烁问题。

**关键词**：零样本视频恢复, 视频扩散模型, 时间一致性, 潜在融合, 训练免费方法

## 3 点简述
- 核心问题：基于扩散的零样本图像方法应用于视频时会导致严重时间闪烁。
- 方法要点：通过同源/异源潜在融合和COT策略，结合文本到视频扩散模型提升时间一致性。
- 实验或效果：训练免费，可应用于任何扩散基图像方法，实验显示优越性能。

## 摘要（原文）

> Although diffusion-based zero-shot image restoration and enhancement methods have achieved great success, applying them to video restoration or enhancement will lead to severe temporal flickering. In this paper, we propose the first framework that utilizes the rapidly-developed video diffusion model to assist the image-based method in maintaining more temporal consistency for zero-shot video restoration and enhancement. We propose homologous latents fusion, heterogenous latents fusion, and a COT-based fusion ratio strategy to utilize both homologous and heterogenous text-to-video diffusion models to complement the image method. Moreover, we propose temporal-strengthening post-processing to utilize the image-to-video diffusion model to further improve temporal consistency. Our method is training-free and can be applied to any diffusion-based image restoration and enhancement methods. Experimental results demonstrate the superiority of the proposed method.

