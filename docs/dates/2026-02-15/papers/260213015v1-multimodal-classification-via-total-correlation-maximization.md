---
layout: default
title: Multimodal Classification via Total Correlation Maximization
---

# Multimodal Classification via Total Correlation Maximization
**arXiv**：[2602.13015v1](https://arxiv.org/abs/2602.13015) · [PDF](https://arxiv.org/pdf/2602.13015.pdf)  
**作者**：Feng Yu, Xiangyu Wu, Yang Yang, Jianfeng Lu  

**一句话要点**：提出TCMax方法，通过最大化总相关以缓解多模态分类中的模态竞争问题。

**关键词**：多模态分类, 总相关最大化, 模态竞争, 信息论分析, 特征对齐

## 3 点简述
- 核心问题：多模态联合学习常过拟合某些模态，导致性能低于单模态学习。
- 方法要点：基于信息论分析模态竞争，引入TCNE估计总相关，设计无超参数损失函数TCMax。
- 实验或效果：在广泛实验中，TCMax优于现有联合和单模态学习方法。

## 摘要（原文）

> Multimodal learning integrates data from diverse sensors to effectively harness information from different modalities. However, recent studies reveal that joint learning often overfits certain modalities while neglecting others, leading to performance inferior to that of unimodal learning. Although previous efforts have sought to balance modal contributions or combine joint and unimodal learning, thereby mitigating the degradation of weaker modalities with promising outcomes, few have examined the relationship between joint and unimodal learning from an information-theoretic perspective. In this paper, we theoretically analyze modality competition and propose a method for multimodal classification by maximizing the total correlation between multimodal features and labels. By maximizing this objective, our approach alleviates modality competition while capturing inter-modal interactions via feature alignment. Building on Mutual Information Neural Estimation (MINE), we introduce Total Correlation Neural Estimation (TCNE) to derive a lower bound for total correlation. Subsequently, we present TCMax, a hyperparameter-free loss function that maximizes total correlation through variational bound optimization. Extensive experiments demonstrate that TCMax outperforms state-of-the-art joint and unimodal learning approaches. Our code is available at https://github.com/hubaak/TCMax.

