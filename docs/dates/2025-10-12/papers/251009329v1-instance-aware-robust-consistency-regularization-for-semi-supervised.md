---
layout: default
title: Instance-Aware Robust Consistency Regularization for Semi-Supervised Nuclei Instance Segmentation
---

# Instance-Aware Robust Consistency Regularization for Semi-Supervised Nuclei Instance Segmentation
**arXiv**：[2510.09329v1](https://arxiv.org/abs/2510.09329) · [PDF](https://arxiv.org/pdf/2510.09329.pdf)  
**作者**：Zenan Lin, Wei Li, Jintao Chen, Zihao Wu, Wenxiong Kang, Changxin Gao, Liansheng Wang, Jin-Gang Yu  
**一句话要点**：提出IRCR-Net以解决病理图像中半监督细胞实例分割的噪声与一致性不足问题

**关键词**：半监督学习, 细胞实例分割, 一致性正则化, 伪标签噪声, 病理图像分析, 形态先验知识

## 3 点简述
- 核心问题：半监督方法在细胞实例分割中缺乏实例级一致性正则化，易引入噪声伪标签。
- 方法要点：引入MIAC和PIAC机制，利用形态先验评估伪标签质量，提升密集重叠细胞分割。
- 实验或效果：在多个公开数据集上显著优于现有方法，部分场景超越全监督方法。

## 摘要（原文）

> Nuclei instance segmentation in pathological images is crucial for downstream
> tasks such as tumor microenvironment analysis. However, the high cost and
> scarcity of annotated data limit the applicability of fully supervised methods,
> while existing semi-supervised methods fail to adequately regularize
> consistency at the instance level, lack leverage of the inherent prior
> knowledge of pathological structures, and are prone to introducing noisy
> pseudo-labels during training. In this paper, we propose an Instance-Aware
> Robust Consistency Regularization Network (IRCR-Net) for accurate
> instance-level nuclei segmentation. Specifically, we introduce the
> Matching-Driven Instance-Aware Consistency (MIAC) and Prior-Driven
> Instance-Aware Consistency (PIAC) mechanisms to refine the nuclei instance
> segmentation result of the teacher and student subnetwork, particularly for
> densely distributed and overlapping nuclei. We incorporate morphological prior
> knowledge of nuclei in pathological images and utilize these priors to assess
> the quality of pseudo-labels generated from unlabeled data. Low-quality
> pseudo-labels are discarded, while high-quality predictions are enhanced to
> reduce pseudo-label noise and benefit the network's robust training.
> Experimental results demonstrate that the proposed method significantly
> enhances semi-supervised nuclei instance segmentation performance across
> multiple public datasets compared to existing approaches, even surpassing fully
> supervised methods in some scenarios.

