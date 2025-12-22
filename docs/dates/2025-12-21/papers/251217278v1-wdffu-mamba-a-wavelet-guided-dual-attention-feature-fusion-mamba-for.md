---
layout: default
title: WDFFU-Mamba: A Wavelet-guided Dual-attention Feature Fusion Mamba for Breast Tumor Segmentation in Ultrasound Images
---

# WDFFU-Mamba: A Wavelet-guided Dual-attention Feature Fusion Mamba for Breast Tumor Segmentation in Ultrasound Images
**arXiv**：[2512.17278v1](https://arxiv.org/abs/2512.17278) · [PDF](https://arxiv.org/pdf/2512.17278.pdf)  
**作者**：Guoping Cai, Houjin Chen, Yanfeng Li, Jia Sun, Ziwei Chen, Qingzi Geng  

**一句话要点**：提出WDFFU-Mamba模型，通过小波去噪与双注意力融合提升乳腺超声图像肿瘤分割准确性。

**关键词**：乳腺超声图像分割, 小波去噪, 注意力机制, 特征融合, Mamba架构, 医学图像分析

## 3 点简述
- 核心问题：乳腺超声图像分割受斑点噪声、成像伪影、不规则病灶形态和模糊边界影响，导致准确性低。
- 方法要点：结合小波去噪高频引导特征模块和双注意力特征融合模块，在U形Mamba架构中增强特征表示与上下文一致性。
- 实验或效果：在两个公共数据集上验证，Dice系数和HD95指标优于现有方法，展现高准确性和泛化能力。

## 摘要（原文）

> Breast ultrasound (BUS) image segmentation plays a vital role in assisting clinical diagnosis and early tumor screening. However, challenges such as speckle noise, imaging artifacts, irregular lesion morphology, and blurred boundaries severely hinder accurate segmentation. To address these challenges, this work aims to design a robust and efficient model capable of automatically segmenting breast tumors in BUS images.We propose a novel segmentation network named WDFFU-Mamba, which integrates wavelet-guided enhancement and dual-attention feature fusion within a U-shaped Mamba architecture. A Wavelet-denoised High-Frequency-guided Feature (WHF) module is employed to enhance low-level representations through noise-suppressed high-frequency cues. A Dual Attention Feature Fusion (DAFF) module is also introduced to effectively merge skip-connected and semantic features, improving contextual consistency.Extensive experiments on two public BUS datasets demonstrate that WDFFU-Mamba achieves superior segmentation accuracy, significantly outperforming existing methods in terms of Dice coefficient and 95th percentile Hausdorff Distance (HD95).The combination of wavelet-domain enhancement and attention-based fusion greatly improves both the accuracy and robustness of BUS image segmentation, while maintaining computational efficiency.The proposed WDFFU-Mamba model not only delivers strong segmentation performance but also exhibits desirable generalization ability across datasets, making it a promising solution for real-world clinical applications in breast tumor ultrasound analysis.

