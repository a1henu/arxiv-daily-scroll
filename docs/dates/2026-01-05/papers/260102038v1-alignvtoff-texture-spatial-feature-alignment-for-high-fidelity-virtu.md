---
layout: default
title: AlignVTOFF: Texture-Spatial Feature Alignment for High-Fidelity Virtual Try-Off
---

# AlignVTOFF: Texture-Spatial Feature Alignment for High-Fidelity Virtual Try-Off
**arXiv**：[2601.02038v1](https://arxiv.org/abs/2601.02038) · [PDF](https://arxiv.org/pdf/2601.02038.pdf)  
**作者**：Yihan Zhu, Mengying Ge  

**一句话要点**：提出AlignVTOFF框架，通过纹理-空间特征对齐解决虚拟试穿中高保真平铺服装生成问题

**关键词**：虚拟试穿, 图像生成, 特征对齐, U-Net框架, 纹理保真

## 3 点简述
- 核心问题：现有方法因轻量模块导致纹理衰减，难以保持结构化图案和细粒度细节
- 方法要点：采用并行U-Net框架，结合参考U-Net和TSFA模块，通过混合注意力对齐纹理与空间特征
- 实验或效果：在多种设置下超越先进方法，提升结构真实性和高频细节保真度

## 摘要（原文）

> Virtual Try-Off (VTOFF) is a challenging multimodal image generation task that aims to synthesize high-fidelity flat-lay garments under complex geometric deformation and rich high-frequency textures. Existing methods often rely on lightweight modules for fast feature extraction, which struggles to preserve structured patterns and fine-grained details, leading to texture attenuation during generation.To address these issues, we propose AlignVTOFF, a novel parallel U-Net framework built upon a Reference U-Net and Texture-Spatial Feature Alignment (TSFA). The Reference U-Net performs multi-scale feature extraction and enhances geometric fidelity, enabling robust modeling of deformation while retaining complex structured patterns. TSFA then injects the reference garment features into a frozen denoising U-Net via a hybrid attention design, consisting of a trainable cross-attention module and a frozen self-attention module. This design explicitly aligns texture and spatial cues and alleviates the loss of high-frequency information during the denoising process.Extensive experiments across multiple settings demonstrate that AlignVTOFF consistently outperforms state-of-the-art methods, producing flat-lay garment results with improved structural realism and high-frequency detail fidelity.

