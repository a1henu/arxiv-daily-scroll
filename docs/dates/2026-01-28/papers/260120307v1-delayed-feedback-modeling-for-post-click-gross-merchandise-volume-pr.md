---
layout: default
title: Delayed Feedback Modeling for Post-Click Gross Merchandise Volume Prediction: Benchmark, Insights and Approaches
---

# Delayed Feedback Modeling for Post-Click Gross Merchandise Volume Prediction: Benchmark, Insights and Approaches
**arXiv**：[2601.20307v1](https://arxiv.org/abs/2601.20307) · [PDF](https://arxiv.org/pdf/2601.20307.pdf)  
**作者**：Xinyu Li, Sishuo Chen, Guipeng Xv, Li Zhang, Mingxuan Luo, Zhangming Chan, Xiang-Rong Sheng, Han Zhu, Jian Xu, Chen Lin  

**一句话要点**：提出READER模型以解决在线广告GMV预测中的延迟反馈问题，并建立TRACE基准数据集。

**关键词**：GMV预测, 延迟反馈建模, 在线流式训练, 复购预测, 基准数据集, 广告排名模型

## 3 点简述
- 核心问题：GMV预测面临延迟反馈挑战，因GMV为连续目标且单点击可导致多次购买，现有研究不足。
- 方法要点：提出READER模型，通过路由器预测复购并激活专家参数，动态校准回归目标以缓解标签不完整导致的低估。
- 实验或效果：在TRACE基准上，READER优于基线，准确率提升2.19%，支持在线流式训练和复购样本单独建模。

## 摘要（原文）

> The prediction objectives of online advertisement ranking models are evolving from probabilistic metrics like conversion rate (CVR) to numerical business metrics like post-click gross merchandise volume (GMV). Unlike the well-studied delayed feedback problem in CVR prediction, delayed feedback modeling for GMV prediction remains unexplored and poses greater challenges, as GMV is a continuous target, and a single click can lead to multiple purchases that cumulatively form the label. To bridge the research gap, we establish TRACE, a GMV prediction benchmark containing complete transaction sequences rising from each user click, which supports delayed feedback modeling in an online streaming manner. Our analysis and exploratory experiments on TRACE reveal two key insights: (1) the rapid evolution of the GMV label distribution necessitates modeling delayed feedback under online streaming training; (2) the label distribution of repurchase samples substantially differs from that of single-purchase samples, highlighting the need for separate modeling. Motivated by these findings, we propose RepurchasE-Aware Dual-branch prEdictoR (READER), a novel GMV modeling paradigm that selectively activates expert parameters according to repurchase predictions produced by a router. Moreover, READER dynamically calibrates the regression target to mitigate under-estimation caused by incomplete labels. Experimental results show that READER yields superior performance on TRACE over baselines, achieving a 2.19% improvement in terms of accuracy. We believe that our study will open up a new avenue for studying online delayed feedback modeling for GMV prediction, and our TRACE benchmark with the gathered insights will facilitate future research and application in this promising direction. Our code and dataset are available at https://github.com/alimama-tech/OnlineGMV .

