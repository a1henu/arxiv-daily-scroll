---
layout: default
title: Telogenesis: Goal Is All U Need
---

# Telogenesis: Goal Is All U Need
**arXiv**：[2603.09476v1](https://arxiv.org/abs/2603.09476) · [PDF](https://arxiv.org/pdf/2603.09476.pdf)  
**作者**：Zhuoran Deng, Yizhi Zhang, Ziyi Zhang, Wan Shen  

**一句话要点**：提出基于认知差距的优先级函数，在无外部目标下生成自适应注意力分配策略。

**关键词**：目标条件系统, 注意力分配, 认知差距, 无监督学习, 自适应策略

## 3 点简述
- 核心问题：注意力优先级能否从智能体内部认知状态自发产生，而非依赖外部目标。
- 方法要点：利用无知、惊讶和过时三种认知差距，构建优先级函数以生成观测目标。
- 实验或效果：在最小环境和模块化世界中验证，优先级策略优于固定策略，并能无监督恢复环境波动结构。

## 摘要（原文）

> Goal-conditioned systems assume goals are provided externally. We ask whether attentional priorities can emerge endogenously from an agent's internal cognitive state. We propose a priority function that generates observation targets from three epistemic gaps: ignorance (posterior variance), surprise (prediction error), and staleness (temporal decay of confidence in unobserved variables). We validate this in two systems: a minimal attention-allocation environment (2,000 runs) and a modular, partially observable world (500 runs). Ablation shows each component is necessary. A key finding is metric-dependent reversal: under global prediction error, coverage-based rotation wins; under change detection latency, priority-guided allocation wins, with advantage growing monotonically with dimensionality (d = -0.95 at N=48, p < 10^-6). Detection latency follows a power law in attention budget, with a steeper exponent for priority-guided allocation (0.55 vs. 0.40). When the decay rate is made learnable per variable, the system spontaneously recovers environmental volatility structure without supervision (t = 22.5, p < 10^-6). We demonstrate that epistemic gaps alone, without external reward, suffice to generate adaptive priorities that outperform fixed strategies and recover latent environmental structure.

