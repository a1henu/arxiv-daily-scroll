---
layout: default
title: SUPER Decoder Block for Reconstruction-Aware U-Net Variants
---

# SUPER Decoder Block for Reconstruction-Aware U-Net Variants
**arXiv**：[2511.11015v1](https://arxiv.org/abs/2511.11015) · [PDF](https://arxiv.org/pdf/2511.11015.pdf)  
**作者**：Siheon Joo, Hongjo Kim  

**一句话要点**：提出SUPER解码器块以解决U-Net变体在逆问题中的信息丢失问题

**关键词**：U-Net变体, 逆问题, 小波重构, 解码器块, 高频细节恢复, 即插即用模块

## 3 点简述
- U-Net变体在逆问题中因信息丢失难以恢复高频细节
- 利用小波完美重构特性选择性抑制冗余特征，作为即插即用模块
- 实验在裂缝分割和图像去噪中提升高频保真度和全局一致性

## 摘要（原文）

> Skip-connected encoder-decoder architectures (U-Net variants) are widely adopted for inverse problems but still suffer from information loss, limiting recovery of fine high-frequency details. We present Selectively Suppressed Perfect Reconstruction (SUPER), which exploits the perfect reconstruction (PR) property of wavelets to prevent information degradation while selectively suppressing (SS) redundant features. Free from rigid framelet constraints, SUPER serves as a plug-and-play decoder block for diverse U-Net variants, eliminating their intrinsic reconstruction bottlenecks and enhancing representational richness. Experiments across diverse crack benchmarks, including state-of-the-art (SOTA) models, demonstrate the structural potential of the proposed SUPER Decoder Block. Maintaining comparable computational cost, SUPER enriches representational diversity through increased parameterization. In small-scale in-domain experiments on the CrackVision12K dataset, SUPER markedly improves thin-crack segmentation performance, particularly for cracks narrower than 4 px, underscoring its advantage in high-frequency dominant settings. In smartphone image denoising on SIDD, where low-frequency components prevail, SUPER still achieves a moderate gain in PSNR, confirming its robustness across low- and high-frequency regimes. These results validate its plug-and-play generality across U-Net variants, achieving high-frequency fidelity and global coherence within a unified, reconstruction-aware framework.

