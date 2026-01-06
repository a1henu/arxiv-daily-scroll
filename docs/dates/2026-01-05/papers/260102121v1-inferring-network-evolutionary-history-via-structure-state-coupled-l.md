---
layout: default
title: Inferring Network Evolutionary History via Structure-State Coupled Learning
---

# Inferring Network Evolutionary History via Structure-State Coupled Learning
**arXiv**：[2601.02121v1](https://arxiv.org/abs/2601.02121) · [PDF](https://arxiv.org/pdf/2601.02121.pdf)  
**作者**：En Xu, Shihe Zhou, Huandong Wang, Jingtao Ding, Yong Li  

**一句话要点**：提出CS²方法，通过结构-状态耦合学习从单网络快照推断演化历史。

**关键词**：网络演化推断, 结构-状态耦合, 稳态动力学, 时序网络分析, 边形成顺序

## 3 点简述
- 核心问题：从单网络快照推断演化历史，现有方法仅依赖拓扑，信息不足且噪声多。
- 方法要点：利用网络稳态动力学作为额外观测，建模结构-状态耦合以提升边形成顺序恢复。
- 实验或效果：在六个真实时序网络上，CS²平均提升边优先准确率4.0%和全局排序一致性7.7%。

## 摘要（原文）

> Inferring a network's evolutionary history from a single final snapshot with limited temporal annotations is fundamental yet challenging. Existing approaches predominantly rely on topology alone, which often provides insufficient and noisy cues. This paper leverages network steady-state dynamics -- converged node states under a given dynamical process -- as an additional and widely accessible observation for network evolution history inference. We propose CS$^2$, which explicitly models structure-state coupling to capture how topology modulates steady states and how the two signals jointly improve edge discrimination for formation-order recovery. Experiments on six real temporal networks, evaluated under multiple dynamical processes, show that CS$^2$ consistently outperforms strong baselines, improving pairwise edge precedence accuracy by 4.0% on average and global ordering consistency (Spearman-$ρ$) by 7.7% on average. CS$^2$ also more faithfully recovers macroscopic evolution trajectories such as clustering formation, degree heterogeneity, and hub growth. Moreover, a steady-state-only variant remains competitive when reliable topology is limited, highlighting steady states as an independent signal for evolution inference.

