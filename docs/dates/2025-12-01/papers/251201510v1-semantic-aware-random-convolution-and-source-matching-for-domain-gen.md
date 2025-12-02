---
layout: default
title: Semantic-aware Random Convolution and Source Matching for Domain Generalization in Medical Image Segmentation
---

# Semantic-aware Random Convolution and Source Matching for Domain Generalization in Medical Image Segmentation
**arXiv**：[2512.01510v1](https://arxiv.org/abs/2512.01510) · [PDF](https://arxiv.org/pdf/2512.01510.pdf)  
**作者**：Franz Thaler, Martin Urschler, Mateusz Kozinski, Matthias AF Gsell, Gernot Plank, Darko Stern  

**一句话要点**：提出SRCSM方法以解决医学图像分割中的单源域泛化问题

**关键词**：医学图像分割, 域泛化, 语义感知增强, 随机卷积, 跨模态泛化, 单源训练

## 3 点简述
- 核心问题：单源域泛化，即训练于一个域（如CT）直接应用于不同域（如MR）而无新域数据。
- 方法要点：训练时通过语义感知随机卷积多样化源域，测试时通过强度映射使目标域图像类似源域。
- 实验或效果：在跨模态和跨中心设置中超越先前方法，部分场景匹配域内基线性能。

## 摘要（原文）

> We tackle the challenging problem of single-source domain generalization (DG) for medical image segmentation. To this end, we aim for training a network on one domain (e.g., CT) and directly apply it to a different domain (e.g., MR) without adapting the model and without requiring images or annotations from the new domain during training. We propose a novel method for promoting DG when training deep segmentation networks, which we call SRCSM. During training, our method diversifies the source domain through semantic-aware random convolution, where different regions of a source image are augmented differently, based on their annotation labels. At test-time, we complement the randomization of the training domain via mapping the intensity of target domain images, making them similar to source domain data. We perform a comprehensive evaluation on a variety of cross-modality and cross-center generalization settings for abdominal, whole-heart and prostate segmentation, where we outperform previous DG techniques in a vast majority of experiments. Additionally, we also investigate our method when training on whole-heart CT or MR data and testing on the diastolic and systolic phase of cine MR data captured with different scanner hardware, where we make a step towards closing the domain gap in this even more challenging setting. Overall, our evaluation shows that SRCSM can be considered a new state-of-the-art in DG for medical image segmentation and, moreover, even achieves a segmentation performance that matches the performance of the in-domain baseline in several settings.

