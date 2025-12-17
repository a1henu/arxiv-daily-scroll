---
layout: default
title: HiFi-Portrait: Zero-shot Identity-preserved Portrait Generation with High-fidelity Multi-face Fusion
---

# HiFi-Portrait: Zero-shot Identity-preserved Portrait Generation with High-fidelity Multi-face Fusion
**arXiv**：[2512.14542v1](https://arxiv.org/abs/2512.14542) · [PDF](https://arxiv.org/pdf/2512.14542.pdf)  
**作者**：Yifang Xu, Benxiang Zhai, Yunzhuo Sun, Ming Li, Yang Li, Sidan Du  

**一句话要点**：提出HiFi-Portrait方法，通过高保真多脸融合实现零样本身份保持肖像生成

**关键词**：身份保持肖像生成, 零样本学习, 多脸融合, 高保真生成, 扩散模型, 面部控制

## 3 点简述
- 现有方法在多参考图像下生成肖像保真度低且属性控制不精确
- 引入面部精炼器和地标生成器获取细粒度特征与3D感知地标，设计HiFi-Net融合特征并对齐地标
- 实验显示在面部相似性和可控性上超越SOTA，兼容SDXL相关工作

## 摘要（原文）

> Recent advancements in diffusion-based technologies have made significant strides, particularly in identity-preserved portrait generation (IPG). However, when using multiple reference images from the same ID, existing methods typically produce lower-fidelity portraits and struggle to customize face attributes precisely. To address these issues, this paper presents HiFi-Portrait, a high-fidelity method for zero-shot portrait generation. Specifically, we first introduce the face refiner and landmark generator to obtain fine-grained multi-face features and 3D-aware face landmarks. The landmarks include the reference ID and the target attributes. Then, we design HiFi-Net to fuse multi-face features and align them with landmarks, which improves ID fidelity and face control. In addition, we devise an automated pipeline to construct an ID-based dataset for training HiFi-Portrait. Extensive experimental results demonstrate that our method surpasses the SOTA approaches in face similarity and controllability. Furthermore, our method is also compatible with previous SDXL-based works.

