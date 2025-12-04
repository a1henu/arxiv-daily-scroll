---
layout: default
title: Label-Efficient Hyperspectral Image Classification via Spectral FiLM Modulation of Low-Level Pretrained Diffusion Features
---

# Label-Efficient Hyperspectral Image Classification via Spectral FiLM Modulation of Low-Level Pretrained Diffusion Features
**arXiv**：[2512.03430v1](https://arxiv.org/abs/2512.03430) · [PDF](https://arxiv.org/pdf/2512.03430.pdf)  
**作者**：Yuzhen Hu, Biplab Banerjee, Saurabh Prasad  

**一句话要点**：提出基于扩散模型预训练特征与光谱FiLM调制的标签高效高光谱图像分类框架

**关键词**：高光谱图像分类, 标签高效学习, 扩散模型, 特征调制, 多模态融合, 遥感图像分析

## 3 点简述
- 高光谱图像分类面临低空间分辨率与稀疏标注的挑战
- 利用冻结扩散模型提取低层空间特征，通过FiLM模块融合光谱信息
- 在稀疏标注下优于现有方法，验证了扩散特征与光谱融合的有效性

## 摘要（原文）

> Hyperspectral imaging (HSI) enables detailed land cover classification, yet low spatial resolution and sparse annotations pose significant challenges. We present a label-efficient framework that leverages spatial features from a frozen diffusion model pretrained on natural images. Our approach extracts low-level representations from high-resolution decoder layers at early denoising timesteps, which transfer effectively to the low-texture structure of HSI. To integrate spectral and spatial information, we introduce a lightweight FiLM-based fusion module that adaptively modulates frozen spatial features using spectral cues, enabling robust multimodal learning under sparse supervision. Experiments on two recent hyperspectral datasets demonstrate that our method outperforms state-of-the-art approaches using only the provided sparse training labels. Ablation studies further highlight the benefits of diffusion-derived features and spectral-aware fusion. Overall, our results indicate that pretrained diffusion models can support domain-agnostic, label-efficient representation learning for remote sensing and broader scientific imaging tasks.

