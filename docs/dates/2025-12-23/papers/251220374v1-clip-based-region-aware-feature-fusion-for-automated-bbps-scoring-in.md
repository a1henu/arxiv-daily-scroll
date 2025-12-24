---
layout: default
title: CLIP Based Region-Aware Feature Fusion for Automated BBPS Scoring in Colonoscopy Images
---

# CLIP Based Region-Aware Feature Fusion for Automated BBPS Scoring in Colonoscopy Images
**arXiv**：[2512.20374v1](https://arxiv.org/abs/2512.20374) · [PDF](https://arxiv.org/pdf/2512.20374.pdf)  
**作者**：Yujia Fu, Zhiyu Dong, Tianwen Qian, Chenye Zheng, Danian Ji, Linhai Zhuo  

**一句话要点**：提出基于CLIP的区域感知特征融合方法，用于结肠镜图像中自动BBPS评分。

**关键词**：结肠镜图像分析, BBPS自动评分, CLIP模型应用, 特征融合, 迁移学习

## 3 点简述
- 核心问题：手动BBPS评分存在主观性和观察者间变异性，影响结肠镜检查效果。
- 方法要点：利用CLIP模型，通过适配器迁移学习和粪便特征提取分支，融合全局视觉特征与粪便相关文本先验。
- 实验或效果：在自建数据集和公开NERTHU数据集上验证，优于现有基线，具有临床部署潜力。

## 摘要（原文）

> Accurate assessment of bowel cleanliness is essential for effective colonoscopy procedures. The Boston Bowel Preparation Scale (BBPS) offers a standardized scoring system but suffers from subjectivity and inter-observer variability when performed manually. In this paper, to support robust training and evaluation, we construct a high-quality colonoscopy dataset comprising 2,240 images from 517 subjects, annotated with expert-agreed BBPS scores. We propose a novel automated BBPS scoring framework that leverages the CLIP model with adapter-based transfer learning and a dedicated fecal-feature extraction branch. Our method fuses global visual features with stool-related textual priors to improve the accuracy of bowel cleanliness evaluation without requiring explicit segmentation. Extensive experiments on both our dataset and the public NERTHU dataset demonstrate the superiority of our approach over existing baselines, highlighting its potential for clinical deployment in computer-aided colonoscopy analysis.

