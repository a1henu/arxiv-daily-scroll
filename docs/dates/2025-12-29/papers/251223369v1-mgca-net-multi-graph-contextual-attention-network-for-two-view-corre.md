---
layout: default
title: MGCA-Net: Multi-Graph Contextual Attention Network for Two-View Correspondence Learning
---

# MGCA-Net: Multi-Graph Contextual Attention Network for Two-View Correspondence Learning
**arXiv**：[2512.23369v1](https://arxiv.org/abs/2512.23369) · [PDF](https://arxiv.org/pdf/2512.23369.pdf)  
**作者**：Shuyuan Lin, Mengtin Lo, Haosheng Chen, Yanjie Liang, Qiangqiang Wu  

**一句话要点**：提出MGCA-Net以解决双视图对应学习中的局部几何建模和跨阶段信息优化问题。

**关键词**：双视图对应学习, 几何注意力, 跨阶段共识, 相机姿态估计, 3D重建

## 3 点简述
- 核心问题：现有方法在局部几何建模和跨阶段信息优化方面存在局限，影响匹配对几何约束的准确捕获和模型鲁棒性。
- 方法要点：设计CGA模块通过自适应注意力机制整合空间位置和特征信息，增强局部和全局几何关系捕获能力；CSMGC模块通过跨阶段稀疏图网络建立几何共识，确保不同阶段信息一致性。
- 实验或效果：在YFCC100M和SUN3D数据集上，MGCA-Net在离群点剔除和相机姿态估计任务中显著优于现有SOTA方法。

## 摘要（原文）

> Two-view correspondence learning is a key task in computer vision, which aims to establish reliable matching relationships for applications such as camera pose estimation and 3D reconstruction. However, existing methods have limitations in local geometric modeling and cross-stage information optimization, which make it difficult to accurately capture the geometric constraints of matched pairs and thus reduce the robustness of the model. To address these challenges, we propose a Multi-Graph Contextual Attention Network (MGCA-Net), which consists of a Contextual Geometric Attention (CGA) module and a Cross-Stage Multi-Graph Consensus (CSMGC) module. Specifically, CGA dynamically integrates spatial position and feature information via an adaptive attention mechanism and enhances the capability to capture both local and global geometric relationships. Meanwhile, CSMGC establishes geometric consensus via a cross-stage sparse graph network, ensuring the consistency of geometric information across different stages. Experimental results on two representative YFCC100M and SUN3D datasets show that MGCA-Net significantly outperforms existing SOTA methods in the outlier rejection and camera pose estimation tasks. Source code is available at http://www.linshuyuan.com.

