---
layout: default
title: Bifrost: Steering Strategic Trajectories to Bridge Contextual Gaps for Self-Improving Agents
---

# Bifrost: Steering Strategic Trajectories to Bridge Contextual Gaps for Self-Improving Agents
**arXiv**：[2602.05810v1](https://arxiv.org/abs/2602.05810) · [PDF](https://arxiv.org/pdf/2602.05810.pdf)  
**作者**：Quan M. Tran, Zhuo Huang, Wenbin Zhang, Bo Han, Koji Yatani, Masashi Sugiyama, Tongliang Liu  

**一句话要点**：提出Bifrost方法以解决自主智能体在任务切换中上下文不匹配导致的轨迹重用问题

**关键词**：自主智能体, 轨迹重用, 上下文适应, 表示学习, 自改进方法, 训练免费

## 3 点简述
- 核心问题：任务切换时上下文不匹配，现有方法丢弃或启发式调整轨迹，导致微调成本高或性能不稳定
- 方法要点：基于上下文-轨迹相关性，利用上下文差异在表示层指导轨迹适应，无需训练
- 实验或效果：在多个基准测试中优于现有轨迹重用和微调自改进方法，有效利用历史经验

## 摘要（原文）

> Autonomous agents excel in self-improvement through reflection and iterative refinement, which reuse successful task trajectories as in-context examples to assist subsequent reasoning. However, shifting across tasks often introduces a context mismatch. Hence, existing approaches either discard the trajectories or manipulate them using heuristics, leading to a non-negligible fine-tuning cost or unguaranteed performance. To bridge this gap, we reveal a context-trajectory correlation, where shifts of context are highly parallel with shifts of trajectory. Based on this finding, we propose BrIdge contextual gap FoR imprOvised trajectory STeering (Bifrost), a training-free method that leverages context differences to precisely guide the adaptation of previously solved trajectories towards the target task, mitigating the misalignment caused by context shifts. Our trajectory adaptation is conducted at the representation level using agent hidden states, ensuring trajectory transformation accurately aligns with the target context in a shared space. Across diverse benchmarks, Bifrost consistently outperforms existing trajectory reuse and finetuned self-improvement methods, demonstrating that agents can effectively leverage past experiences despite substantial context shifts.

