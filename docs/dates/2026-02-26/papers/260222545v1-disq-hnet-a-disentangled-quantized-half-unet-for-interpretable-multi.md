---
layout: default
title: DisQ-HNet: A Disentangled Quantized Half-UNet for Interpretable Multimodal Image Synthesis Applications to Tau-PET Synthesis from T1 and FLAIR MRI
---

# DisQ-HNet: A Disentangled Quantized Half-UNet for Interpretable Multimodal Image Synthesis Applications to Tau-PET Synthesis from T1 and FLAIR MRI
**arXiv**：[2602.22545v1](https://arxiv.org/abs/2602.22545) · [PDF](https://arxiv.org/pdf/2602.22545.pdf)  
**作者**：Agamdeep S. Chopra, Caitlin Neher, Tianyi Ren, Juampablo E. Heras Rivera, Mehmet Kurt  

**一句话要点**：提出DisQ-HNet框架，从T1和FLAIR MRI合成tau-PET，以解决阿尔茨海默病病理标记成本高和可用性有限的问题。

**关键词**：多模态图像合成, 阿尔茨海默病诊断, 向量量化编码, 信息分解, 医学影像分析, tau-PET合成

## 3 点简述
- 核心问题：tau-PET作为阿尔茨海默病病理标记成本高且可用性有限，需基于MRI的替代方案。
- 方法要点：结合PID引导的向量量化编码器分解潜在信息，以及Half-UNet解码器利用结构边缘线索保留解剖细节。
- 实验或效果：在多个基线模型上保持重建保真度，并更好地保留疾病相关信号用于下游任务，如Braak分期和分类。

## 摘要（原文）

> Tau positron emission tomography (tau-PET) provides an in vivo marker of Alzheimer's disease pathology, but cost and limited availability motivate MRI-based alternatives. We introduce DisQ-HNet (DQH), a framework that synthesizes tau-PET from paired T1-weighted and FLAIR MRI while exposing how each modality contributes to the prediction. The method combines (i) a Partial Information Decomposition (PID)-guided, vector-quantized encoder that partitions latent information into redundant, unique, and complementary components, and (ii) a Half-UNet decoder that preserves anatomical detail using pseudo-skip connections conditioned on structural edge cues rather than direct encoder feature reuse. Across multiple baselines (VAE, VQ-VAE, and UNet), DisQ-HNet maintains reconstruction fidelity and better preserves disease-relevant signal for downstream AD tasks, including Braak staging, tau localization, and classification. PID-based Shapley analysis provides modality-specific attribution of synthesized uptake patterns.

