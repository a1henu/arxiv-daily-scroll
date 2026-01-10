---
layout: default
title: 3D Conditional Image Synthesis of Left Atrial LGE MRI from Composite Semantic Masks
---

# 3D Conditional Image Synthesis of Left Atrial LGE MRI from Composite Semantic Masks
**arXiv**：[2601.04588v1](https://arxiv.org/abs/2601.04588) · [PDF](https://arxiv.org/pdf/2601.04588.pdf)  
**作者**：Yusri Al-Sanaani, Rebecca Thornhill, Sreeraman Rajan  

**一句话要点**：提出基于复合语义掩码的3D条件生成模型，以增强左心房LGE MRI数据并提升分割性能

**关键词**：3D图像合成, 条件生成模型, 左心房分割, LGE MRI, 数据增强, 医学图像分析

## 3 点简述
- 核心问题：左心房LGE MRI分割数据稀缺，影响心房纤维化量化准确性。
- 方法要点：使用Pix2Pix GAN、SPADE-GAN和SPADE-LDM从复合语义掩码合成3D LGE MRI图像。
- 实验或效果：SPADE-LDM生成图像最真实，FID为4.063；合成数据使LA腔分割Dice分数从0.908提升至0.936。

## 摘要（原文）

> Segmentation of the left atrial (LA) wall and endocardium from late gadolinium-enhanced (LGE) MRI is essential for quantifying atrial fibrosis in patients with atrial fibrillation. The development of accurate machine learning-based segmentation models remains challenging due to the limited availability of data and the complexity of anatomical structures. In this work, we investigate 3D conditional generative models as potential solution for augmenting scarce LGE training data and improving LA segmentation performance. We develop a pipeline to synthesize high-fidelity 3D LGE MRI volumes from composite semantic label maps combining anatomical expert annotations with unsupervised tissue clusters, using three 3D conditional generators (Pix2Pix GAN, SPADE-GAN, and SPADE-LDM). The synthetic images are evaluated for realism and their impact on downstream LA segmentation. SPADE-LDM generates the most realistic and structurally accurate images, achieving an FID of 4.063 and surpassing GAN models, which have FIDs of 40.821 and 7.652 for Pix2Pix and SPADE-GAN, respectively. When augmented with synthetic LGE images, the Dice score for LA cavity segmentation with a 3D U-Net model improved from 0.908 to 0.936, showing a statistically significant improvement (p < 0.05) over the baseline.These findings demonstrate the potential of label-conditioned 3D synthesis to enhance the segmentation of under-represented cardiac structures.

