---
layout: default
title: Late-decoupled 3D Hierarchical Semantic Segmentation with Semantic Prototype Discrimination based Bi-branch Supervision
---

# Late-decoupled 3D Hierarchical Semantic Segmentation with Semantic Prototype Discrimination based Bi-branch Supervision
**arXiv**：[2511.16650v1](https://arxiv.org/abs/2511.16650) · [PDF](https://arxiv.org/pdf/2511.16650.pdf)  
**作者**：Shuyu Cao, Chongshou Li, Jie Xu, Tianrui Li, Na Zhao  

**一句话要点**：提出晚解耦双分支框架以解决3D层次语义分割中的层次冲突和类别不平衡问题

**关键词**：3D层次语义分割, 晚解耦架构, 语义原型, 双分支监督, 类别不平衡, 多粒度理解

## 3 点简述
- 核心问题：多标签学习导致层次冲突，类别不平衡影响模型性能
- 方法要点：采用晚解耦多解码器结构和语义原型双分支监督机制
- 实验或效果：在多个数据集上实现先进性能，组件可即插即用

## 摘要（原文）

> 3D hierarchical semantic segmentation (3DHS) is crucial for embodied intelligence applications that demand a multi-grained and multi-hierarchy understanding of 3D scenes. Despite the progress, previous 3DHS methods have overlooked following two challenges: I) multi-label learning with a parameter-sharing model can lead to multi-hierarchy conflicts in cross-hierarchy optimization, and II) the class imbalance issue is inevitable across multiple hierarchies of 3D scenes, which makes the model performance become dominated by major classes. To address these issues, we propose a novel framework with a primary 3DHS branch and an auxiliary discrimination branch. Specifically, to alleviate the multi-hierarchy conflicts, we propose a late-decoupled 3DHS framework which employs multiple decoders with the coarse-to-fine hierarchical guidance and consistency. The late-decoupled architecture can mitigate the underfitting and overfitting conflicts among multiple hierarchies and can also constrain the class imbalance problem in each individual hierarchy. Moreover, we introduce a 3DHS-oriented semantic prototype based bi-branch supervision mechanism, which additionally learns class-wise discriminative point cloud features and performs mutual supervision between the auxiliary and 3DHS branches, to enhance the class-imbalance segmentation. Extensive experiments on multiple datasets and backbones demonstrate that our approach achieves state-of-the-art 3DHS performance, and its core components can also be used as a plug-and-play enhancement to improve previous methods.

