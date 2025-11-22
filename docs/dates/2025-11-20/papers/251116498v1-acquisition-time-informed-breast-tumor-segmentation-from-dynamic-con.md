---
layout: default
title: Acquisition Time-Informed Breast Tumor Segmentation from Dynamic Contrast-Enhanced MRI
---

# Acquisition Time-Informed Breast Tumor Segmentation from Dynamic Contrast-Enhanced MRI
**arXiv**：[2511.16498v1](https://arxiv.org/abs/2511.16498) · [PDF](https://arxiv.org/pdf/2511.16498.pdf)  
**作者**：Rui Wang, Yuexi Du, John Lewin, R. Todd Constable, Nicha C. Dvornek  

**一句话要点**：提出基于采集时间调制的乳腺肿瘤分割方法以提升DCE-MRI分割性能与泛化能力

**关键词**：乳腺肿瘤分割, 动态对比增强MRI, 特征调制, 采集时间整合, 模型泛化, FiLM层

## 3 点简述
- 核心问题：DCE-MRI中采集协议和个体差异导致组织外观变化大，自动肿瘤分割困难
- 方法要点：使用FiLM层整合图像采集时间，调制模型特征以适应不同采集序列
- 实验或效果：在域内和域外数据集上验证，时间信息提升分割性能和模型泛化

## 摘要（原文）

> Dynamic contrast-enhanced magnetic resonance imaging (DCE-MRI) plays an important role in breast cancer screening, tumor assessment, and treatment planning and monitoring. The dynamic changes in contrast in different tissues help to highlight the tumor in post-contrast images. However, varying acquisition protocols and individual factors result in large variation in the appearance of tissues, even for images acquired in the same phase (e.g., first post-contrast phase), making automated tumor segmentation challenging. Here, we propose a tumor segmentation method that leverages knowledge of the image acquisition time to modulate model features according to the specific acquisition sequence. We incorporate the acquisition times using feature-wise linear modulation (FiLM) layers, a lightweight method for incorporating temporal information that also allows for capitalizing on the full, variables number of images acquired per imaging study. We trained baseline and different configurations for the time-modulated models with varying backbone architectures on a large public multisite breast DCE-MRI dataset. Evaluation on in-domain images and a public out-of-domain dataset showed that incorporating knowledge of phase acquisition time improved tumor segmentation performance and model generalization.

