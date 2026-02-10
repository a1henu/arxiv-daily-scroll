---
layout: default
title: Contrastive Learning for Diversity-Aware Product Recommendations in Retail
---

# Contrastive Learning for Diversity-Aware Product Recommendations in Retail
**arXiv**：[2602.08886v1](https://arxiv.org/abs/2602.08886) · [PDF](https://arxiv.org/pdf/2602.08886.pdf)  
**作者**：Vasileios Karlis, Ezgi Yıldırım, David Vos, Maarten de Rijke  

**一句话要点**：提出基于对比学习的负采样方法，以增强宜家零售推荐系统的商品目录覆盖度，同时保持推荐质量。

**关键词**：对比学习, 负采样, 推荐系统, 多样性推荐, 长尾分布, 流行度偏差

## 3 点简述
- 核心问题：推荐系统在长尾分布和有限商品曝光下，流行商品主导推荐，影响多样性。
- 方法要点：集成对比学习与精心选择的负样本，以缓解流行度偏差，提升目录覆盖。
- 实验或效果：通过离线和在线评估，证明方法提高覆盖度，确保推荐多样性且保持性能。

## 摘要（原文）

> Recommender systems often struggle with long-tail distributions and limited item catalog exposure, where a small subset of popular items dominates recommendations. This challenge is especially critical in large-scale online retail settings with extensive and diverse product assortments. This paper introduces an approach to enhance catalog coverage without compromising recommendation quality in the existing digital recommendation pipeline at IKEA Retail. Drawing inspiration from recent advances in negative sampling to address popularity bias, we integrate contrastive learning with carefully selected negative samples. Through offline and online evaluations, we demonstrate that our method improves catalog coverage, ensuring a more diverse set of recommendations yet preserving strong recommendation performance.

