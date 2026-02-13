---
layout: default
title: How to Optimize Multispecies Set Predictions in Presence-Absence Modeling ?
---

# How to Optimize Multispecies Set Predictions in Presence-Absence Modeling ?
**arXiv**：[2602.11771v1](https://arxiv.org/abs/2602.11771) · [PDF](https://arxiv.org/pdf/2602.11771.pdf)  
**作者**：Sébastien Gigot--Léandri, Gaétan Morand, Alexis Joly, François Munoz, David Mouillot, Christophe Botella, Maximilien Servajean  

**一句话要点**：提出MaxExp和SSE方法以优化多物种分布模型的二值化预测

**关键词**：物种分布模型, 二值化预测, 多物种优化, MaxExp框架, SSE方法, 生态建模

## 3 点简述
- 核心问题：物种分布模型概率预测二值化步骤常扭曲物种丰度和群落组成估计
- 方法要点：MaxExp通过最大化评估指标直接选择最可能物种组合，SSE基于期望物种丰富度预测组合
- 实验或效果：在三个案例中，MaxExp优于常用阈值方法，SSE提供简单竞争选项

## 摘要（原文）

> Species distribution models (SDMs) commonly produce probabilistic occurrence predictions that must be converted into binary presence-absence maps for ecological inference and conservation planning. However, this binarization step is typically heuristic and can substantially distort estimates of species prevalence and community composition. We present MaxExp, a decision-driven binarization framework that selects the most probable species assemblage by directly maximizing a chosen evaluation metric. MaxExp requires no calibration data and is flexible across several scores. We also introduce the Set Size Expectation (SSE) method, a computationally efficient alternative that predicts assemblages based on expected species richness. Using three case studies spanning diverse taxa, species counts, and performance metrics, we show that MaxExp consistently matches or surpasses widely used thresholding and calibration methods, especially under strong class imbalance and high rarity. SSE offers a simpler yet competitive option. Together, these methods provide robust, reproducible tools for multispecies SDM binarization.

