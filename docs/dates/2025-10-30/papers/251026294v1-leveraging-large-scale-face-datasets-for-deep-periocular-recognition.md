---
layout: default
title: Leveraging Large-Scale Face Datasets for Deep Periocular Recognition via Ocular Cropping
---

# Leveraging Large-Scale Face Datasets for Deep Periocular Recognition via Ocular Cropping
**arXiv**：[2510.26294v1](https://arxiv.org/abs/2510.26294) · [PDF](https://arxiv.org/pdf/2510.26294.pdf)  
**作者**：Fernando Alonso-Fernandez, Kevin Hernandez-Diaz, Jose Maria Buades Rubio, Josef Bigun  

**一句话要点**：利用大规模人脸数据集通过眼部裁剪进行深度眼周识别

**关键词**：眼周识别, 卷积神经网络, 大规模数据集, 生物识别, 图像裁剪, 性能评估

## 3 点简述
- 核心问题：眼周生物识别在非受控条件下性能下降，需提升识别准确性。
- 方法要点：从VGGFace2提取190万眼部图像，训练三种不同复杂度CNN架构。
- 实验效果：在UFPR-Periocular数据集上实现1-2% EER，优于现有方法。

## 摘要（原文）

> We focus on ocular biometrics, specifically the periocular region (the area
> around the eye), which offers high discrimination and minimal acquisition
> constraints. We evaluate three Convolutional Neural Network architectures of
> varying depth and complexity to assess their effectiveness for periocular
> recognition. The networks are trained on 1,907,572 ocular crops extracted from
> the large-scale VGGFace2 database. This significantly contrasts with existing
> works, which typically rely on small-scale periocular datasets for training
> having only a few thousand images. Experiments are conducted with ocular images
> from VGGFace2-Pose, a subset of VGGFace2 containing in-the-wild face images,
> and the UFPR-Periocular database, which consists of selfies captured via mobile
> devices with user guidance on the screen. Due to the uncontrolled conditions of
> VGGFace2, the Equal Error Rates (EERs) obtained with ocular crops range from
> 9-15%, noticeably higher than the 3-6% EERs achieved using full-face images. In
> contrast, UFPR-Periocular yields significantly better performance (EERs of
> 1-2%), thanks to higher image quality and more consistent acquisition
> protocols. To the best of our knowledge, these are the lowest reported EERs on
> the UFPR dataset to date.

