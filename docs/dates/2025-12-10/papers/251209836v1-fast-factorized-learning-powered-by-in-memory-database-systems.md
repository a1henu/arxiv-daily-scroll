---
layout: default
title: Fast Factorized Learning: Powered by In-Memory Database Systems
---

# Fast Factorized Learning: Powered by In-Memory Database Systems
**arXiv**：[2512.09836v1](https://arxiv.org/abs/2512.09836) · [PDF](https://arxiv.org/pdf/2512.09836.pdf)  
**作者**：Bernhard Stöckl, Maximilian E. Schüle  

**一句话要点**：实现基于内存数据库的因子化学习，加速机器学习训练流程

**关键词**：因子化学习, 内存数据库, 机器学习加速, 数据库内学习, 线性回归, 性能基准测试

## 3 点简述
- 核心问题：因子化学习在内存数据库系统中的性能增益未知，缺乏可复现代码
- 方法要点：在数据库中实现因子化学习，利用共享共因子预计算避免冗余计算
- 实验或效果：在内存数据库上比非因子化学习快70%，比磁盘数据库快100倍

## 摘要（原文）

> Learning models over factorized joins avoids redundant computations by identifying and pre-computing shared cofactors. Previous work has investigated the performance gain when computing cofactors on traditional disk-based database systems. Due to the absence of published code, the experiments could not be reproduced on in-memory database systems. This work describes the implementation when using cofactors for in-database factorized learning. We benchmark our open-source implementation for learning linear regression on factorized joins with PostgreSQL -- as a disk-based database system -- and HyPer -- as an in-memory engine. The evaluation shows a performance gain of factorized learning on in-memory database systems by 70\% to non-factorized learning and by a factor of 100 compared to disk-based database systems. Thus, modern database engines can contribute to the machine learning pipeline by pre-computing aggregates prior to data extraction to accelerate training.

