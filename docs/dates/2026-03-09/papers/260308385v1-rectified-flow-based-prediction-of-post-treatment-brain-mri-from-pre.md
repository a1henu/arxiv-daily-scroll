---
layout: default
title: Rectified flow-based prediction of post-treatment brain MRI from pre-radiotherapy priors for patients with glioma
---

# Rectified flow-based prediction of post-treatment brain MRI from pre-radiotherapy priors for patients with glioma
**arXiv**：[2603.08385v1](https://arxiv.org/abs/2603.08385) · [PDF](https://arxiv.org/pdf/2603.08385.pdf)  
**作者**：Selena Huisman, Nordin Belkacemi, Vera Keil, Joost Verhoeff, Szabolcs David  

**一句话要点**：提出基于校正流的条件图像生成模型，用于预测脑胶质瘤患者放疗后MRI，以支持治疗优化。

**关键词**：条件图像生成, 校正流模型, 脑MRI预测, 放疗剂量规划, 人工智能医疗

## 3 点简述
- 核心问题：脑肿瘤治疗导致复杂结构变化，需通过MRI监测，但传统方法难以实时预测放疗后影像。
- 方法要点：使用校正流模型，以治疗前MRI和放疗剂量图为条件，结合交叉注意力整合时间与化疗数据。
- 实验或效果：模型生成影像在SSIM、PSNR和Dice分数上表现良好，推理速度比DDPM快250倍，支持反事实模拟。

## 摘要（原文）

> Purpose/Objective: Brain tumors result in 20 years of lost life on average. Standard therapies induce complex structural changes in the brain that are monitored through MRI. Recent developments in artificial intelligence (AI) enable conditional multimodal image generation from clinical data. In this study, we investigate AI-driven generation of follow-up MRI in patients with in- tracranial tumors through conditional image generation. This approach enables realistic modeling of post-radiotherapy changes, allowing for treatment optimization. Material/Methods: The public SAILOR dataset of 25 patients was used to create a 2D rectified flow model conditioned on axial slices of pre-treatment MRI and RT dose maps. Cross-attention conditioning was used to incorporate temporal and chemotherapy data. The resulting images were validated with structural similarity index measure (SSIM), peak signal-to-noise ratio (PSNR), Dice scores and Jacobian determinants. Results: The resulting model generates realistic follow-up MRI for any time point, while integrating treatment information. Comparing real versus predicted images, SSIM is 0.88, and PSNR is 22.82. Tissue segmentations from real versus predicted MRI result in a mean Dice-Sørensen coefficient (DSC) of 0.91. The rectified flow (RF) model enables up to 250x faster inference than Denoising Diffusion Probabilistic Models (DDPM). Conclusion: The proposed model generates realistic follow-up MRI in real-time, preserving both semantic and visual fidelity as confirmed by image quality metrics and tissue segmentations. Conditional generation allows counterfactual simulations by varying treatment parameters, producing predicted morphological changes. This capability has potential to support adaptive treatment dose planning and personalized outcome prediction for patients with intracranial tumors.

