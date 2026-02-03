---
layout: default
title: CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions
---

# CloDS: Visual-Only Unsupervised Cloth Dynamics Learning in Unknown Conditions
**arXiv**：[2602.01844v1](https://arxiv.org/abs/2602.01844) · [PDF](https://arxiv.org/pdf/2602.01844.pdf)  
**作者**：Yuliang Zhan, Jian Li, Wenbing Huang, Wenbing Huang, Yang Liu, Hao Sun  

**一句话要点**：提出CloDS框架以解决未知条件下仅从视觉数据无监督学习布料动态的挑战

**关键词**：无监督学习, 布料动态模拟, 视觉到几何映射, 高斯泼溅, 多视角观测, 未知条件

## 3 点简述
- 核心问题：现有方法需已知物理属性作为监督，限制了在未知条件下的应用
- 方法要点：采用三阶段流程，通过双位置不透明度调制实现视频到几何的映射
- 实验或效果：在综合实验中有效学习布料动态，对未见配置保持强泛化能力

## 摘要（原文）

> Deep learning has demonstrated remarkable capabilities in simulating complex dynamic systems. However, existing methods require known physical properties as supervision or inputs, limiting their applicability under unknown conditions. To explore this challenge, we introduce Cloth Dynamics Grounding (CDG), a novel scenario for unsupervised learning of cloth dynamics from multi-view visual observations. We further propose Cloth Dynamics Splatting (CloDS), an unsupervised dynamic learning framework designed for CDG. CloDS adopts a three-stage pipeline that first performs video-to-geometry grounding and then trains a dynamics model on the grounded meshes. To cope with large non-linear deformations and severe self-occlusions during grounding, we introduce a dual-position opacity modulation that supports bidirectional mapping between 2D observations and 3D geometry via mesh-based Gaussian splatting in video-to-geometry grounding stage. It jointly considers the absolute and relative position of Gaussian components. Comprehensive experimental evaluations demonstrate that CloDS effectively learns cloth dynamics from visual data while maintaining strong generalization capabilities for unseen configurations. Our code is available at https://github.com/whynot-zyl/CloDS. Visualization results are available at https://github.com/whynot-zyl/CloDS_video}.%\footnote{As in this example.

