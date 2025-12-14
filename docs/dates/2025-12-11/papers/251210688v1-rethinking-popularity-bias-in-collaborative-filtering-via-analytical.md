---
layout: default
title: Rethinking Popularity Bias in Collaborative Filtering via Analytical Vector Decomposition
---

# Rethinking Popularity Bias in Collaborative Filtering via Analytical Vector Decomposition
**arXiv**：[2512.10688v1](https://arxiv.org/abs/2512.10688) · [PDF](https://arxiv.org/pdf/2512.10688.pdf)  
**作者**：Lingfeng Liu, Yixin Song, Dazhong Shen, Bing Yin, Hao Li, Yanyong Zhang, Chao Wang  

**一句话要点**：提出方向性分解与校正框架以解决协同过滤中的流行度偏差几何问题

**关键词**：协同过滤, 流行度偏差, 嵌入几何, 贝叶斯成对排序, 方向性校正, 推荐系统

## 3 点简述
- 揭示流行度偏差是贝叶斯成对排序优化的内在几何伪影，导致嵌入沿流行方向扭曲
- 提出方向性分解与校正框架，通过非对称方向更新在几何源头分离偏好与流行度
- 实验显示框架显著优于现有去偏方法，训练损失降至基线5%以下，提升推荐质量与公平性

## 摘要（原文）

> Popularity bias fundamentally undermines the personalization capabilities of collaborative filtering (CF) models, causing them to disproportionately recommend popular items while neglecting users' genuine preferences for niche content. While existing approaches treat this as an external confounding factor, we reveal that popularity bias is an intrinsic geometric artifact of Bayesian Pairwise Ranking (BPR) optimization in CF models. Through rigorous mathematical analysis, we prove that BPR systematically organizes item embeddings along a dominant "popularity direction" where embedding magnitudes directly correlate with interaction frequency. This geometric distortion forces user embeddings to simultaneously handle two conflicting tasks-expressing genuine preference and calibrating against global popularity-trapping them in suboptimal configurations that favor popular items regardless of individual tastes. We propose Directional Decomposition and Correction (DDC), a universally applicable framework that surgically corrects this embedding geometry through asymmetric directional updates. DDC guides positive interactions along personalized preference directions while steering negative interactions away from the global popularity direction, disentangling preference from popularity at the geometric source. Extensive experiments across multiple BPR-based architectures demonstrate that DDC significantly outperforms state-of-the-art debiasing methods, reducing training loss to less than 5% of heavily-tuned baselines while achieving superior recommendation quality and fairness. Code is available in https://github.com/LingFeng-Liu-AI/DDC.

