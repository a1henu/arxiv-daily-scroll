---
layout: default
title: Out-of-Distribution Detection Based on Total Variation Estimation
---

# Out-of-Distribution Detection Based on Total Variation Estimation
**arXiv**：[2601.15867v1](https://arxiv.org/abs/2601.15867) · [PDF](https://arxiv.org/pdf/2601.15867.pdf)  
**作者**：Dabiao Ma, Zhiba Su, Jian Yang, Haojun Fei  

**一句话要点**：提出基于总变差估计的TV-OOD方法以提升机器学习模型在分布偏移下的部署安全性

**关键词**：分布外检测, 总变差估计, 图像分类, 机器学习安全, 模型部署

## 3 点简述
- 核心问题：解决实际应用中机器学习模型因分布偏移导致的部署安全问题
- 方法要点：利用总变差网络估计器计算输入对总变差的贡献，定义总变差分数区分分布内外数据
- 实验或效果：在多种模型和数据集上测试，图像分类任务中性能与前沿方法相当或更优

## 摘要（原文）

> This paper introduces a novel approach to securing machine learning model deployments against potential distribution shifts in practical applications, the Total Variation Out-of-Distribution (TV-OOD) detection method. Existing methods have produced satisfactory results, but TV-OOD improves upon these by leveraging the Total Variation Network Estimator to calculate each input's contribution to the overall total variation. By defining this as the total variation score, TV-OOD discriminates between in- and out-of-distribution data. The method's efficacy was tested across a range of models and datasets, consistently yielding results in image classification tasks that were either comparable or superior to those achieved by leading-edge out-of-distribution detection techniques across all evaluation metrics.

