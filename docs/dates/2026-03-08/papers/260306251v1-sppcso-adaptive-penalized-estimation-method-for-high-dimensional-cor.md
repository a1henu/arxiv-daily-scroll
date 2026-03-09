---
layout: default
title: SPPCSO: Adaptive Penalized Estimation Method for High-Dimensional Correlated Data
---

# SPPCSO: Adaptive Penalized Estimation Method for High-Dimensional Correlated Data
**arXiv**：[2603.06251v1](https://arxiv.org/abs/2603.06251) · [PDF](https://arxiv.org/pdf/2603.06251.pdf)  
**作者**：Ying Hu, Hu Yang  

**一句话要点**：提出SPPCSO方法以解决高维相关数据中高噪声下的模型不稳定问题

**关键词**：高维数据, 变量选择, 主成分回归, L1正则化, 模型稳定性, 基因表达分析

## 3 点简述
- 核心问题：高维相关数据中的多重共线性导致模型不稳定和预测精度下降
- 方法要点：结合单参数主成分回归和L1正则化，自适应调整收缩因子以平衡变量选择和系数估计
- 实验或效果：在数值实验中稳定估计，准确区分信号与噪声变量，并在基因表达数据分析中识别疾病相关基因

## 摘要（原文）

> With the rise of high-dimensional correlated data, multicollinearity poses a significant challenge to model stability, often leading to unstable estimation and reduced predictive accuracy. This work proposes the Single-Parametric Principal Component Selection Operator (SPPCSO), an innovative penalized estimation method that integrates single-parametric principal component regression and $L_{1}$ regularization to adaptively adjust the shrinkage factor by incorporating principal component information. This approach achieves a balance between variable selection and coefficient estimation, ensuring model stability and robust estimation even in high-dimensional, high-noise environments. The primary contribution lies in addressing the instability of traditional variable selection methods when applied to high-noise, high-dimensional correlated data. Theoretically, our method exhibits selection consistency and achieves a smaller estimation error bound compared to traditional penalized estimation approaches. Extensive numerical experiments demonstrate that SPPCSO not only delivers stable and reliable estimation in high-noise settings but also accurately distinguishes signal variables from noise variables in group-effect structured data with highly correlated noise variables, effectively eliminating redundant variables and achieving more stable variable selection. Furthermore, SPPCSO successfully identifies disease-associated genes in gene expression data analysis, showcasing strong practical value. The results indicate that SPPCSO serves as an ideal tool for high-dimensional variable selection, offering an efficient and interpretable solution for modeling correlated data.

