---
layout: default
title: 3D Modality-Aware Pre-training for Vision-Language Model in MRI Multi-organ Abnormality Detection
---

# 3D Modality-Aware Pre-training for Vision-Language Model in MRI Multi-organ Abnormality Detection
**arXiv**：[2602.23652v1](https://arxiv.org/abs/2602.23652) · [PDF](https://arxiv.org/pdf/2602.23652.pdf)  
**作者**：Haowen Zhu, Ning Yin, Xiaogen Zhou  

**一句话要点**：提出MedMAP框架以解决3D MRI多器官异常检测中的模态感知视觉-语言对齐与跨模态特征融合问题。

**关键词**：3D MRI, 视觉-语言模型, 模态感知预训练, 多器官异常检测, 跨模态对齐

## 3 点简述
- 核心问题：多器官医学影像中视觉-语言模型面临模态特定对齐与跨模态特征融合挑战。
- 方法要点：通过模态感知预训练阶段隐式捕获联合模态分布，增强视觉与文本表示对齐。
- 实验或效果：在MedMoM-MRI3D数据集上，MedMAP显著优于现有视觉-语言模型。

## 摘要（原文）

> Vision-language models (VLMs) show strong potential for complex diagnostic tasks in medical imaging. However, applying VLMs to multi-organ medical imaging introduces two principal challenges: (1) modality-specific vision-language alignment and (2) cross-modal feature fusion. In this work, we propose MedMAP, a Medical Modality-Aware Pretraining framework that enhances vision-language representation learning in 3D MRI. MedMAP comprises a modality-aware vision-language alignment stage and a fine-tuning stage for multi-organ abnormality detection. During the pre-training stage, the modality-aware encoders implicitly capture the joint modality distribution and improve alignment between visual and textual representations. We then fine-tune the pre-trained vision encoders (while keeping the text encoder frozen) for downstream tasks. To this end, we curated MedMoM-MRI3D, comprising 7,392 3D MRI volume-report pairs spanning twelve MRI modalities and nine abnormalities tailored for various 3D medical analysis tasks. Extensive experiments on MedMoM-MRI3D demonstrate that MedMAP significantly outperforms existing VLMs in 3D MRI-based multi-organ abnormality detection. Our code is available at https://github.com/RomantiDr/MedMAP.

