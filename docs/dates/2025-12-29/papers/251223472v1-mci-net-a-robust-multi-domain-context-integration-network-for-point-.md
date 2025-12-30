---
layout: default
title: MCI-Net: A Robust Multi-Domain Context Integration Network for Point Cloud Registration
---

# MCI-Net: A Robust Multi-Domain Context Integration Network for Point Cloud Registration
**arXiv**：[2512.23472v1](https://arxiv.org/abs/2512.23472) · [PDF](https://arxiv.org/pdf/2512.23472.pdf)  
**作者**：Shuyuan Lin, Wenwu Peng, Junjie Huang, Qiang Qi, Miaohui Wang, Jian Weng  

**一句话要点**：提出MCI-Net以解决点云注册中特征学习不足的问题，通过多域上下文集成提升性能。

**关键词**：点云注册, 多域上下文集成, 图神经网络, 特征学习, 动态内点选择

## 3 点简述
- 核心问题：现有基于欧几里得邻域的特征提取方法难以有效捕获点云的隐式语义和结构一致性。
- 方法要点：设计图邻域聚合模块和渐进上下文交互模块，增强特征表示和判别性。
- 实验或效果：在室内RGB-D和室外LiDAR数据集上显著优于现有方法，3DMatch上注册召回率达96.4%。

## 摘要（原文）

> Robust and discriminative feature learning is critical for high-quality point cloud registration. However, existing deep learning-based methods typically rely on Euclidean neighborhood-based strategies for feature extraction, which struggle to effectively capture the implicit semantics and structural consistency in point clouds. To address these issues, we propose a multi-domain context integration network (MCI-Net) that improves feature representation and registration performance by aggregating contextual cues from diverse domains. Specifically, we propose a graph neighborhood aggregation module, which constructs a global graph to capture the overall structural relationships within point clouds. We then propose a progressive context interaction module to enhance feature discriminability by performing intra-domain feature decoupling and inter-domain context interaction. Finally, we design a dynamic inlier selection method that optimizes inlier weights using residual information from multiple iterations of pose estimation, thereby improving the accuracy and robustness of registration. Extensive experiments on indoor RGB-D and outdoor LiDAR datasets show that the proposed MCI-Net significantly outperforms existing state-of-the-art methods, achieving the highest registration recall of 96.4\% on 3DMatch. Source code is available at http://www.linshuyuan.com.

