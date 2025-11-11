---
layout: default
title: 3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition
---

# 3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition
**arXiv**：[2511.07040v1](https://arxiv.org/abs/2511.07040) · [PDF](https://arxiv.org/pdf/2511.07040.pdf)  
**作者**：Yuanmin Huang, Wenxuan Li, Mi Zhang, Xiaohan Zhang, Xiaoyu You, Min Yang  

**一句话要点**：提出3D-ANC方法以增强3D点云识别的对抗鲁棒性

**关键词**：3D点云识别, 对抗鲁棒性, 神经坍缩, 特征学习, 自适应训练

## 3 点简述
- 核心问题：3D点云识别模型易受对抗攻击，特征空间纠缠导致脆弱性。
- 方法要点：利用神经坍缩机制，结合ETF对齐分类和自适应训练框架。
- 实验效果：在ModelNet40上，DGCNN准确率从27.2%提升至80.9%。

## 摘要（原文）

> Deep neural networks have recently achieved notable progress in 3D point
> cloud recognition, yet their vulnerability to adversarial perturbations poses
> critical security challenges in practical deployments. Conventional defense
> mechanisms struggle to address the evolving landscape of multifaceted attack
> patterns. Through systematic analysis of existing defenses, we identify that
> their unsatisfactory performance primarily originates from an entangled feature
> space, where adversarial attacks can be performed easily. To this end, we
> present 3D-ANC, a novel approach that capitalizes on the Neural Collapse (NC)
> mechanism to orchestrate discriminative feature learning. In particular, NC
> depicts where last-layer features and classifier weights jointly evolve into a
> simplex equiangular tight frame (ETF) arrangement, establishing maximally
> separable class prototypes. However, leveraging this advantage in 3D
> recognition confronts two substantial challenges: (1) prevalent class imbalance
> in point cloud datasets, and (2) complex geometric similarities between object
> categories. To tackle these obstacles, our solution combines an ETF-aligned
> classification module with an adaptive training framework consisting of
> representation-balanced learning (RBL) and dynamic feature direction loss
> (FDL). 3D-ANC seamlessly empowers existing models to develop disentangled
> feature spaces despite the complexity in 3D data distribution. Comprehensive
> evaluations state that 3D-ANC significantly improves the robustness of models
> with various structures on two datasets. For instance, DGCNN's classification
> accuracy is elevated from 27.2% to 80.9% on ModelNet40 -- a 53.7% absolute gain
> that surpasses leading baselines by 34.0%.

