---
layout: default
title: Diffusion Bridge Networks Simulate Clinical-grade PET from MRI for Dementia Diagnostics
---

# Diffusion Bridge Networks Simulate Clinical-grade PET from MRI for Dementia Diagnostics
**arXiv**：[2510.15556v1](https://arxiv.org/abs/2510.15556) · [PDF](https://arxiv.org/pdf/2510.15556.pdf)  
**作者**：Yitong Li, Ralph Buchert, Benita Schmitz-Koep, Timo Grimmer, Björn Ommer, Dennis M. Hedderich, Igor Yakushev, Christian Wachinger  

**一句话要点**：提出SiM2P扩散桥网络从MRI模拟临床级PET以改进痴呆诊断

**关键词**：扩散桥网络, 医学图像模拟, 痴呆诊断, PET-MRI映射, 临床部署

## 3 点简述
- FDG-PET在痴呆诊断中成本高且难获取，而MRI更普及但诊断准确性有限。
- SiM2P使用3D扩散桥框架学习从MRI和患者信息到PET图像的映射。
- 临床研究显示SiM2P将诊断准确率从75.0%提升至84.7%，并提高诊断确定性。

## 摘要（原文）

> Positron emission tomography (PET) with 18F-Fluorodeoxyglucose (FDG) is an
> established tool in the diagnostic workup of patients with suspected dementing
> disorders. However, compared to the routinely available magnetic resonance
> imaging (MRI), FDG-PET remains significantly less accessible and substantially
> more expensive. Here, we present SiM2P, a 3D diffusion bridge-based framework
> that learns a probabilistic mapping from MRI and auxiliary patient information
> to simulate FDG-PET images of diagnostic quality. In a blinded clinical reader
> study, two neuroradiologists and two nuclear medicine physicians rated the
> original MRI and SiM2P-simulated PET images of patients with Alzheimer's
> disease, behavioral-variant frontotemporal dementia, and cognitively healthy
> controls. SiM2P significantly improved the overall diagnostic accuracy of
> differentiating between three groups from 75.0% to 84.7% (p<0.05). Notably, the
> simulated PET images received higher diagnostic certainty ratings and achieved
> superior interrater agreement compared to the MRI images. Finally, we developed
> a practical workflow for local deployment of the SiM2P framework. It requires
> as few as 20 site-specific cases and only basic demographic information. This
> approach makes the established diagnostic benefits of FDG-PET imaging more
> accessible to patients with suspected dementing disorders, potentially
> improving early detection and differential diagnosis in resource-limited
> settings. Our code is available at https://github.com/Yiiitong/SiM2P.

