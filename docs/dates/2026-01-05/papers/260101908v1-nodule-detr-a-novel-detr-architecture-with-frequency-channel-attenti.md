---
layout: default
title: Nodule-DETR: A Novel DETR Architecture with Frequency-Channel Attention for Ultrasound Thyroid Nodule Detection
---

# Nodule-DETR: A Novel DETR Architecture with Frequency-Channel Attention for Ultrasound Thyroid Nodule Detection
**arXiv**：[2601.01908v1](https://arxiv.org/abs/2601.01908) · [PDF](https://arxiv.org/pdf/2601.01908.pdf)  
**作者**：Jingjing Wang, Qianglin Liu, Zhuo Xiao, Xinning Yao, Bo Liu, Lu Li, Lijuan Niu, Fugen Zhou  

**一句话要点**：提出Nodule-DETR，结合频率通道注意力，用于超声甲状腺结节检测。

**关键词**：甲状腺结节检测, 检测变换器, 频率通道注意力, 多尺度特征融合, 超声图像分析, 计算机辅助诊断

## 3 点简述
- 核心问题：超声图像对比度低、结节边界模糊，影响甲状腺结节检测准确性。
- 方法要点：引入MSFCA模块增强低对比度特征，HFF模块融合多尺度信息，MSDA模块捕捉小且不规则结节。
- 实验或效果：在真实临床数据集上，mAP@0.5:0.95提升0.149，达到先进性能，代码已开源。

## 摘要（原文）

> Thyroid cancer is the most common endocrine malignancy, and its incidence is rising globally. While ultrasound is the preferred imaging modality for detecting thyroid nodules, its diagnostic accuracy is often limited by challenges such as low image contrast and blurred nodule boundaries. To address these issues, we propose Nodule-DETR, a novel detection transformer (DETR) architecture designed for robust thyroid nodule detection in ultrasound images. Nodule-DETR introduces three key innovations: a Multi-Spectral Frequency-domain Channel Attention (MSFCA) module that leverages frequency analysis to enhance features of low-contrast nodules; a Hierarchical Feature Fusion (HFF) module for efficient multi-scale integration; and Multi-Scale Deformable Attention (MSDA) to flexibly capture small and irregularly shaped nodules. We conducted extensive experiments on a clinical dataset of real-world thyroid ultrasound images. The results demonstrate that Nodule-DETR achieves state-of-the-art performance, outperforming the baseline model by a significant margin of 0.149 in mAP@0.5:0.95. The superior accuracy of Nodule-DETR highlights its significant potential for clinical application as an effective tool in computer-aided thyroid diagnosis. The code of work is available at https://github.com/wjj1wjj/Nodule-DETR.

