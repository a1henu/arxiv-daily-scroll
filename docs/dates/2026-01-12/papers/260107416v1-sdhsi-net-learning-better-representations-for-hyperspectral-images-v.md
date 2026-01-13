---
layout: default
title: SDHSI-Net: Learning Better Representations for Hyperspectral Images via Self-Distillation
---

# SDHSI-Net: Learning Better Representations for Hyperspectral Images via Self-Distillation
**arXiv**：[2601.07416v1](https://arxiv.org/abs/2601.07416) · [PDF](https://arxiv.org/pdf/2601.07416.pdf)  
**作者**：Prachet Dev Singh, Shyamsundar Paramasivam, Sneha Barman, Mainak Singha, Ankit Jha, Girish Mishra, Biplab Banerjee  

**一句话要点**：提出SDHSI-Net，通过自蒸馏学习高光谱图像分类的更好表示

**关键词**：高光谱图像分类, 自蒸馏, 特征表示学习, 光谱空间学习, 深度学习

## 3 点简述
- 高光谱图像分类面临高维光谱和有限标注数据的挑战，易过拟合且计算成本高。
- 采用自蒸馏方法，将网络早期输出作为软目标，增强中间与最终预测的一致性。
- 在基准数据集上验证，分类准确性和鲁棒性显著提升，代码已开源。

## 摘要（原文）

> Hyperspectral image (HSI) classification presents unique challenges due to its high spectral dimensionality and limited labeled data. Traditional deep learning models often suffer from overfitting and high computational costs. Self-distillation (SD), a variant of knowledge distillation where a network learns from its own predictions, has recently emerged as a promising strategy to enhance model performance without requiring external teacher networks. In this work, we explore the application of SD to HSI by treating earlier outputs as soft targets, thereby enforcing consistency between intermediate and final predictions. This process improves intra-class compactness and inter-class separability in the learned feature space. Our approach is validated on two benchmark HSI datasets and demonstrates significant improvements in classification accuracy and robustness, highlighting the effectiveness of SD for spectral-spatial learning. Codes are available at https://github.com/Prachet-Dev-Singh/SDHSI.

