---
layout: default
title: Orthogonal Approximate Message Passing with Optimal Spectral Initializations for Rectangular Spiked Matrix Models
---

# Orthogonal Approximate Message Passing with Optimal Spectral Initializations for Rectangular Spiked Matrix Models
**arXiv**：[2512.19334v1](https://arxiv.org/abs/2512.19334) · [PDF](https://arxiv.org/pdf/2512.19334.pdf)  
**作者**：Haohua Chen, Songbin Liu, Junjie Ma  

**一句话要点**：提出正交近似消息传递算法，用于矩形尖峰矩阵模型中的信号估计。

**关键词**：正交近似消息传递, 矩形尖峰矩阵模型, 旋转不变噪声, 状态演化, 谱初始化, 信号估计

## 3 点简述
- 针对矩形尖峰矩阵模型，处理旋转不变噪声下的信号估计问题。
- 建立严格状态演化，设计迭代最优去噪器，并整合谱初始化。
- 算法性能与贝叶斯最优估计器的副本对称预测一致，推测统计最优。

## 摘要（原文）

> We propose an orthogonal approximate message passing (OAMP) algorithm for signal estimation in the rectangular spiked matrix model with general rotationally invariant (RI) noise. We establish a rigorous state evolution that precisely characterizes the algorithm's high-dimensional dynamics and enables the construction of iteration-wise optimal denoisers. Within this framework, we accommodate spectral initializations under minimal assumptions on the empirical noise spectrum. In the rectangular setting, where a single rank-one component typically generates multiple informative outliers, we further propose a procedure for combining these outliers under mild non-Gaussian signal assumptions. For general RI noise models, the predicted performance of the proposed optimal OAMP algorithm agrees with replica-symmetric predictions for the associated Bayes-optimal estimator, and we conjecture that it is statistically optimal within a broad class of iterative estimation methods.

