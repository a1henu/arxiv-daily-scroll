---
layout: default
title: When More Data Doesn't Help: Limits of Adaptation in Multitask Learning
---

# When More Data Doesn't Help: Limits of Adaptation in Multitask Learning
**arXiv**：[2601.20774v1](https://arxiv.org/abs/2601.20774) · [PDF](https://arxiv.org/pdf/2601.20774.pdf)  
**作者**：Steve Hanneke, Mingyue Xu  

**一句话要点**：揭示多任务学习中数据量无法克服适应性的统计极限

**关键词**：多任务学习, 统计极限, 适应不可能性, 样本量, 风险保证, 理论分析

## 3 点简述
- 核心问题：多任务学习在无分布信息时，即使每任务样本量任意大，也无法保证最优风险。
- 方法要点：基于arXiv:2006.15785的改进，建立更强的适应不可能性定理。
- 实验或效果：理论分析表明，多任务学习的困难性不能通过增加每任务数据量来克服。

## 摘要（原文）

> Multitask learning and related frameworks have achieved tremendous success in modern applications. In multitask learning problem, we are given a set of heterogeneous datasets collected from related source tasks and hope to enhance the performance above what we could hope to achieve by solving each of them individually. The recent work of arXiv:2006.15785 has showed that, without access to distributional information, no algorithm based on aggregating samples alone can guarantee optimal risk as long as the sample size per task is bounded.
>   In this paper, we focus on understanding the statistical limits of multitask learning. We go beyond the no-free-lunch theorem in arXiv:2006.15785 by establishing a stronger impossibility result of adaptation that holds for arbitrarily large sample size per task. This improvement conveys an important message that the hardness of multitask learning cannot be overcame by having abundant data per task. We also discuss the notion of optimal adaptivity that may be of future interests.

