---
layout: default
title: Reconstruction Guided Few-shot Network For Remote Sensing Image Classification
---

# Reconstruction Guided Few-shot Network For Remote Sensing Image Classification
**arXiv**：[2601.07335v1](https://arxiv.org/abs/2601.07335) · [PDF](https://arxiv.org/pdf/2601.07335.pdf)  
**作者**：Mohit Jaiswal, Naman Jain, Shivani Pathak, Mainak Singha, Nikunja Bihari Kar, Ankit Jha, Biplab Banerjee  

**一句话要点**：提出重建引导小样本网络以解决遥感图像分类中样本少和类别多变问题

**关键词**：小样本学习, 遥感图像分类, 掩码重建, 特征学习, 空间理解

## 3 点简述
- 核心问题：遥感图像小样本分类面临标记样本有限和地物类型高变异性挑战
- 方法要点：通过掩码图像重建任务增强特征学习，提升空间理解和类别区分能力
- 实验或效果：在EuroSAT和PatternNet数据集上，1-shot和5-shot协议下优于现有基线

## 摘要（原文）

> Few-shot remote sensing image classification is challenging due to limited labeled samples and high variability in land-cover types. We propose a reconstruction-guided few-shot network (RGFS-Net) that enhances generalization to unseen classes while preserving consistency for seen categories. Our method incorporates a masked image reconstruction task, where parts of the input are occluded and reconstructed to encourage semantically rich feature learning. This auxiliary task strengthens spatial understanding and improves class discrimination under low-data settings. We evaluated the efficacy of EuroSAT and PatternNet datasets under 1-shot and 5-shot protocols, our approach consistently outperforms existing baselines. The proposed method is simple, effective, and compatible with standard backbones, offering a robust solution for few-shot remote sensing classification. Codes are available at https://github.com/stark0908/RGFS.

