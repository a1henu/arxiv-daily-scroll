---
layout: default
title: Efficient Cross-Architecture Knowledge Transfer for Large-Scale Online User Response Prediction
---

# Efficient Cross-Architecture Knowledge Transfer for Large-Scale Online User Response Prediction
**arXiv**：[2602.01775v1](https://arxiv.org/abs/2602.01775) · [PDF](https://arxiv.org/pdf/2602.01775.pdf)  
**作者**：Yucheng Wu, Yuekui Yang, Hongzheng Li, Anan Liu, Jian Xiao, Junjie Zhai, Huan Yu, Shaoping Ma, Leye Wang  

**一句话要点**：提出CrossAdapt框架以解决大规模在线用户响应预测中跨架构知识转移的高成本和性能下降问题

**关键词**：用户响应预测, 知识蒸馏, 跨架构转移, 嵌入表优化, 在线学习, 大规模部署

## 3 点简述
- 核心问题：大规模用户响应预测系统部署新架构时，因重训练成本高和数据保留限制导致性能下降
- 方法要点：采用两阶段框架，离线阶段通过维度自适应投影和渐进蒸馏快速转移嵌入，在线阶段使用非对称协同蒸馏和分布感知适应机制
- 实验或效果：在三个公共数据集上提升AUC 0.27-0.43%，减少训练时间43-71%，并在腾讯微信频道大规模部署中有效缓解性能退化

## 摘要（原文）

> Deploying new architectures in large-scale user response prediction systems incurs high model switching costs due to expensive retraining on massive historical data and performance degradation under data retention constraints. Existing knowledge distillation methods struggle with architectural heterogeneity and the prohibitive cost of transferring large embedding tables. We propose CrossAdapt, a two-stage framework for efficient cross-architecture knowledge transfer. The offline stage enables rapid embedding transfer via dimension-adaptive projections without iterative training, combined with progressive network distillation and strategic sampling to reduce computational cost. The online stage introduces asymmetric co-distillation, where students update frequently while teachers update infrequently, together with a distribution-aware adaptation mechanism that dynamically balances historical knowledge preservation and fast adaptation to evolving data. Experiments on three public datasets show that CrossAdapt achieves 0.27-0.43% AUC improvements while reducing training time by 43-71%. Large-scale deployment on Tencent WeChat Channels (~10M daily samples) further demonstrates its effectiveness, significantly mitigating AUC degradation, LogLoss increase, and prediction bias compared to standard distillation baselines.

