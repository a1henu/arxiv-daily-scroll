---
layout: default
title: Advantages and limitations in the use of transfer learning for individual treatment effects in causal machine learning
---

# Advantages and limitations in the use of transfer learning for individual treatment effects in causal machine learning
**arXiv**：[2512.16489v1](https://arxiv.org/abs/2512.16489) · [PDF](https://arxiv.org/pdf/2512.16489.pdf)  
**作者**：Seyda Betul Aydin, Holger Brandt  

**一句话要点**：提出TL-TARNet，通过迁移学习改进小样本个体治疗效果估计

**关键词**：个体治疗效果, 迁移学习, 因果机器学习, 小样本估计, TARNet

## 3 点简述
- 核心问题：小样本下个体治疗效果估计偏差大，外部有效性受限
- 方法要点：基于TARNet，利用源数据集知识迁移至目标环境
- 实验或效果：模拟和实证显示迁移学习减少误差和偏差，提升估计准确性

## 摘要（原文）

> Generalizing causal knowledge across diverse environments is challenging, especially when estimates from large-scale datasets must be applied to smaller or systematically different contexts, where external validity is critical. Model-based estimators of individual treatment effects (ITE) from machine learning require large sample sizes, limiting their applicability in domains such as behavioral sciences with smaller datasets. We demonstrate how estimation of ITEs with Treatment Agnostic Representation Networks (TARNet; Shalit et al., 2017) can be improved by leveraging knowledge from source datasets and adapting it to new settings via transfer learning (TL-TARNet; Aloui et al., 2023). In simulations that vary source and sample sizes and consider both randomized and non-randomized intervention target settings, the transfer-learning extension TL-TARNet improves upon standard TARNet, reducing ITE error and attenuating bias when a large unbiased source is available and target samples are small. In an empirical application using the India Human Development Survey (IHDS-II), we estimate the effect of mothers' firewood collection time on children's weekly study time; transfer learning pulls the target mean ITEs toward the source ITE estimate, reducing bias in the estimates obtained without transfer. These results suggest that transfer learning for causal models can improve the estimation of ITE in small samples.

