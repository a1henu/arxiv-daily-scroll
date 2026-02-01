---
layout: default
title: Zenith: Scaling up Ranking Models for Billion-scale Livestreaming Recommendation
---

# Zenith: Scaling up Ranking Models for Billion-scale Livestreaming Recommendation
**arXiv**：[2601.21285v1](https://arxiv.org/abs/2601.21285) · [PDF](https://arxiv.org/pdf/2601.21285.pdf)  
**作者**：Ruifeng Zhang, Zexi Huang, Zikai Wang, Ke Sun, Bohang Zheng, Zhen Ouyang, Huimin Xie, Phil Shen, Junlin Zhang, Wentao Guo, Qinglei Wang  

**一句话要点**：提出Zenith架构以解决大规模直播推荐中特征交互建模与推理延迟的平衡问题

**关键词**：直播推荐, 特征交互, 模型扩展, 推理效率, A/B测试

## 3 点简述
- 核心问题：推荐系统中高效处理高维特征交互并扩展模型容量，同时避免推理延迟过高
- 方法要点：通过Token Fusion和Token Boost模块处理少量高维Prime Tokens，提升token异质性以实现更好的扩展性
- 实验或效果：在TikTok Live部署A/B测试，CTR AUC提升1.05%，用户质量观看会话增长9.93%

## 摘要（原文）

> Accurately capturing feature interactions is essential in recommender systems, and recent trends show that scaling up model capacity could be a key driver for next-level predictive performance. While prior work has explored various model architectures to capture multi-granularity feature interactions, relatively little attention has been paid to efficient feature handling and scaling model capacity without incurring excessive inference latency. In this paper, we address this by presenting Zenith, a scalable and efficient ranking architecture that learns complex feature interactions with minimal runtime overhead. Zenith is designed to handle a few high-dimensional Prime Tokens with Token Fusion and Token Boost modules, which exhibits superior scaling laws compared to other state-of-the-art ranking methods, thanks to its improved token heterogeneity. Its real-world effectiveness is demonstrated by deploying the architecture to TikTok Live, a leading online livestreaming platform that attracts billions of users globally. Our A/B test shows that Zenith achieves +1.05%/-1.10% in online CTR AUC and Logloss, and realizes +9.93% gains in Quality Watch Session / User and +8.11% in Quality Watch Duration / User.

