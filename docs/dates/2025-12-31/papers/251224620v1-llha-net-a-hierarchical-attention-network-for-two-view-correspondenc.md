---
layout: default
title: LLHA-Net: A Hierarchical Attention Network for Two-View Correspondence Learning
---

# LLHA-Net: A Hierarchical Attention Network for Two-View Correspondence Learning
**arXiv**：[2512.24620v1](https://arxiv.org/abs/2512.24620) · [PDF](https://arxiv.org/pdf/2512.24620.pdf)  
**作者**：Shuyuan Lin, Yu Guo, Xiao Chen, Yanjie Liang, Guobao Xiao, Feiran Huang  

**一句话要点**：提出LLHA-Net以解决两视图特征点匹配中的离群点问题

**关键词**：特征点匹配, 离群点去除, 分层注意力网络, 两视图对应学习, 相机姿态估计

## 3 点简述
- 核心问题：特征点匹配中离群点影响精度与鲁棒性，需在大量离群点下提取高质量信息。
- 方法要点：采用分层注意力网络，结合阶段融合、分层提取和注意力机制增强特征表示能力。
- 实验或效果：在YFCC100M和SUN3D数据集上，离群点去除和相机姿态估计优于现有技术。

## 摘要（原文）

> Establishing the correct correspondence of feature points is a fundamental task in computer vision. However, the presence of numerous outliers among the feature points can significantly affect the matching results, reducing the accuracy and robustness of the process. Furthermore, a challenge arises when dealing with a large proportion of outliers: how to ensure the extraction of high-quality information while reducing errors caused by negative samples. To address these issues, in this paper, we propose a novel method called Layer-by-Layer Hierarchical Attention Network, which enhances the precision of feature point matching in computer vision by addressing the issue of outliers. Our method incorporates stage fusion, hierarchical extraction, and an attention mechanism to improve the network's representation capability by emphasizing the rich semantic information of feature points. Specifically, we introduce a layer-by-layer channel fusion module, which preserves the feature semantic information from each stage and achieves overall fusion, thereby enhancing the representation capability of the feature points. Additionally, we design a hierarchical attention module that adaptively captures and fuses global perception and structural semantic information using an attention mechanism. Finally, we propose two architectures to extract and integrate features, thereby improving the adaptability of our network. We conduct experiments on two public datasets, namely YFCC100M and SUN3D, and the results demonstrate that our proposed method outperforms several state-of-the-art techniques in both outlier removal and camera pose estimation. Source code is available at http://www.linshuyuan.com.

