---
layout: default
title: Detecting Fake Reviewer Groups in Dynamic Networks: An Adaptive Graph Learning Method
---

# Detecting Fake Reviewer Groups in Dynamic Networks: An Adaptive Graph Learning Method
**arXiv**：[2603.08332v1](https://arxiv.org/abs/2603.08332) · [PDF](https://arxiv.org/pdf/2603.08332.pdf)  
**作者**：Jing Zhang, Ke Huang, Yao Zhang, Bin Guo, Zhiwen Yu  

**一句话要点**：提出DS-DGA-GCN模型以检测动态网络中的虚假评论者群体

**关键词**：虚假评论检测, 动态图学习, 图卷积网络, 注意力机制, 网络特征评分

## 3 点简述
- 核心问题：虚假评论群体在冷启动场景下逃避传统检测方法，损害平台信任。
- 方法要点：建模产品-评论-评论者网络，集成网络特征评分和动态图注意力机制。
- 实验或效果：在亚马逊和小红书数据集上，准确率分别达89.8%和88.3%，优于基线方法。

## 摘要（原文）

> The proliferation of fake reviews, often produced by organized groups, undermines consumer trust and fair competition on online platforms. These groups employ sophisticated strategies that evade traditional detection methods, particularly in cold-start scenarios involving newly launched products with sparse data. To address this, we propose the \underline{D}iversity- and \underline{S}imilarity-aware \underline{D}ynamic \underline{G}raph \underline{A}ttention-enhanced \underline{G}raph \underline{C}onvolutional \underline{N}etwork (DS-DGA-GCN), a new graph learning model for detecting fake reviewer groups. DS-DGA-GCN achieves robust detection since it focuses on the joint relationships among products, reviews, and reviewers by modeling product-review-reviewer networks. DS-DGA-GCN also achieves adaptive detection by integrating a Network Feature Scoring (NFS) system and a new dynamic graph attention mechanism. The NFS system quantifies network attributes, including neighbor diversity, network self-similarity, as a unified feature score. The dynamic graph attention mechanism improves the adaptability and computational efficiency by captures features related to temporal information, node importance, and global network structure. Extensive experiments conducted on two real-world datasets derived from Amazon and Xiaohongshu demonstrate that DS-DGA-GCN significantly outperforms state-of-the-art baselines, achieving accuracies of up to \textbf{89.8\% and 88.3\%}, respectively.

