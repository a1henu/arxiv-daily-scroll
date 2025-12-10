---
layout: default
title: DINO-BOLDNet: A DINOv3-Guided Multi-Slice Attention Network for T1-to-BOLD Generation
---

# DINO-BOLDNet: A DINOv3-Guided Multi-Slice Attention Network for T1-to-BOLD Generation
**arXiv**：[2512.08337v1](https://arxiv.org/abs/2512.08337) · [PDF](https://arxiv.org/pdf/2512.08337.pdf)  
**作者**：Jianwei Wang, Qing Wang, Menglan Ruan, Rongjun Ge, Chunfeng Yang, Yang Chen, Chunming Xie  

**一句话要点**：提出DINO-BOLDNet，利用DINOv3引导的多切片注意力网络从T1加权图像生成BOLD图像，以恢复缺失功能信息。

**关键词**：T1到BOLD生成, 自监督Transformer引导, 多切片注意力, 结构到功能映射, 医学图像生成

## 3 点简述
- 核心问题：当BOLD图像损坏或缺失时，从T1加权图像生成BOLD图像以支持下游任务。
- 方法要点：结合冻结的DINOv3编码器提取切片内结构表示，使用切片注意力模块融合跨切片上下文信息，并通过多尺度解码器恢复功能对比度。
- 实验或效果：在248名受试者的临床数据集上，PSNR和MS-SSIM指标优于条件GAN基线，首次实现从T1加权图像直接生成平均BOLD图像。

## 摘要（原文）

> Generating BOLD images from T1w images offers a promising solution for recovering missing BOLD information and enabling downstream tasks when BOLD images are corrupted or unavailable. Motivated by this, we propose DINO-BOLDNet, a DINOv3-guided multi-slice attention framework that integrates a frozen self-supervised DINOv3 encoder with a lightweight trainable decoder. The model uses DINOv3 to extract within-slice structural representations, and a separate slice-attention module to fuse contextual information across neighboring slices. A multi-scale generation decoder then restores fine-grained functional contrast, while a DINO-based perceptual loss encourages structural and textural consistency between predictions and ground-truth BOLD in the transformer feature space. Experiments on a clinical dataset of 248 subjects show that DINO-BOLDNet surpasses a conditional GAN baseline in both PSNR and MS-SSIM. To our knowledge, this is the first framework capable of generating mean BOLD images directly from T1w images, highlighting the potential of self-supervised transformer guidance for structural-to-functional mapping.

