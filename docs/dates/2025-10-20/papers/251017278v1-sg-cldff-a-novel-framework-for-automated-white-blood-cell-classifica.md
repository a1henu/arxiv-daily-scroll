---
layout: default
title: SG-CLDFF: A Novel Framework for Automated White Blood Cell Classification and Segmentation
---

# SG-CLDFF: A Novel Framework for Automated White Blood Cell Classification and Segmentation
**arXiv**：[2510.17278v1](https://arxiv.org/abs/2510.17278) · [PDF](https://arxiv.org/pdf/2510.17278.pdf)  
**作者**：Mehdi Zekriyapanah Gashti, Mostafa Mohammadpour, Ghasem Farjamnia  

**一句话要点**：提出SG-CLDFF框架以改进白细胞分割与分类的鲁棒性和可解释性

**关键词**：白细胞分类, 图像分割, 显著性检测, 特征融合, 多任务学习, 可解释AI

## 3 点简述
- 核心问题：白细胞图像分割与分类受染色变异、复杂背景和类别不平衡影响
- 方法要点：结合显著性引导预处理与跨层深度特征融合，使用多任务训练
- 实验或效果：在公开基准测试中IoU、F1和分类准确率优于基线模型

## 摘要（原文）

> Accurate segmentation and classification of white blood cells (WBCs) in
> microscopic images are essential for diagnosis and monitoring of many
> hematological disorders, yet remain challenging due to staining variability,
> complex backgrounds, and class imbalance. In this paper, we introduce a novel
> Saliency-Guided Cross-Layer Deep Feature Fusion framework (SG-CLDFF) that
> tightly integrates saliency-driven preprocessing with multi-scale deep feature
> aggregation to improve both robustness and interpretability for WBC analysis.
> SG-CLDFF first computes saliency priors to highlight candidate WBC regions and
> guide subsequent feature extraction. A lightweight hybrid backbone
> (EfficientSwin-style) produces multi-resolution representations, which are
> fused by a ResNeXt-CC-inspired cross-layer fusion module to preserve
> complementary information from shallow and deep layers. The network is trained
> in a multi-task setup with concurrent segmentation and cell-type classification
> heads, using class-aware weighted losses and saliency-alignment regularization
> to mitigate imbalance and suppress background activation. Interpretability is
> enforced through Grad-CAM visualizations and saliency consistency checks,
> allowing model decisions to be inspected at the regional level. We validate the
> framework on standard public benchmarks (BCCD, LISC, ALL-IDB), reporting
> consistent gains in IoU, F1, and classification accuracy compared to strong CNN
> and transformer baselines. An ablation study also demonstrates the individual
> contributions of saliency preprocessing and cross-layer fusion. SG-CLDFF offers
> a practical and explainable path toward more reliable automated WBC analysis in
> clinical workflows.

