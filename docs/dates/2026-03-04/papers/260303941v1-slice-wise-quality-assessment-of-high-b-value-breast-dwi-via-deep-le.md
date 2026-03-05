---
layout: default
title: Slice-wise quality assessment of high b-value breast DWI via deep learning-based artifact detection
---

# Slice-wise quality assessment of high b-value breast DWI via deep learning-based artifact detection
**arXiv**：[2603.03941v1](https://arxiv.org/abs/2603.03941) · [PDF](https://arxiv.org/pdf/2603.03941.pdf)  
**作者**：Ameya Markale, Luise Brock, Ihor Horishnyi, Dominika Skwierawska, Tri-Thien Nguyen, Hannes Schreiter, Shirin Heidarikahkesh, Lorenz A. Kapsner, Michael Uder, Sabine Ohlmeyer, Frederik B Laun, Andrzej Liebert, Sebastian Bickelhaupt  

**一句话要点**：提出基于深度学习的切片级高b值乳腺DWI伪影检测方法，以提升图像质量评估。

**关键词**：乳腺磁共振成像, 扩散加权成像, 伪影检测, 深度学习, 卷积神经网络, 图像质量评估

## 3 点简述
- 核心问题：高b值乳腺扩散加权成像易受高强度和低强度伪影影响，干扰诊断评估。
- 方法要点：使用卷积神经网络（如DenseNet121）进行二分类和多分类伪影检测，基于切片数据集。
- 实验或效果：在独立测试集上，DenseNet121对高强度和低强度伪影检测的AUROC分别达0.92和0.94，初步验证有效性。

## 摘要（原文）

> Diffusion-weighted imaging (DWI) can support lesion detection and characterization in breast magnetic resonance imaging (MRI), however especially high b-value diffusion-weighted acquisitions can be prone to intensity artifacts that can affect diagnostic image assessment. This study aims to detect both hyper- and hypointense artifacts on high b-value diffusion-weighted images (b=1500 s/mm2) using deep learning, employing either a binary classification (artifact presence) or a multiclass classification (artifact intensity) approach on a slice-wise dataset.This IRB-approved retrospective study used the single-center dataset comprising n=11806 slices from routine 3T breast MRI examinations performed between 2022 and mid-2023. Three convolutional neural network (CNN) architectures (DenseNet121, ResNet18, and SEResNet50) were trained for binary classification of hyper- and hypointense artifacts. The best performing model (DenseNet121) was applied to an independent holdout test set and was further trained separately for multiclass classification. Evaluation included area under receiver operating characteristic curve (AUROC), area under precision recall curve (AUPRC), precision, and recall, as well as analysis of predicted bounding box positions, derived from the network Grad-CAM heatmaps. DenseNet121 achieved AUROCs of 0.92 and 0.94 for hyper- and hypointense artifact detection, respectively, and weighted AUROCs of 0.85 and 0.88 for multiclass classification on single-slice high b-value diffusion-weighted images. A radiologist evaluated bounding box precision on a 1-5 Likert-like scale across 200 slices, achieving mean scores of 3.33+-1.04 for hyperintense artifacts and 2.62+-0.81 for hypointense artifacts. Hyper- and hypointense artifact detection in slice-wise breast DWI MRI dataset (b=1500 s/mm2) using CNNs particularly DenseNet121, seems promising and requires further validation.

