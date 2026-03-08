---
layout: default
title: Debiasing Sequential Recommendation with Time-aware Inverse Propensity Scoring
---

# Debiasing Sequential Recommendation with Time-aware Inverse Propensity Scoring
**arXiv**：[2603.04986v1](https://arxiv.org/abs/2603.04986) · [PDF](https://arxiv.org/pdf/2603.04986.pdf)  
**作者**：Sirui Huang, Jing Long, Qian Li, Guandong Xu, Qing Li  

**一句话要点**：提出时间感知逆倾向评分以解决序列推荐中的选择与曝光偏差问题

**关键词**：序列推荐, 逆倾向评分, 时间感知建模, 选择偏差, 曝光偏差, 反事实推理

## 3 点简述
- 核心问题：序列推荐忽略物品曝光，导致选择偏差和曝光偏差，无法区分未曝光与不感兴趣物品。
- 方法要点：引入时间感知逆倾向评分，动态建模序列依赖性和时间动态，以更准确估计用户偏好。
- 实验或效果：作为插件增强多种序列推荐器性能，实验验证其有效性，代码将公开。

## 摘要（原文）

> Sequential Recommendation (SR) predicts users next interactions by modeling the temporal order of their historical behaviors. Existing approaches, including traditional sequential models and generative recommenders, achieve strong performance but primarily rely on explicit interactions such as clicks or purchases while overlooking item exposures. This ignorance introduces selection bias, where exposed but unclicked items are misinterpreted as disinterest, and exposure bias, where unexposed items are treated as irrelevant. Effectively addressing these biases requires distinguishing between items that were "not exposed" and those that were "not of interest", which cannot be reliably inferred from correlations in historical data. Counterfactual reasoning provides a natural solution by estimating user preferences under hypothetical exposure, and Inverse Propensity Scoring (IPS) is a common tool for such estimation. However, conventional IPS methods are static and fail to capture the sequential dependencies and temporal dynamics of user behavior. To overcome these limitations, we propose Time aware Inverse Propensity Scoring (TIPS). Unlike traditional static IPS, TIPS effectively accounts for sequential dependencies and temporal dynamics, thereby capturing user preferences more accurately. Extensive experiments show that TIPS consistently enhances recommendation performance as a plug-in for various sequential recommenders. Our code will be publicly available upon acceptance.

