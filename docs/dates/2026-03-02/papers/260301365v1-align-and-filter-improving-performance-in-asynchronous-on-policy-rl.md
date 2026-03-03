---
layout: default
title: Align and Filter: Improving Performance in Asynchronous On-Policy RL
---

# Align and Filter: Improving Performance in Asynchronous On-Policy RL
**arXiv**：[2603.01365v1](https://arxiv.org/abs/2603.01365) · [PDF](https://arxiv.org/pdf/2603.01365.pdf)  
**作者**：Homayoun Honari, Roger Creus Castanyer, Michael Przystupa, Michael Noukhovitch, Pablo Samuel Castro, Glen Berseth  

**一句话要点**：提出总变差优势对齐约束策略优化以缓解异步策略强化学习中的策略滞后问题

**关键词**：异步强化学习, 策略滞后, 分布式训练, 策略优化, 总变差优势, LLM推理

## 3 点简述
- 核心问题：分布式训练和高更新频率加剧策略滞后，阻碍策略学习算法扩展
- 方法要点：基于总变差优势对齐约束策略优化，减少行为策略与学习策略的失配
- 实验或效果：在经典强化学习任务和LLM数学推理任务中验证了方法对策略滞后的鲁棒性

## 摘要（原文）

> Distributed training and increasing the gradient update frequency are practical strategies to accelerate learning and improve performance, but both exacerbate a central challenge: \textit{policy lag}, which is the mismatch between the behavior policy generating data and the learning policy being updated. Policy lag can hinder the scaling of on-policy learning algorithms to larger problems. In this paper, we identify the sources of policy lag caused by distributed learning and high update frequency. We use the findings to propose \textit{total Variation-based Advantage aligned Constrained policy Optimization (\methodacronym)} as a practical approach to mitigate policy lag. We empirically validate our method and show that it offers better robustness to policy lag in classic RL tasks and a modern RL for LLM math reasoning task.

