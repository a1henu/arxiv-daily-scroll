---
layout: default
title: MAUGIF: Mechanism-Aware Unsupervised General Image Fusion via Dual Cross-Image Autoencoders
---

# MAUGIF: Mechanism-Aware Unsupervised General Image Fusion via Dual Cross-Image Autoencoders
**arXiv**：[2511.08272v1](https://arxiv.org/abs/2511.08272) · [PDF](https://arxiv.org/pdf/2511.08272.pdf)  
**作者**：Kunjing Yang, Zhiwei Wang, Minru Bai  

**一句话要点**：提出机制感知无监督通用图像融合方法，通过双交叉图像自编码器解决任务特定与通用策略的平衡问题。

**关键词**：图像融合, 无监督学习, 自编码器, 机制感知, 多模态融合

## 3 点简述
- 现有图像融合方法常忽略不同任务的独特机制，导致任务特定或通用策略不适用。
- 基于双交叉图像自编码器，分类加性和乘性融合机制，选择性注入模态特征。
- 在多种融合任务上实验验证方法有效性和泛化能力，代码已开源。

## 摘要（原文）

> Image fusion aims to integrate structural and complementary information from multi-source images. However, existing fusion methods are often either highly task-specific, or general frameworks that apply uniform strategies across diverse tasks, ignoring their distinct fusion mechanisms. To address this issue, we propose a mechanism-aware unsupervised general image fusion (MAUGIF) method based on dual cross-image autoencoders. Initially, we introduce a classification of additive and multiplicative fusion according to the inherent mechanisms of different fusion tasks. Then, dual encoders map source images into a shared latent space, capturing common content while isolating modality-specific details. During the decoding phase, dual decoders act as feature injectors, selectively reintegrating the unique characteristics of each modality into the shared content for reconstruction. The modality-specific features are injected into the source image in the fusion process, generating the fused image that integrates information from both modalities. The architecture of decoders varies according to their fusion mechanisms, enhancing both performance and interpretability. Extensive experiments are conducted on diverse fusion tasks to validate the effectiveness and generalization ability of our method. The code is available at https://anonymous.4open.science/r/MAUGIF.

