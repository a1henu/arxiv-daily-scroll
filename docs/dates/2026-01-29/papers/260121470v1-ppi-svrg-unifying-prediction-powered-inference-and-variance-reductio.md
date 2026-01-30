---
layout: default
title: PPI-SVRG: Unifying Prediction-Powered Inference and Variance Reduction for Semi-Supervised Optimization
---

# PPI-SVRG: Unifying Prediction-Powered Inference and Variance Reduction for Semi-Supervised Optimization
**arXiv**：[2601.21470v1](https://arxiv.org/abs/2601.21470) · [PDF](https://arxiv.org/pdf/2601.21470.pdf)  
**作者**：Ruicheng Ao, Hongyu Chen, Haoyang Liu, David Simchi-Levi, Will Wei Sun  

**一句话要点**：提出PPI-SVRG以统一预测增强推断与方差缩减，解决半监督优化中标签稀缺问题。

**关键词**：半监督优化, 方差缩减, 预测增强推断, 随机梯度下降, 控制变量法, 标签稀缺

## 3 点简述
- 研究半监督随机优化，标签数据稀缺但预训练模型预测可用。
- 证明PPI与SVRG数学等价，结合两者开发PPI-SVRG方法。
- 实验显示在标签稀缺下MSE降低43-52%，MNIST上测试精度提升2.7-2.9个百分点。

## 摘要（原文）

> We study semi-supervised stochastic optimization when labeled data is scarce but predictions from pre-trained models are available. PPI and SVRG both reduce variance through control variates -- PPI uses predictions, SVRG uses reference gradients. We show they are mathematically equivalent and develop PPI-SVRG, which combines both. Our convergence bound decomposes into the standard SVRG rate plus an error floor from prediction uncertainty. The rate depends only on loss geometry; predictions affect only the neighborhood size. When predictions are perfect, we recover SVRG exactly. When predictions degrade, convergence remains stable but reaches a larger neighborhood. Experiments confirm the theory: PPI-SVRG reduces MSE by 43--52\% under label scarcity on mean estimation benchmarks and improves test accuracy by 2.7--2.9 percentage points on MNIST with only 10\% labeled data.

