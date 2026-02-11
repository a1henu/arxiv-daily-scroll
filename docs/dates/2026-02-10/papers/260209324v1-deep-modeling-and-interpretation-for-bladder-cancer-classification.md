---
layout: default
title: Deep Modeling and Interpretation for Bladder Cancer Classification
---

# Deep Modeling and Interpretation for Bladder Cancer Classification
**arXiv**：[2602.09324v1](https://arxiv.org/abs/2602.09324) · [PDF](https://arxiv.org/pdf/2602.09324.pdf)  
**作者**：Ahmad Chaddad, Yihang Wu, Xianrui Chen  

**一句话要点**：评估深度模型在膀胱癌分类中的性能、校准与可解释性，提出模型选择建议。

**关键词**：膀胱癌分类, 深度模型评估, 校准分析, 可解释性, 医学影像, Transformer模型

## 3 点简述
- 核心问题：医学影像中异常区域小，深度模型在膀胱癌分类中性能与可解释性未知。
- 方法要点：比较13个CNN与Transformer模型，进行校准分析和GradCAM++可解释性评估。
- 实验或效果：ConvNext泛化能力有限，ViT校准效果更好，无模型适用于所有可解释场景。

## 摘要（原文）

> Deep models based on vision transformer (ViT) and convolutional neural network (CNN) have demonstrated remarkable performance on natural datasets. However, these models may not be similar in medical imaging, where abnormal regions cover only a small portion of the image. This challenge motivates this study to investigate the latest deep models for bladder cancer classification tasks. We propose the following to evaluate these deep models: 1) standard classification using 13 models (four CNNs and eight transormer-based models), 2) calibration analysis to examine if these models are well calibrated for bladder cancer classification, and 3) we use GradCAM++ to evaluate the interpretability of these models for clinical diagnosis. We simulate $\sim 300$ experiments on a publicly multicenter bladder cancer dataset, and the experimental results demonstrate that the ConvNext series indicate limited generalization ability to classify bladder cancer images (e.g., $\sim 60\%$ accuracy). In addition, ViTs show better calibration effects compared to ConvNext and swin transformer series. We also involve test time augmentation to improve the models interpretability. Finally, no model provides a one-size-fits-all solution for a feasible interpretable model. ConvNext series are suitable for in-distribution samples, while ViT and its variants are suitable for interpreting out-of-distribution samples.

