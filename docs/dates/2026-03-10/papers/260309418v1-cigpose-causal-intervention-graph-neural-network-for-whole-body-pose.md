---
layout: default
title: CIGPose: Causal Intervention Graph Neural Network for Whole-Body Pose Estimation
---

# CIGPose: Causal Intervention Graph Neural Network for Whole-Body Pose Estimation
**arXiv**：[2603.09418v1](https://arxiv.org/abs/2603.09418) · [PDF](https://arxiv.org/pdf/2603.09418.pdf)  
**作者**：Bohao Li, Zhicheng Cao, Huixian Li, Yangming Guo  

**一句话要点**：提出CIGPose框架，通过因果干预解决全身姿态估计中的虚假相关性问题

**关键词**：全身姿态估计, 因果干预, 图神经网络, 结构因果模型, 解剖学合理性

## 3 点简述
- 核心问题：现有方法因学习视觉上下文中的虚假相关性，导致姿态预测缺乏鲁棒性和解剖学合理性
- 方法要点：基于结构因果模型设计因果干预模块，用上下文不变嵌入替换混淆关键点表示，结合分层图神经网络推理
- 实验或效果：在COCO-WholeBody上达到67.0% AP的新SOTA，使用额外数据后提升至67.5% AP，展示优越鲁棒性和数据效率

## 摘要（原文）

> State-of-the-art whole-body pose estimators often lack robustness, producing anatomically implausible predictions in challenging scenes. We posit this failure stems from spurious correlations learned from visual context, a problem we formalize using a Structural Causal Model (SCM). The SCM identifies visual context as a confounder that creates a non-causal backdoor path, corrupting the model's reasoning. We introduce the Causal Intervention Graph Pose (CIGPose) framework to address this by approximating the true causal effect between visual evidence and pose. The core of CIGPose is a novel Causal Intervention Module: it first identifies confounded keypoint representations via predictive uncertainty and then replaces them with learned, context-invariant canonical embeddings. These deconfounded embeddings are processed by a hierarchical graph neural network that reasons over the human skeleton at both local and global semantic levels to enforce anatomical plausibility. Extensive experiments show CIGPose achieves a new state-of-the-art on COCO-WholeBody. Notably, our CIGPose-x model achieves 67.0\% AP, surpassing prior methods that rely on extra training data. With the additional UBody dataset, CIGPose-x is further boosted to 67.5\% AP, demonstrating superior robustness and data efficiency. The codes and models are publicly available at https://github.com/53mins/CIGPose.

