---
layout: default
title: Active Causal Experimentalist (ACE): Learning Intervention Strategies via Direct Preference Optimization
---

# Active Causal Experimentalist (ACE): Learning Intervention Strategies via Direct Preference Optimization
**arXiv**：[2602.02451v1](https://arxiv.org/abs/2602.02451) · [PDF](https://arxiv.org/pdf/2602.02451.pdf)  
**作者**：Patrick Cooper, Alvaro Velasquez  

**一句话要点**：提出Active Causal Experimentalist (ACE)以解决因果发现中的自适应实验设计问题

**关键词**：因果发现, 实验设计, 直接偏好优化, 序列决策, 自适应策略, 干预学习

## 3 点简述
- 核心问题：传统因果实验设计方法无法从经验中学习自适应策略，导致干预效率低下
- 方法要点：利用直接偏好优化，通过成对干预比较学习序列策略，避免基于不稳定奖励的强化学习
- 实验或效果：在合成基准、物理模拟和经济数据上，相比基线在相同干预预算下提升70-71%

## 摘要（原文）

> Discovering causal relationships requires controlled experiments, but experimentalists face a sequential decision problem: each intervention reveals information that should inform what to try next. Traditional approaches such as random sampling, greedy information maximization, and round-robin coverage treat each decision in isolation, unable to learn adaptive strategies from experience. We propose Active Causal Experimentalist (ACE), which learns experimental design as a sequential policy. Our key insight is that while absolute information gains diminish as knowledge accumulates (making value-based RL unstable), relative comparisons between candidate interventions remain meaningful throughout. ACE exploits this via Direct Preference Optimization, learning from pairwise intervention comparisons rather than non-stationary reward magnitudes. Across synthetic benchmarks, physics simulations, and economic data, ACE achieves 70-71% improvement over baselines at equal intervention budgets (p < 0.001, Cohen's d ~ 2). Notably, the learned policy autonomously discovers that collider mechanisms require concentrated interventions on parent variables, a theoretically-grounded strategy that emerges purely from experience. This suggests preference-based learning can recover principled experimental strategies, complementing theory with learned domain adaptation.

