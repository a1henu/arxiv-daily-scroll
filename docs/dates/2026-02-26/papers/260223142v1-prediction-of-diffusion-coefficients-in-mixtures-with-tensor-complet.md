---
layout: default
title: Prediction of Diffusion Coefficients in Mixtures with Tensor Completion
---

# Prediction of Diffusion Coefficients in Mixtures with Tensor Completion
**arXiv**：[2602.23142v1](https://arxiv.org/abs/2602.23142) · [PDF](https://arxiv.org/pdf/2602.23142.pdf)  
**作者**：Zeno Romero, Kerstin Münnemann, Hans Hasse, Fabian Jirasek  

**一句话要点**：提出混合张量补全方法以预测二元混合物中温度依赖的无限稀释扩散系数

**关键词**：张量补全, 扩散系数预测, 温度依赖建模, 贝叶斯训练, 主动学习, 无限稀释

## 3 点简述
- 核心问题：现有矩阵补全方法仅限单温度预测，且依赖高质量实验数据，难以准确预测温度依赖的扩散系数。
- 方法要点：采用Tucker分解的混合张量补全方法，结合贝叶斯训练框架和SEGWE模型先验知识，实现温度线性外推。
- 实验或效果：通过主动学习扩展实验数据库，结合新测量数据，显著提升预测准确性，优于现有模型。

## 摘要（原文）

> Predicting diffusion coefficients in mixtures is crucial for many applications, as experimental data remain scarce, and machine learning (ML) offers promising alternatives to established semi-empirical models. Among ML models, matrix completion methods (MCMs) have proven effective in predicting thermophysical properties, including diffusion coefficients in binary mixtures. However, MCMs are restricted to single-temperature predictions, and their accuracy depends strongly on the availability of high-quality experimental data for each temperature of interest. In this work, we address this challenge by presenting a hybrid tensor completion method (TCM) for predicting temperature-dependent diffusion coefficients at infinite dilution in binary mixtures. The TCM employs a Tucker decomposition and is jointly trained on experimental data for diffusion coefficients at infinite dilution in binary systems at 298 K, 313 K, and 333 K. Predictions from the semi-empirical SEGWE model serve as prior knowledge within a Bayesian training framework. The TCM then extrapolates linearly to any temperature between 268 K and 378 K, achieving markedly improved prediction accuracy compared to established models across all studied temperatures. To further enhance predictive performance, the experimental database was expanded using active learning (AL) strategies for targeted acquisition of new diffusion data by pulsed-field gradient (PFG) NMR measurements. Diffusion coefficients at infinite dilution in 19 solute + solvent systems were measured at 298 K, 313 K, and 333 K. Incorporating these results yields a substantial improvement in the TCM's predictive accuracy. These findings highlight the potential of combining data-efficient ML methods with adaptive experimentation to advance predictive modeling of transport properties.

