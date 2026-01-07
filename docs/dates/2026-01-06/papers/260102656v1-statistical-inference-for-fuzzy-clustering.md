---
layout: default
title: Statistical Inference for Fuzzy Clustering
---

# Statistical Inference for Fuzzy Clustering
**arXiv**：[2601.02656v1](https://arxiv.org/abs/2601.02656) · [PDF](https://arxiv.org/pdf/2601.02656.pdf)  
**作者**：Qiuyi Wu, Zihan Zhu, Anru R. Zhang  

**一句话要点**：提出加权模糊c均值框架以解决聚类大小不平衡下的统计推断问题

**关键词**：模糊聚类, 统计推断, 加权模糊c均值, 块状MM算法, 重要性采样, 生物医学数据分析

## 3 点简述
- 针对模糊聚类缺乏统计推断方法的核心问题，提出加权模糊c均值框架
- 通过块状MM算法估计参数，并基于重要性采样近似归一化常数
- 在单细胞RNA-seq和ADNI数据中验证了稳定不确定性量化和生物学意义

## 摘要（原文）

> Clustering is a central tool in biomedical research for discovering heterogeneous patient subpopulations, where group boundaries are often diffuse rather than sharply separated. Traditional methods produce hard partitions, whereas soft clustering methods such as fuzzy $c$-means (FCM) allow mixed memberships and better capture uncertainty and gradual transitions. Despite the widespread use of FCM, principled statistical inference for fuzzy clustering remains limited.
>   We develop a new framework for weighted fuzzy $c$-means (WFCM) for settings with potential cluster size imbalance. Cluster-specific weights rebalance the classical FCM criterion so that smaller clusters are not overwhelmed by dominant groups, and the weighted objective induces a normalized density model with scale parameter $σ$ and fuzziness parameter $m$. Estimation is performed via a blockwise majorize--minimize (MM) procedure that alternates closed-form membership and centroid updates with likelihood-based updates of $(σ,\bw)$. The intractable normalizing constant is approximated by importance sampling using a data-adaptive Gaussian mixture proposal. We further provide likelihood ratio tests for comparing cluster centers and bootstrap-based confidence intervals.
>   We establish consistency and asymptotic normality of the maximum likelihood estimator, validate the method through simulations, and illustrate it using single-cell RNA-seq and Alzheimer disease Neuroimaging Initiative (ADNI) data. These applications demonstrate stable uncertainty quantification and biologically meaningful soft memberships, ranging from well-separated cell populations under imbalance to a graded AD versus non-AD continuum consistent with disease progression.

