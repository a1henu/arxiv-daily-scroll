---
layout: default
title: DB-MSMUNet:Dual Branch Multi-scale Mamba UNet for Pancreatic CT Scans Segmentation
---

# DB-MSMUNet:Dual Branch Multi-scale Mamba UNet for Pancreatic CT Scans Segmentation
**arXiv**：[2601.04676v1](https://arxiv.org/abs/2601.04676) · [PDF](https://arxiv.org/pdf/2601.04676.pdf)  
**作者**：Qiu Guan, Zhiqiang Yang, Dezhang Ye, Yang Chen, Xinli Xu, Ying Tang  

**一句话要点**：提出DB-MSMUNet以解决胰腺CT图像分割中低对比度、模糊边界和小病灶的挑战。

**关键词**：胰腺CT分割, 多尺度Mamba模块, 双解码器架构, 边缘增强, 深度学习, 医学图像分析

## 3 点简述
- 核心问题：胰腺CT分割因组织对比度低、边界模糊、器官形状不规则和病灶小尺寸而困难。
- 方法要点：采用多尺度Mamba编码器和双解码器设计，结合边缘增强路径和多层解码器提升分割精度。
- 实验或效果：在三个数据集上测试，Dice系数达87.59%-89.47%，优于现有方法，验证了泛化能力。

## 摘要（原文）

> Accurate segmentation of the pancreas and its lesions in CT scans is crucial for the precise diagnosis and treatment of pancreatic cancer. However, it remains a highly challenging task due to several factors such as low tissue contrast with surrounding organs, blurry anatomical boundaries, irregular organ shapes, and the small size of lesions. To tackle these issues, we propose DB-MSMUNet (Dual-Branch Multi-scale Mamba UNet), a novel encoder-decoder architecture designed specifically for robust pancreatic segmentation. The encoder is constructed using a Multi-scale Mamba Module (MSMM), which combines deformable convolutions and multi-scale state space modeling to enhance both global context modeling and local deformation adaptation. The network employs a dual-decoder design: the edge decoder introduces an Edge Enhancement Path (EEP) to explicitly capture boundary cues and refine fuzzy contours, while the area decoder incorporates a Multi-layer Decoder (MLD) to preserve fine-grained details and accurately reconstruct small lesions by leveraging multi-scale deep semantic features. Furthermore, Auxiliary Deep Supervision (ADS) heads are added at multiple scales to both decoders, providing more accurate gradient feedback and further enhancing the discriminative capability of multi-scale features. We conduct extensive experiments on three datasets: the NIH Pancreas dataset, the MSD dataset, and a clinical pancreatic tumor dataset provided by collaborating hospitals. DB-MSMUNet achieves Dice Similarity Coefficients of 89.47%, 87.59%, and 89.02%, respectively, outperforming most existing state-of-the-art methods in terms of segmentation accuracy, edge preservation, and robustness across different datasets. These results demonstrate the effectiveness and generalizability of the proposed method for real-world pancreatic CT segmentation tasks.

