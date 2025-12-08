---
layout: default
title: UniFS: Unified Multi-Contrast MRI Reconstruction via Frequency-Spatial Fusion
---

# UniFS: Unified Multi-Contrast MRI Reconstruction via Frequency-Spatial Fusion
**arXiv**：[2512.05481v1](https://arxiv.org/abs/2512.05481) · [PDF](https://arxiv.org/pdf/2512.05481.pdf)  
**作者**：Jialin Li, Yiwei Ren, Kai Pan, Dong Wei, Pujin Cheng, Xian Wu, Xiaoying Tang  

**一句话要点**：提出UniFS模型以解决多对比MRI重建中泛化性差和频率信息利用不足的问题。

**关键词**：多对比MRI重建, 频率-空间融合, 自适应提示学习, k空间欠采样, 泛化性提升, 医学图像处理

## 3 点简述
- 现有方法需为不同k空间欠采样模式单独训练模型，泛化性受限。
- UniFS通过频率-空间融合模块和自适应提示学习，统一处理多种欠采样模式。
- 在BraTS和HCP数据集上，UniFS在未见模式中实现先进性能，代码已开源。

## 摘要（原文）

> Recently, Multi-Contrast MR Reconstruction (MCMR) has emerged as a hot research topic that leverages high-quality auxiliary modalities to reconstruct undersampled target modalities of interest. However, existing methods often struggle to generalize across different k-space undersampling patterns, requiring the training of a separate model for each specific pattern, which limits their practical applicability. To address this challenge, we propose UniFS, a Unified Frequency-Spatial Fusion model designed to handle multiple k-space undersampling patterns for MCMR tasks without any need for retraining. UniFS integrates three key modules: a Cross-Modal Frequency Fusion module, an Adaptive Mask-Based Prompt Learning module, and a Dual-Branch Complementary Refinement module. These modules work together to extract domain-invariant features from diverse k-space undersampling patterns while dynamically adapt to their own variations. Another limitation of existing MCMR methods is their tendency to focus solely on spatial information while neglect frequency characteristics, or extract only shallow frequency features, thus failing to fully leverage complementary cross-modal frequency information. To relieve this issue, UniFS introduces an adaptive prompt-guided frequency fusion module for k-space learning, significantly enhancing the model's generalization performance. We evaluate our model on the BraTS and HCP datasets with various k-space undersampling patterns and acceleration factors, including previously unseen patterns, to comprehensively assess UniFS's generalizability. Experimental results across multiple scenarios demonstrate that UniFS achieves state-of-the-art performance. Our code is available at https://github.com/LIKP0/UniFS.

