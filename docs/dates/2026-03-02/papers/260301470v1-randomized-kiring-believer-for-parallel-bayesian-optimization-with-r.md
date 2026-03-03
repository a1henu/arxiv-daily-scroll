---
layout: default
title: Randomized Kiring Believer for Parallel Bayesian Optimization with Regret Bounds
---

# Randomized Kiring Believer for Parallel Bayesian Optimization with Regret Bounds
**arXiv**：[2603.01470v1](https://arxiv.org/abs/2603.01470) · [PDF](https://arxiv.org/pdf/2603.01470.pdf)  
**作者**：Shuhei Sugiura, Ichiro Takeuchi, Shion Takeno  

**一句话要点**：提出随机克里金信徒方法以提升并行贝叶斯优化的性能与理论保证

**关键词**：并行贝叶斯优化, 克里金信徒, 随机化方法, 理论保证, 异步并行, 黑盒函数优化

## 3 点简述
- 核心问题：并行贝叶斯优化中现有方法性能不佳或缺乏理论保证
- 方法要点：基于克里金信徒启发式，引入随机化以降低计算复杂度并支持异步并行
- 实验或效果：在合成和基准函数及真实数据模拟器上验证有效性

## 摘要（原文）

> We consider an optimization problem of an expensive-to-evaluate black-box function, in which we can obtain noisy function values in parallel. For this problem, parallel Bayesian optimization (PBO) is a promising approach, which aims to optimize with fewer function evaluations by selecting a diverse input set for parallel evaluation. However, existing PBO methods suffer from poor practical performance or lack theoretical guarantees. In this study, we propose a PBO method, called randomized kriging believer (KB), based on a well-known KB heuristic and inheriting the advantages of the original KB: low computational complexity, a simple implementation, versatility across various BO methods, and applicability to asynchronous parallelization. Furthermore, we show that our randomized KB achieves Bayesian expected regret guarantees. We demonstrate the effectiveness of the proposed method through experiments on synthetic and benchmark functions and emulators of real-world data.

