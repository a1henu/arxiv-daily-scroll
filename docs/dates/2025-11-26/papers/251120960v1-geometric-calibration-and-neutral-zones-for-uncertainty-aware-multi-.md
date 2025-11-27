---
layout: default
title: Geometric Calibration and Neutral Zones for Uncertainty-Aware Multi-Class Classification
---

# Geometric Calibration and Neutral Zones for Uncertainty-Aware Multi-Class Classification
**arXiv**：[2511.20960v1](https://arxiv.org/abs/2511.20960) · [PDF](https://arxiv.org/pdf/2511.20960.pdf)  
**作者**：Soumojit Das, Nairanjana Dasgupta, Prashanta Dutta  

**一句话要点**：提出几何校准与中性区域框架，用于多类分类的不确定性感知决策。

**关键词**：概率校准, 信息几何, 多类分类, 不确定性量化, 中性区域, Fisher-Rao度量

## 3 点简述
- 核心问题：AI系统在不确定时易出错，缺乏可靠的不确定性处理机制。
- 方法要点：基于Fisher-Rao度量在概率单纯形上构建ALR校准映射，定义几何可靠性分数。
- 实验或效果：在AAV分类中，捕获72.5%错误并延迟34.5%样本，提升操作性能。

## 摘要（原文）

> Modern artificial intelligence systems make critical decisions yet often fail silently when uncertain. We develop a geometric framework for post-hoc calibration of neural network probability outputs, treating probability vectors as points on the $(c-1)$-dimensional probability simplex equipped with the Fisher--Rao metric. Our approach yields Additive Log-Ratio (ALR) calibration maps that reduce exactly to Platt scaling for binary problems (Proposition~1) while extending naturally to multi-class settings -- providing a principled generalization that existing methods lack. Complementing calibration, we define geometric reliability scores based on Fisher--Rao distance and construct neutral zones for principled deferral of uncertain predictions.
>   Theoretical contributions include: (i) consistency of the calibration estimator at rate $O_p(n^{-1/2})$ via M-estimation theory (Theorem~1), and (ii) tight concentration bounds for reliability scores with explicit sub-Gaussian parameters enabling sample size calculations for validation set design (Theorem~2). We conjecture Neyman--Pearson optimality of our neutral zone construction based on connections to Bhattacharyya coefficients. Empirical validation on Adeno-Associated Virus classification demonstrates that the two-stage framework (calibration followed by reliability-based deferral) captures 72.5\% of errors while deferring 34.5\% of samples. Notably, this operational gain is achievable with any well-calibrated probability output; the contribution of geometric calibration lies in its theoretical foundations rather than empirical superiority over simpler alternatives. This work bridges information geometry and statistical learning, offering formal guarantees relevant to applications requiring rigorous validation.

