---
layout: default
title: AdaptOVCD: Training-Free Open-Vocabulary Remote Sensing Change Detection via Adaptive Information Fusion
---

# AdaptOVCD: Training-Free Open-Vocabulary Remote Sensing Change Detection via Adaptive Information Fusion
**arXiv**：[2602.06529v1](https://arxiv.org/abs/2602.06529) · [PDF](https://arxiv.org/pdf/2602.06529.pdf)  
**作者**：Mingyu Dou, Shi Qiu, Ming Hu, Yifan Chen, Huping Ye, Xiaohan Liao, Zhe Sun  

**一句话要点**：提出AdaptOVCD，通过自适应信息融合实现免训练开放词汇遥感变化检测

**关键词**：遥感变化检测, 开放词汇学习, 免训练方法, 信息融合, 自适应设计, 零样本检测

## 3 点简述
- 核心问题：现有遥感变化检测方法依赖预定义类别和像素级标注，泛化能力受限
- 方法要点：基于双维度多级信息融合，垂直整合数据、特征和决策层，水平引入自适应设计
- 实验或效果：在九个场景中零样本检测任意类别变化，性能显著优于现有免训练方法

## 摘要（原文）

> Remote sensing change detection plays a pivotal role in domains such as environmental monitoring, urban planning, and disaster assessment. However, existing methods typically rely on predefined categories and large-scale pixel-level annotations, which limit their generalization and applicability in open-world scenarios. To address these limitations, this paper proposes AdaptOVCD, a training-free Open-Vocabulary Change Detection (OVCD) architecture based on dual-dimensional multi-level information fusion. The framework integrates multi-level information fusion across data, feature, and decision levels vertically while incorporating targeted adaptive designs horizontally, achieving deep synergy among heterogeneous pre-trained models to effectively mitigate error propagation. Specifically, (1) at the data level, Adaptive Radiometric Alignment (ARA) fuses radiometric statistics with original texture features and synergizes with SAM-HQ to achieve radiometrically consistent segmentation; (2) at the feature level, Adaptive Change Thresholding (ACT) combines global difference distributions with edge structure priors and leverages DINOv3 to achieve robust change detection; (3) at the decision level, Adaptive Confidence Filtering (ACF) integrates semantic confidence with spatial constraints and collaborates with DGTRS-CLIP to achieve high-confidence semantic identification. Comprehensive evaluations across nine scenarios demonstrate that AdaptOVCD detects arbitrary category changes in a zero-shot manner, significantly outperforming existing training-free methods. Meanwhile, it achieves 84.89\% of the fully-supervised performance upper bound in cross-dataset evaluations and exhibits superior generalization capabilities. The code is available at https://github.com/Dmygithub/AdaptOVCD.

