---
layout: default
title: PADM: A Physics-aware Diffusion Model for Attenuation Correction
---

# PADM: A Physics-aware Diffusion Model for Attenuation Correction
**arXiv**：[2511.06948v1](https://arxiv.org/abs/2511.06948) · [PDF](https://arxiv.org/pdf/2511.06948.pdf)  
**作者**：Trung Kien Pham, Hoang Minh Vu, Anh Duc Chu, Dac Thai Nguyen, Trung Thanh Nguyen, Thao Nguyen Truong, Mai Hong Son, Thanh Trung Nguyen, Phi Le Nguyen  

**一句话要点**：提出PADM扩散模型以解决心脏SPECT成像中的衰减伪影问题

**关键词**：心脏SPECT成像, 衰减校正, 扩散模型, 师生蒸馏, 物理先验, 生成模型

## 3 点简述
- 心脏SPECT成像中衰减伪影影响诊断准确性，混合SPECT/CT系统成本高且辐射大
- PADM结合物理先验和师生蒸馏，仅需非衰减校正输入进行伪影校正
- 实验显示PADM在定量指标和视觉评估上优于现有生成模型

## 摘要（原文）

> Attenuation artifacts remain a significant challenge in cardiac Myocardial
> Perfusion Imaging (MPI) using Single-Photon Emission Computed Tomography
> (SPECT), often compromising diagnostic accuracy and reducing clinical
> interpretability. While hybrid SPECT/CT systems mitigate these artifacts
> through CT-derived attenuation maps, their high cost, limited accessibility,
> and added radiation exposure hinder widespread clinical adoption. In this
> study, we propose a novel CT-free solution to attenuation correction in cardiac
> SPECT. Specifically, we introduce Physics-aware Attenuation Correction
> Diffusion Model (PADM), a diffusion-based generative method that incorporates
> explicit physics priors via a teacher--student distillation mechanism. This
> approach enables attenuation artifact correction using only
> Non-Attenuation-Corrected (NAC) input, while still benefiting from
> physics-informed supervision during training. To support this work, we also
> introduce CardiAC, a comprehensive dataset comprising 424 patient studies with
> paired NAC and Attenuation-Corrected (AC) reconstructions, alongside
> high-resolution CT-based attenuation maps. Extensive experiments demonstrate
> that PADM outperforms state-of-the-art generative models, delivering superior
> reconstruction fidelity across both quantitative metrics and visual assessment.

