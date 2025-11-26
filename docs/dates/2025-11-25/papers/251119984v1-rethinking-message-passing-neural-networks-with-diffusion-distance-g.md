---
layout: default
title: Rethinking Message Passing Neural Networks with Diffusion Distance-guided Stress Majorization
---

# Rethinking Message Passing Neural Networks with Diffusion Distance-guided Stress Majorization
**arXiv**：[2511.19984v1](https://arxiv.org/abs/2511.19984) · [PDF](https://arxiv.org/pdf/2511.19984.pdf)  
**作者**：Haoran Zheng, Renchi Yang, Yubo Zhou, Jianliang Xu  

**一句话要点**：提出DDSM模型以解决图神经网络中的过平滑和过相关问题

**关键词**：消息传递神经网络, 扩散距离, 应力优化, 图学习, 过平滑问题

## 3 点简述
- 核心问题：MPNN因最小化Dirichlet能量导致过平滑和过相关
- 方法要点：结合应力优化、正交正则化和扩散距离指导消息传递
- 实验或效果：在15个基线中，于同质和异质图上表现显著提升

## 摘要（原文）

> Message passing neural networks (MPNNs) have emerged as go-to models for learning on graph-structured data in the past decade. Despite their effectiveness, most of such models still incur severe issues such as over-smoothing and -correlation, due to their underlying objective of minimizing the Dirichlet energy and the derived neighborhood aggregation operations. In this paper, we propose the DDSM, a new MPNN model built on an optimization framework that includes the stress majorization and orthogonal regularization for overcoming the above issues. Further, we introduce the diffusion distances for nodes into the framework to guide the new message passing operations and develop efficient algorithms for distance approximations, both backed by rigorous theoretical analyses. Our comprehensive experiments showcase that DDSM consistently and considerably outperforms 15 strong baselines on both homophilic and heterophilic graphs.

