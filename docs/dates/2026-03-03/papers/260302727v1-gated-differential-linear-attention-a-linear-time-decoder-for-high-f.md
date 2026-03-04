---
layout: default
title: Gated Differential Linear Attention: A Linear-Time Decoder for High-Fidelity Medical Segmentation
---

# Gated Differential Linear Attention: A Linear-Time Decoder for High-Fidelity Medical Segmentation
**arXiv**：[2603.02727v1](https://arxiv.org/abs/2603.02727) · [PDF](https://arxiv.org/pdf/2603.02727.pdf)  
**作者**：Hongbo Zheng, Afshin Bozorgpour, Dorit Merhof, Minjia Zhang  

**一句话要点**：提出PVT-GDLA解码器，以线性时间实现高保真医学图像分割。

**关键词**：医学图像分割, 线性注意力, Transformer解码器, 差分注意力, 门控机制, 资源受限部署

## 3 点简述
- 医学分割需平衡全局依赖与效率，现有方法存在计算成本高或边界模糊问题。
- 核心GDLA通过差分线性注意力与门控机制，抑制噪声并增强上下文，保持线性复杂度。
- 在多种医学影像基准上，PVT-GDLA以较低计算成本达到先进精度，适用于临床部署。

## 摘要（原文）

> Medical image segmentation requires models that preserve fine anatomical boundaries while remaining efficient for clinical deployment. While transformers capture long-range dependencies, they suffer from quadratic attention cost and large data requirements, whereas CNNs are compute-friendly yet struggle with global reasoning. Linear attention offers $\mathcal{O}(N)$ scaling, but often exhibits training instability and attention dilution, yielding diffuse maps. We introduce PVT-GDLA, a decoder-centric Transformer that restores sharp, long-range dependencies at linear time. Its core, Gated Differential Linear Attention (GDLA), computes two kernelized attention paths on complementary query/key subspaces and subtracts them with a learnable, channel-wise scale to cancel common-mode noise and amplify relevant context. A lightweight, head-specific gate injects nonlinearity and input-adaptive sparsity, mitigating attention sink, and a parallel local token-mixing branch with depthwise convolution strengthens neighboring-token interactions, improving boundary fidelity, all while retaining $\mathcal{O}(N)$ complexity and low parameter overhead. Coupled with a pretrained Pyramid Vision Transformer (PVT) encoder, PVT-GDLA achieves state-of-the-art accuracy across CT, MRI, ultrasound, and dermoscopy benchmarks under equal training budgets, with comparable parameters but lower FLOPs than CNN-, Transformer-, hybrid-, and linear-attention baselines. PVT-GDLA provides a practical path to fast, scalable, high-fidelity medical segmentation in clinical environments and other resource-constrained settings.

