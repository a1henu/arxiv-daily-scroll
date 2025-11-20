---
layout: default
title: Multi-Stage Residual-Aware Unsupervised Deep Learning Framework for Consistent Ultrasound Strain Elastography
---

# Multi-Stage Residual-Aware Unsupervised Deep Learning Framework for Consistent Ultrasound Strain Elastography
**arXiv**：[2511.15640v1](https://arxiv.org/abs/2511.15640) · [PDF](https://arxiv.org/pdf/2511.15640.pdf)  
**作者**：Shourov Joarder, Tushar Talukder Showrav, Md. Kamrul Hasan  

**一句话要点**：提出MUSSE-Net多阶段无监督深度学习框架以解决超声应变弹性成像中的噪声和不一致性问题

**关键词**：超声应变弹性成像, 无监督深度学习, 多阶段框架, 残差感知, 应变估计, 噪声抑制

## 3 点简述
- 核心问题：超声应变弹性成像受组织去相关噪声、真值稀缺和变形条件下应变估计不一致限制
- 方法要点：采用多阶段残差感知架构，结合多流编码器-解码器和一致性损失提升稳定性
- 实验或效果：在模拟和临床数据集上实现高信噪比和对比度，优于现有无监督方法

## 摘要（原文）

> Ultrasound Strain Elastography (USE) is a powerful non-invasive imaging technique for assessing tissue mechanical properties, offering crucial diagnostic value across diverse clinical applications. However, its clinical application remains limited by tissue decorrelation noise, scarcity of ground truth, and inconsistent strain estimation under different deformation conditions. Overcoming these barriers, we propose MUSSE-Net, a residual-aware, multi-stage unsupervised sequential deep learning framework designed for robust and consistent strain estimation. At its backbone lies our proposed USSE-Net, an end-to-end multi-stream encoder-decoder architecture that parallelly processes pre- and post-deformation RF sequences to estimate displacement fields and axial strains. The novel architecture incorporates Context-Aware Complementary Feature Fusion (CACFF)-based encoder with Tri-Cross Attention (TCA) bottleneck with a Cross-Attentive Fusion (CAF)-based sequential decoder. To ensure temporal coherence and strain stability across varying deformation levels, this architecture leverages a tailored consistency loss. Finally, with the MUSSE-Net framework, a secondary residual refinement stage further enhances accuracy and suppresses noise. Extensive validation on simulation, in vivo, and private clinical datasets from Bangladesh University of Engineering and Technology (BUET) medical center, demonstrates MUSSE-Net's outperformed existing unsupervised approaches. On MUSSE-Net achieves state-of-the-art performance with a target SNR of 24.54, background SNR of 132.76, CNR of 59.81, and elastographic SNR of 9.73 on simulation data. In particular, on the BUET dataset, MUSSE-Net produces strain maps with enhanced lesion-to-background contrast and significant noise suppression yielding clinically interpretable strain patterns.

