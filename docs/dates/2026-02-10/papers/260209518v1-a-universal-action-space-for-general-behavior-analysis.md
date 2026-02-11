---
layout: default
title: A Universal Action Space for General Behavior Analysis
---

# A Universal Action Space for General Behavior Analysis
**arXiv**：[2602.09518v1](https://arxiv.org/abs/2602.09518) · [PDF](https://arxiv.org/pdf/2602.09518.pdf)  
**作者**：Hung-Shuo Chang, Yue-Cheng Yang, Yu-Hsi Chen, Wei-Hsin Chen, Chien-Yao Wang, James C. Liao, Chien-Chang Chen, Hen-Hsen Huang, Hong-Yuan Mark Liao  

**一句话要点**：提出通用动作空间以分析动物和人类行为

**关键词**：行为分析, 通用动作空间, 深度学习, 计算机视觉, 动物行为

## 3 点简述
- 核心问题：早期行为分析依赖手工特征，鲁棒性和泛化性有限
- 方法要点：基于ImageNet范式，利用现有标注数据集构建大规模通用动作空间
- 实验或效果：将该空间应用于哺乳动物和黑猩猩行为数据集的分类与分析

## 摘要（原文）

> Analyzing animal and human behavior has long been a challenging task in computer vision. Early approaches from the 1970s to the 1990s relied on hand-crafted edge detection, segmentation, and low-level features such as color, shape, and texture to locate objects and infer their identities-an inherently ill-posed problem. Behavior analysis in this era typically proceeded by tracking identified objects over time and modeling their trajectories using sparse feature points, which further limited robustness and generalization. A major shift occurred with the introduction of ImageNet by Deng and Li in 2010, which enabled large-scale visual recognition through deep neural networks and effectively served as a comprehensive visual dictionary. This development allowed object recognition to move beyond complex low-level processing toward learned high-level representations. In this work, we follow this paradigm to build a large-scale Universal Action Space (UAS) using existing labeled human-action datasets. We then use this UAS as the foundation for analyzing and categorizing mammalian and chimpanzee behavior datasets. The source code is released on GitHub at https://github.com/franktpmvu/Universal-Action-Space.

