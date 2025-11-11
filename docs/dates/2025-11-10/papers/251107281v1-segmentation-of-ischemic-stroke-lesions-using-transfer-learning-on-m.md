---
layout: default
title: Segmentation of Ischemic Stroke Lesions using Transfer Learning on Multi-sequence MRI
---

# Segmentation of Ischemic Stroke Lesions using Transfer Learning on Multi-sequence MRI
**arXiv**：[2511.07281v1](https://arxiv.org/abs/2511.07281) · [PDF](https://arxiv.org/pdf/2511.07281.pdf)  
**作者**：R. P. Chowdhury, T. Rahman  

**一句话要点**：提出基于迁移学习的Res-Unet框架以自动分割缺血性卒中病灶

**关键词**：缺血性卒中分割, 迁移学习, Res-Unet架构, 多序列MRI, 多数投票分类器

## 3 点简述
- 核心问题：手动分割缺血性卒中病灶耗时且不一致，传统方法依赖手工特征难以处理复杂形状
- 方法要点：使用Res-Unet架构，结合迁移学习，在T1、T2、DWI和FLAIR等多序列MRI上训练
- 实验或效果：在ISLES 2015数据集上验证，Dice得分80.5%，准确率74.03%

## 摘要（原文）

> The accurate understanding of ischemic stroke lesions is critical for
> efficient therapy and prognosis of stroke patients. Magnetic resonance imaging
> (MRI) is sensitive to acute ischemic stroke and is a common diagnostic method
> for stroke. However, manual lesion segmentation performed by experts is
> tedious, time-consuming, and prone to observer inconsistency. Automatic medical
> image analysis methods have been proposed to overcome this challenge. However,
> previous approaches have relied on hand-crafted features that may not capture
> the irregular and physiologically complex shapes of ischemic stroke lesions. In
> this study, we present a novel framework for quickly and automatically
> segmenting ischemic stroke lesions on various MRI sequences, including
> T1-weighted, T2-weighted, DWI, and FLAIR. The proposed methodology is validated
> on the ISLES 2015 Brain Stroke sequence dataset, where we trained our model
> using the Res-Unet architecture twice: first, with pre-existing weights, and
> then without, to explore the benefits of transfer learning. Evaluation metrics,
> including the Dice score and sensitivity, were computed across 3D volumes.
> Finally, a Majority Voting Classifier was integrated to amalgamate the outcomes
> from each axis, resulting in a comprehensive segmentation method. Our efforts
> culminated in achieving a Dice score of 80.5\% and an accuracy of 74.03\%,
> showcasing the efficacy of our segmentation approach.

