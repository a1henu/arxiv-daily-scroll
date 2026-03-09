---
layout: default
title: Ensemble Learning with Sparse Hypercolumns
---

# Ensemble Learning with Sparse Hypercolumns
**arXiv**：[2603.06036v1](https://arxiv.org/abs/2603.06036) · [PDF](https://arxiv.org/pdf/2603.06036.pdf)  
**作者**：Julia Dietlmeier, Vayangi Ganepola, Oluwabukola G. Adegboro, Mayug Maniparambil, Claudia Mazo, Noel E. O'Connor  

**一句话要点**：提出基于分层子采样的稀疏超列集成学习方法，以解决脑肿瘤分割中计算复杂度高的问题。

**关键词**：超列, 集成学习, 分层子采样, 脑肿瘤分割, 低样本学习

## 3 点简述
- 核心问题：超列在图像分割中计算复杂度高，限制了实际应用。
- 方法要点：对VGG16超列应用分层子采样，并研究集成学习在稀疏超列上的性能。
- 实验或效果：在低样本情况下，集成方法表现竞争性，但N≤20时逻辑回归最有效，10%采样率下Dice分数达0.66。

## 摘要（原文）

> Directly inspired by findings in biological vision, high-dimensional hypercolumns are feature vectors built by concatenating multi-scale activations of convolutional neural networks for a single image pixel location. Together with powerful classifiers, they can be used for image segmentation i.e. pixel classification. However, in practice, there are only very few works dedicated to the use of hypercolumns. One reason is the computational complexity of processing concatenated dense hypercolumns that grows linearly with the size $N$ of the training set. In this work, we address this challenge by applying stratified subsampling to the VGG16 based hypercolumns. Furthermore, we investigate the performance of ensemble learning on sparse hypercolumns. Our experiments on a brain tumor dataset show that stacking and voting ensembles deliver competitive performance, but in the extreme low-shot case of $N \leq 20$, a simple Logistic Regression classifier is the most effective method. For 10% stratified subsampling rate, our best average Dice score is 0.66 for $N=20$. This is a statistically significant improvement of 24.53% over the standard multi-scale UNet baseline ($p$-value = $[3.07e-11]$, Wilcoxon signed-rank test), which is less effective due to overfitting.

