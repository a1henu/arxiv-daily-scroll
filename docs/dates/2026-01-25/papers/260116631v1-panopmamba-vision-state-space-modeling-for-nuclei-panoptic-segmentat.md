---
layout: default
title: PanopMamba: Vision State Space Modeling for Nuclei Panoptic Segmentation
---

# PanopMamba: Vision State Space Modeling for Nuclei Panoptic Segmentation
**arXiv**：[2601.16631v1](https://arxiv.org/abs/2601.16631) · [PDF](https://arxiv.org/pdf/2601.16631.pdf)  
**作者**：Ming Kang, Fung Fung Ting, Raphaël C. -W. Phan, Zongyuan Ge, Chee-Ming Ting  

**一句话要点**：提出PanopMamba，结合Mamba与Transformer，通过状态空间建模增强特征融合，用于组织病理图像中的细胞全景分割。

**关键词**：全景分割, 状态空间模型, 细胞分割, 组织病理图像, 特征融合, 评估指标

## 3 点简述
- 核心问题：细胞全景分割面临小目标检测、边界模糊和类别不平衡等挑战。
- 方法要点：设计多尺度Mamba骨干和基于状态空间模型的融合网络，实现高效长程感知和特征增强。
- 实验或效果：在MoNuSAC2020和NuInsSeg数据集上优于现有方法，并引入新评估指标以减少偏差。

## 摘要（原文）

> Nuclei panoptic segmentation supports cancer diagnostics by integrating both semantic and instance segmentation of different cell types to analyze overall tissue structure and individual nuclei in histopathology images. Major challenges include detecting small objects, handling ambiguous boundaries, and addressing class imbalance. To address these issues, we propose PanopMamba, a novel hybrid encoder-decoder architecture that integrates Mamba and Transformer with additional feature-enhanced fusion via state space modeling. We design a multiscale Mamba backbone and a State Space Model (SSM)-based fusion network to enable efficient long-range perception in pyramid features, thereby extending the pure encoder-decoder framework while facilitating information sharing across multiscale features of nuclei. The proposed SSM-based feature-enhanced fusion integrates pyramid feature networks and dynamic feature enhancement across different spatial scales, enhancing the feature representation of densely overlapping nuclei in both semantic and spatial dimensions. To the best of our knowledge, this is the first Mamba-based approach for panoptic segmentation. Additionally, we introduce alternative evaluation metrics, including image-level Panoptic Quality ($i$PQ), boundary-weighted PQ ($w$PQ), and frequency-weighted PQ ($fw$PQ), which are specifically designed to address the unique challenges of nuclei segmentation and thereby mitigate the potential bias inherent in vanilla PQ. Experimental evaluations on two multiclass nuclei segmentation benchmark datasets, MoNuSAC2020 and NuInsSeg, demonstrate the superiority of PanopMamba for nuclei panoptic segmentation over state-of-the-art methods. Consequently, the robustness of PanopMamba is validated across various metrics, while the distinctiveness of PQ variants is also demonstrated. Code is available at https://github.com/mkang315/PanopMamba.

