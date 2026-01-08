---
layout: default
title: Stochastic Voronoi Ensembles for Anomaly Detection
---

# Stochastic Voronoi Ensembles for Anomaly Detection
**arXiv**：[2601.03664v1](https://arxiv.org/abs/2601.03664) · [PDF](https://arxiv.org/pdf/2601.03664.pdf)  
**作者**：Yang Cao  

**一句话要点**：提出SVEAD以解决局部密度变化数据集中的异常检测问题

**关键词**：异常检测, Voronoi图, 集成学习, 局部密度, 线性复杂度, 几何方法

## 3 点简述
- 核心问题：现有方法在处理局部密度变化数据集时，难以有效识别局部异常，且存在参数敏感或高计算复杂度问题。
- 方法要点：基于几何洞察，通过构建随机Voronoi图集成，利用归一化单元相对距离加权局部尺度进行异常评分。
- 实验或效果：在45个数据集上验证，SVEAD优于12种先进方法，实现线性时间复杂度和常数空间复杂度。

## 摘要（原文）

> Anomaly detection aims to identify data instances that deviate significantly from majority of data, which has been widely used in fraud detection, network security, and industrial quality control. Existing methods struggle with datasets exhibiting varying local densities: distance-based methods miss local anomalies, while density-based approaches require careful parameter selection and incur quadratic time complexity. We observe that local anomalies, though indistinguishable under global analysis, become conspicuous when the data space is decomposed into restricted regions and each region is examined independently. Leveraging this geometric insight, we propose SVEAD (Stochastic Voronoi Ensembles Anomaly Detector), which constructs ensemble random Voronoi diagrams and scores points by normalized cell-relative distances weighted by local scale. The proposed method achieves linear time complexity and constant space complexity. Experiments on 45 datasets demonstrate that SVEAD outperforms 12 state-of-the-art approaches.

