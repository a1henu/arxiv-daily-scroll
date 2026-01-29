---
layout: default
title: RAW-Flow: Advancing RGB-to-RAW Image Reconstruction with Deterministic Latent Flow Matching
---

# RAW-Flow: Advancing RGB-to-RAW Image Reconstruction with Deterministic Latent Flow Matching
**arXiv**：[2601.20364v1](https://arxiv.org/abs/2601.20364) · [PDF](https://arxiv.org/pdf/2601.20364.pdf)  
**作者**：Zhen Liu, Diedong Feng, Hai Jiang, Liaoyuan Zeng, Hao Wang, Chaoyu Feng, Lei Lei, Bing Zeng, Shuaicheng Liu  

**一句话要点**：提出RAW-Flow框架，通过确定性潜在流匹配解决RGB到RAW图像重建中的细节不一致和颜色偏差问题。

**关键词**：RGB到RAW重建, 流匹配, 潜在传输, 图像信号处理逆建模, 生成模型, 跨尺度特征引导

## 3 点简述
- 核心问题：RGB到RAW重建因逆ISP不适定性和RGB图像量化信息损失，导致细节不一致和颜色偏差。
- 方法要点：将重建任务重构为确定性潜在传输问题，利用流匹配学习潜在空间向量场，并引入跨尺度上下文引导模块和双域潜在自编码器。
- 实验或效果：在定量和视觉评估中优于现有方法，实现高保真重建。

## 摘要（原文）

> RGB-to-RAW reconstruction, or the reverse modeling of a camera Image Signal Processing (ISP) pipeline, aims to recover high-fidelity RAW data from RGB images. Despite notable progress, existing learning-based methods typically treat this task as a direct regression objective and struggle with detail inconsistency and color deviation, due to the ill-posed nature of inverse ISP and the inherent information loss in quantized RGB images. To address these limitations, we pioneer a generative perspective by reformulating RGB-to-RAW reconstruction as a deterministic latent transport problem and introduce a novel framework named RAW-Flow, which leverages flow matching to learn a deterministic vector field in latent space, to effectively bridge the gap between RGB and RAW representations and enable accurate reconstruction of structural details and color information. To further enhance latent transport, we introduce a cross-scale context guidance module that injects hierarchical RGB features into the flow estimation process. Moreover, we design a dual-domain latent autoencoder with a feature alignment constraint to support the proposed latent transport framework, which jointly encodes RGB and RAW inputs while promoting stable training and high-fidelity reconstruction. Extensive experiments demonstrate that RAW-Flow outperforms state-of-the-art approaches both quantitatively and visually.

