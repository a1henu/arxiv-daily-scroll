---
layout: default
title: TriFusion-SR: Joint Tri-Modal Medical Image Fusion and SR
---

# TriFusion-SR: Joint Tri-Modal Medical Image Fusion and SR
**arXiv**：[2603.09702v1](https://arxiv.org/abs/2603.09702) · [PDF](https://arxiv.org/pdf/2603.09702.pdf)  
**作者**：Fayaz Ali Dharejo, Sharif S. M. A., Aiman Khalil, Nachiket Chaudhary, Rizwan Ali Naqvi, Radu Timofte  

**一句话要点**：提出TriFusion-SR框架，通过联合三模态融合与超分辨率解决医学图像分辨率下降和模态差异问题。

**关键词**：医学图像融合, 超分辨率, 小波变换, 条件扩散模型, 多模态学习, 图像增强

## 3 点简述
- 核心问题：多模态医学图像融合因分辨率下降和模态差异受限，现有方法分阶段处理导致伪影和感知质量下降。
- 方法要点：基于小波引导的条件扩散框架，通过频率分解和自适应空间-频率融合实现联合三模态融合与超分辨率。
- 实验或效果：在多个上采样尺度上实现PSNR提升4.8-12.4%，并显著降低RMSE和LPIPS指标。

## 摘要（原文）

> Multimodal medical image fusion facilitates comprehensive diagnosis by aggregating complementary structural and functional information, but its effectiveness is limited by resolution degradation and modality discrepancies. Existing approaches typically perform image fusion and super-resolution (SR) in separate stages, leading to artifacts and degraded perceptual quality. These limitations are further amplified in tri-modal settings that combine anatomical modalities (e.g., MRI, CT) with functional scans (e.g., PET, SPECT) due to pronounced frequency domain imbalances. We propose TriFusionSR, a wavelet-guided conditional diffusion framework for joint tri-modal fusion and SR. The framework explicitly decomposes multimodal features into frequency bands using the 2D Discrete Wavelet Transform, enabling frequency-aware crossmodal interaction. We further introduce a Rectified Wavelet Features (RWF) strategy for latent coefficient calibration, followed by an Adaptive Spatial-Frequency Fusion (ASFF) module with gated channel-spatial attention to enable structure-driven multimodal refinement. Extensive experiments demonstrate state-of-the-art performance, achieving 4.8-12.4% PSNR improvement and substantial reductions in RMSE and LPIPS across multiple upsampling scales.

