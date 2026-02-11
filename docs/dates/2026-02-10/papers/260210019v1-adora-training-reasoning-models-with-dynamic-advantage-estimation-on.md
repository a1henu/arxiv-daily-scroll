---
layout: default
title: ADORA: Training Reasoning Models with Dynamic Advantage Estimation on Reinforcement Learning
---

# ADORA: Training Reasoning Models with Dynamic Advantage Estimation on Reinforcement Learning
**arXiv**：[2602.10019v1](https://arxiv.org/abs/2602.10019) · [PDF](https://arxiv.org/pdf/2602.10019.pdf)  
**作者**：Qingnan Ren, Shiting Huang, Zhen Fang, Zehui Chen, Lin Chen, Lijun Li, Feng Zhao  

**一句话要点**：提出ADORA框架，通过动态优势估计优化强化学习中的推理模型训练

**关键词**：强化学习, 优势估计, 策略优化, 推理模型, 动态样本分类

## 3 点简述
- 核心问题：静态优势估计导致信用分配低效，影响策略更新和收敛速度
- 方法要点：动态调整优势函数权重，基于在线rollout自适应分类训练样本
- 实验或效果：在几何和数学任务中显著提升长推理性能，无需敏感超参数调优

## 摘要（原文）

> Reinforcement learning has become a cornerstone technique for developing reasoning models in complex tasks, ranging from mathematical problem-solving to imaginary reasoning. The optimization of these models typically relies on policy gradient methods, whose efficacy hinges on the accurate estimation of an advantage function. However, prevailing methods typically employ static advantage estimation, a practice that leads to inefficient credit assignment by neglecting the dynamic utility of training samples over time. This limitation results in suboptimal policy updates, which in turn manifest as slower convergence rates and increased learning instability, as models fail to adapt to evolving sample utilities effectively. To address this problem, we introduce \textbf{ADORA} (\textbf{A}dvantage \textbf{D}ynamics via \textbf{O}nline \textbf{R}ollout \textbf{A}daptation), a novel framework for policy optimization. ADORA dynamically adjusts the advantage function's weighting by adaptively categorizing training data into temporarily advantageous and disadvantageous samples, based on their evolving utility during online model rollouts. This tailored data differentiation strategy allows ADORA to be seamlessly integrated into existing policy optimization algorithms without significant architectural modifications, enabling the policy to prioritize learning from more informative experiences and thereby achieve more efficient policy updates. Extensive evaluations across diverse model families and varying data scales demonstrate that ADORA is a robust and efficient framework. It significantly enhances long reasoning in both geometric and mathematical tasks, consistently achieving notable performance gains without requiring sensitive hyperparameter tuning.

