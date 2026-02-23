---
layout: default
title: Box Thirding: Anytime Best Arm Identification under Insufficient Sampling
---

# Box Thirding: Anytime Best Arm Identification under Insufficient Sampling
**arXiv**：[2602.18186v1](https://arxiv.org/abs/2602.18186) · [PDF](https://arxiv.org/pdf/2602.18186.pdf)  
**作者**：Seohwa Hwang, Junyong Park  

**一句话要点**：提出Box Thirding算法，用于固定预算下的大规模臂识别与随时最佳臂识别。

**关键词**：最佳臂识别, 固定预算, 大规模臂, 随时算法, 三元比较, 简单遗憾

## 3 点简述
- 核心问题：固定预算下，臂数过多时无法穷举评估，需高效识别最佳臂。
- 方法要点：采用迭代三元比较，每轮比较三个臂，保留最佳、推迟中位、丢弃最弱。
- 实验或效果：在New Yorker Cartoon Caption Contest数据集上，简单遗憾优于现有方法。

## 摘要（原文）

> We introduce Box Thirding (B3), a flexible and efficient algorithm for Best Arm Identification (BAI) under fixed-budget constraints. It is designed for both anytime BAI and scenarios with large N, where the number of arms is too large for exhaustive evaluation within a limited budget T. The algorithm employs an iterative ternary comparison: in each iteration, three arms are compared--the best-performing arm is explored further, the median is deferred for future comparisons, and the weakest is discarded. Even without prior knowledge of T, B3 achieves an epsilon-best arm misidentification probability comparable to Successive Halving (SH), which requires T as a predefined parameter, applied to a randomly selected subset of c0 arms that fit within the budget. Empirical results show that B3 outperforms existing methods under limited-budget constraints in terms of simple regret, as demonstrated on the New Yorker Cartoon Caption Contest dataset.

