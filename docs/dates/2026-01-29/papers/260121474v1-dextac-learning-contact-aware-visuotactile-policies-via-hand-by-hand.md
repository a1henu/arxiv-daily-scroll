---
layout: default
title: DexTac: Learning Contact-aware Visuotactile Policies via Hand-by-hand Teaching
---

# DexTac: Learning Contact-aware Visuotactile Policies via Hand-by-hand Teaching
**arXiv**：[2601.21474v1](https://arxiv.org/abs/2601.21474) · [PDF](https://arxiv.org/pdf/2601.21474.pdf)  
**作者**：Xingyu Zhang, Chaofan Zhang, Boyue Zhang, Zhinan Peng, Shaowei Cui, Shuo Wang  

**一句话要点**：提出DexTac框架，通过手把手教学学习接触感知的视觉触觉策略，以解决灵巧操作中触觉信息低维的问题。

**关键词**：灵巧操作, 触觉感知, 动觉教学, 策略学习, 接触密集型任务

## 3 点简述
- 核心问题：现有灵巧操作数据收集系统触觉信息低维，难以支持接触密集型任务。
- 方法要点：基于动觉教学捕获多维触觉数据，整合到策略网络中实现接触感知的自主操作。
- 实验或效果：在注射任务中达到91.67%成功率，高精度场景下优于仅用力的基线31.67%。

## 摘要（原文）

> For contact-intensive tasks, the ability to generate policies that produce comprehensive tactile-aware motions is essential. However, existing data collection and skill learning systems for dexterous manipulation often suffer from low-dimensional tactile information. To address this limitation, we propose DexTac, a visuo-tactile manipulation learning framework based on kinesthetic teaching. DexTac captures multi-dimensional tactile data-including contact force distributions and spatial contact regions-directly from human demonstrations. By integrating these rich tactile modalities into a policy network, the resulting contact-aware agent enables a dexterous hand to autonomously select and maintain optimal contact regions during complex interactions. We evaluate our framework on a challenging unimanual injection task. Experimental results demonstrate that DexTac achieves a 91.67% success rate. Notably, in high-precision scenarios involving small-scale syringes, our approach outperforms force-only baselines by 31.67%. These results underscore that learning multi-dimensional tactile priors from human demonstrations is critical for achieving robust, human-like dexterous manipulation in contact-rich environments.

