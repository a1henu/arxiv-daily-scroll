---
layout: default
title: MOS: Mitigating Optical-SAR Modality Gap for Cross-Modal Ship Re-Identification
---

# MOS: Mitigating Optical-SAR Modality Gap for Cross-Modal Ship Re-Identification
**arXiv**：[2512.03404v1](https://arxiv.org/abs/2512.03404) · [PDF](https://arxiv.org/pdf/2512.03404.pdf)  
**作者**：Yujian Zhao, Hankun Liu, Guanglin Niu  

**一句话要点**：提出MOS框架以缓解光学与SAR模态差异，实现跨模态船舶重识别

**关键词**：跨模态重识别, 光学-SAR模态对齐, 船舶识别, 扩散模型, 特征融合

## 3 点简述
- 核心问题：光学与SAR图像间模态差异大，阻碍跨模态船舶重识别。
- 方法要点：结合模态一致表示学习和跨模态数据生成与特征融合，对齐特征分布。
- 实验或效果：在HOSS数据集上显著超越现有方法，R1准确率提升最高达16.4%。

## 摘要（原文）

> Cross-modal ship re-identification (ReID) between optical and synthetic aperture radar (SAR) imagery has recently emerged as a critical yet underexplored task in maritime intelligence and surveillance. However, the substantial modality gap between optical and SAR images poses a major challenge for robust identification. To address this issue, we propose MOS, a novel framework designed to mitigate the optical-SAR modality gap and achieve modality-consistent feature learning for optical-SAR cross-modal ship ReID. MOS consists of two core components: (1) Modality-Consistent Representation Learning (MCRL) applies denoise SAR image procession and a class-wise modality alignment loss to align intra-identity feature distributions across modalities. (2) Cross-modal Data Generation and Feature fusion (CDGF) leverages a brownian bridge diffusion model to synthesize cross-modal samples, which are subsequently fused with original features during inference to enhance alignment and discriminability. Extensive experiments on the HOSS ReID dataset demonstrate that MOS significantly surpasses state-of-the-art methods across all evaluation protocols, achieving notable improvements of +3.0%, +6.2%, and +16.4% in R1 accuracy under the ALL to ALL, Optical to SAR, and SAR to Optical settings, respectively. The code and trained models will be released upon publication.

