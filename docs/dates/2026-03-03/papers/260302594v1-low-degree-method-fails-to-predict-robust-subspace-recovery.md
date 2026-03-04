---
layout: default
title: Low-Degree Method Fails to Predict Robust Subspace Recovery
---

# Low-Degree Method Fails to Predict Robust Subspace Recovery
**arXiv**：[2603.02594v1](https://arxiv.org/abs/2603.02594) · [PDF](https://arxiv.org/pdf/2603.02594.pdf)  
**作者**：He Jia, Aravindan Vijayaraghavan  

**一句话要点**：揭示低阶多项式方法在鲁棒子空间恢复问题中预测计算可解性的失败

**关键词**：低阶多项式方法, 鲁棒子空间恢复, 计算复杂度, 反集中性质, 高维统计

## 3 点简述
- 研究低阶多项式框架在预测高维统计问题计算与统计差距时的局限性
- 针对鲁棒子空间恢复问题，展示低阶方法无法预测多项式时间算法的存在
- 提出基于反集中性质的简单鲁棒算法，挑战低阶方法的普适性

## 摘要（原文）

> The low-degree polynomial framework has been highly successful in predicting computational versus statistical gaps for high-dimensional problems in average-case analysis and machine learning. This success has led to the low-degree conjecture, which posits that this method captures the power and limitations of efficient algorithms for a wide class of high-dimensional statistical problems. We identify a natural and basic hypothesis testing problem in $\mathbb{R}^n$ which is polynomial time solvable, but for which the low-degree polynomial method fails to predict its computational tractability even up to degree $k=n^{Ω(1)}$. Moreover, the low-degree moments match exactly up to degree $k=O(\sqrt{\log n/\log\log n})$. Our problem is a special case of the well-studied robust subspace recovery problem. The lower bounds suggest that there is no polynomial time algorithm for this problem. In contrast, we give a simple and robust polynomial time algorithm that solves the problem (and noisy variants of it), leveraging anti-concentration properties of the distribution. Our results suggest that the low-degree method and low-degree moments fail to capture algorithms based on anti-concentration, challenging their universality as a predictor of computational barriers.

