---
layout: default
title: Position: Universal Time Series Foundation Models Rest on a Category Error
---

# Position: Universal Time Series Foundation Models Rest on a Category Error
**arXiv**：[2602.05287v1](https://arxiv.org/abs/2602.05287) · [PDF](https://arxiv.org/pdf/2602.05287.pdf)  
**作者**：Xilin Dai, Wanxu Cai, Zhijian Xu, Qiang Xu  

**一句话要点**：提出因果控制代理范式以解决时间序列通用基础模型的范畴错误问题

**关键词**：时间序列建模, 范畴错误, 自回归盲界, 因果控制代理, 分布漂移, 基准评估

## 3 点简述
- 核心问题：时间序列通用基础模型存在范畴错误，误将结构容器视为语义模态，导致模型在分布漂移下泛化失败
- 方法要点：引入自回归盲界理论，证明仅依赖历史的模型无法预测干预驱动的机制转变，并倡导因果控制代理范式
- 实验或效果：未知，但呼吁基准从零样本精度转向漂移适应速度，以优先考虑鲁棒的控制理论系统

## 摘要（原文）

> This position paper argues that the pursuit of "Universal Foundation Models for Time Series" rests on a fundamental category error, mistaking a structural Container for a semantic Modality. We contend that because time series hold incompatible generative processes (e.g., finance vs. fluid dynamics), monolithic models degenerate into expensive "Generic Filters" that fail to generalize under distributional drift. To address this, we introduce the "Autoregressive Blindness Bound," a theoretical limit proving that history-only models cannot predict intervention-driven regime shifts. We advocate replacing universality with a Causal Control Agent paradigm, where an agent leverages external context to orchestrate a hierarchy of specialized solvers, from frozen domain experts to lightweight Just-in-Time adaptors. We conclude by calling for a shift in benchmarks from "Zero-Shot Accuracy" to "Drift Adaptation Speed" to prioritize robust, control-theoretic systems.

