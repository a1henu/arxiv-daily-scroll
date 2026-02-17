---
layout: default
title: Uncertainty-Aware Vision-Language Segmentation for Medical Imaging
---

# Uncertainty-Aware Vision-Language Segmentation for Medical Imaging
**arXiv**：[2602.14498v1](https://arxiv.org/abs/2602.14498) · [PDF](https://arxiv.org/pdf/2602.14498.pdf)  
**作者**：Aryan Das, Tanishq Rachamalla, Koushik Biswas, Swalpa Kumar Roy, Vinay Kumar Verma  

**一句话要点**：提出不确定性感知视觉语言分割框架，用于医学影像诊断，提升模型可靠性和效率。

**关键词**：医学影像分割, 不确定性建模, 跨模态融合, 视觉语言模型, 计算效率

## 3 点简述
- 核心问题：医学影像分割在图像质量差时存在不确定性，影响诊断精度。
- 方法要点：引入MoDAB和SSMix进行跨模态融合，提出SEU损失联合建模空间、谱和不确定性。
- 实验或效果：在多个公开数据集上验证，性能优于现有方法，计算效率更高。

## 摘要（原文）

> We introduce a novel uncertainty-aware multimodal segmentation framework that leverages both radiological images and associated clinical text for precise medical diagnosis. We propose a Modality Decoding Attention Block (MoDAB) with a lightweight State Space Mixer (SSMix) to enable efficient cross-modal fusion and long-range dependency modelling. To guide learning under ambiguity, we propose the Spectral-Entropic Uncertainty (SEU) Loss, which jointly captures spatial overlap, spectral consistency, and predictive uncertainty in a unified objective. In complex clinical circumstances with poor image quality, this formulation improves model reliability. Extensive experiments on various publicly available medical datasets, QATA-COVID19, MosMed++, and Kvasir-SEG, demonstrate that our method achieves superior segmentation performance while being significantly more computationally efficient than existing State-of-the-Art (SoTA) approaches. Our results highlight the importance of incorporating uncertainty modelling and structured modality alignment in vision-language medical segmentation tasks. Code: https://github.com/arya-domain/UA-VLS

