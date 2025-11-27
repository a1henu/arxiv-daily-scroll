---
layout: default
title: A Probabilistic Framework for Temporal Distribution Generalization in Industry-Scale Recommender Systems
---

# A Probabilistic Framework for Temporal Distribution Generalization in Industry-Scale Recommender Systems
**arXiv**：[2511.21032v1](https://arxiv.org/abs/2511.21032) · [PDF](https://arxiv.org/pdf/2511.21032.pdf)  
**作者**：Yuxuan Zhu, Cong Fu, Yabo Ni, Anxiang Zeng, Yuan Fang  

**一句话要点**：提出ELBO$_{TDS}$概率框架以解决工业推荐系统中的时间分布泛化问题

**关键词**：时间分布泛化, 概率框架, 自监督学习, 因果图, 工业推荐系统, 数据增强

## 3 点简述
- 核心问题：时间分布偏移导致推荐系统长期准确性下降，现有方法泛化不稳定或数据利用低效
- 方法要点：基于因果图设计自监督变分目标ELBO$_{TDS}$，结合数据增强扩展训练分布
- 实验或效果：在Shopee产品搜索中部署，提升用户GMV 2.33%，实现优越时间泛化

## 摘要（原文）

> Temporal distribution shift (TDS) erodes the long-term accuracy of recommender systems, yet industrial practice still relies on periodic incremental training, which struggles to capture both stable and transient patterns. Existing approaches such as invariant learning and self-supervised learning offer partial solutions but often suffer from unstable temporal generalization, representation collapse, or inefficient data utilization. To address these limitations, we propose ELBO$_\text{TDS}$, a probabilistic framework that integrates seamlessly into industry-scale incremental learning pipelines. First, we identify key shifting factors through statistical analysis of real-world production data and design a simple yet effective data augmentation strategy that resamples these time-varying factors to extend the training support. Second, to harness the benefits of this extended distribution while preventing representation collapse, we model the temporal recommendation scenario using a causal graph and derive a self-supervised variational objective, ELBO$_\text{TDS}$, grounded in the causal structure. Extensive experiments supported by both theoretical and empirical analysis demonstrate that our method achieves superior temporal generalization, yielding a 2.33\% uplift in GMV per user and has been successfully deployed in Shopee Product Search. Code is available at https://github.com/FuCongResearchSquad/ELBO4TDS.

