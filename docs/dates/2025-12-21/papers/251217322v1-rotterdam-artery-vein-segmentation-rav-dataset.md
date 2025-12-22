---
layout: default
title: Rotterdam artery-vein segmentation (RAV) dataset
---

# Rotterdam artery-vein segmentation (RAV) dataset
**arXiv**：[2512.17322v1](https://arxiv.org/abs/2512.17322) · [PDF](https://arxiv.org/pdf/2512.17322.pdf)  
**作者**：Jose Vargas Quiros, Bart Liefers, Karin van Garderen, Jeroen Vermeulen, Eyened Reading Center, Caroline Klaver  

**一句话要点**：提出Rotterdam动脉-静脉分割数据集，支持眼科血管分析机器学习算法的开发与评估。

**关键词**：眼底图像分割, 动脉-静脉标注, 机器学习数据集, 眼科血管分析, 连通性验证

## 3 点简述
- 核心问题：缺乏高质量、多样化的眼底图像动脉-静脉分割数据集，限制机器学习模型在真实世界条件下的泛化能力。
- 方法要点：从Rotterdam研究中采样图像，使用自定义界面进行分层标注，并通过连通性验证工具确保分割质量。
- 实验或效果：数据集包含1024x1024像素PNG图像，涵盖原始、对比度增强和RGB编码掩码，支持在图像质量变化下的稳健基准测试。

## 摘要（原文）

> Purpose: To provide a diverse, high-quality dataset of color fundus images (CFIs) with detailed artery-vein (A/V) segmentation annotations, supporting the development and evaluation of machine learning algorithms for vascular analysis in ophthalmology.
>   Methods: CFIs were sampled from the longitudinal Rotterdam Study (RS), encompassing a wide range of ages, devices, and capture conditions. Images were annotated using a custom interface that allowed graders to label arteries, veins, and unknown vessels on separate layers, starting from an initial vessel segmentation mask. Connectivity was explicitly verified and corrected using connected component visualization tools.
>   Results: The dataset includes 1024x1024-pixel PNG images in three modalities: original RGB fundus images, contrast-enhanced versions, and RGB-encoded A/V masks. Image quality varied widely, including challenging samples typically excluded by automated quality assessment systems, but judged to contain valuable vascular information.
>   Conclusion: This dataset offers a rich and heterogeneous source of CFIs with high-quality segmentations. It supports robust benchmarking and training of machine learning models under real-world variability in image quality and acquisition settings.
>   Translational Relevance: By including connectivity-validated A/V masks and diverse image conditions, this dataset enables the development of clinically applicable, generalizable machine learning tools for retinal vascular analysis, potentially improving automated screening and diagnosis of systemic and ocular diseases.

