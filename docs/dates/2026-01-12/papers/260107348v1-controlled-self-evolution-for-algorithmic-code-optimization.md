---
layout: default
title: Controlled Self-Evolution for Algorithmic Code Optimization
---

# Controlled Self-Evolution for Algorithmic Code Optimization
**arXiv**：[2601.07348v1](https://arxiv.org/abs/2601.07348) · [PDF](https://arxiv.org/pdf/2601.07348.pdf)  
**作者**：Tu Hu, Ronghao Chen, Shuo Zhang, Jianghao Yin, Mou Xiao Feng, Jingping Liu, Shaolei Zhang, Wenqi Jiang, Yuqi Fang, Sen Hu, Yi Xu, Huacan Wang  

**一句话要点**：提出受控自进化方法以解决算法代码优化中探索效率低的问题

**关键词**：算法代码优化, 自进化方法, 遗传进化, 探索效率, 反馈引导, 进化记忆

## 3 点简述
- 现有自进化方法因初始化偏差和随机操作导致探索效率低，难以在有限预算内发现更优解
- CSE通过多样化规划初始化、反馈引导的遗传进化和分层进化记忆来提升优化效果
- 在EffiBench-X上实验显示CSE优于基线，早期效率高且持续改进

## 摘要（原文）

> Self-evolution methods enhance code generation through iterative "generate-verify-refine" cycles, yet existing approaches suffer from low exploration efficiency, failing to discover solutions with superior complexity within limited budgets. This inefficiency stems from initialization bias trapping evolution in poor solution regions, uncontrolled stochastic operations lacking feedback guidance, and insufficient experience utilization across tasks.To address these bottlenecks, we propose Controlled Self-Evolution (CSE), which consists of three key components. Diversified Planning Initialization generates structurally distinct algorithmic strategies for broad solution space coverage. Genetic Evolution replaces stochastic operations with feedback-guided mechanisms, enabling targeted mutation and compositional crossover. Hierarchical Evolution Memory captures both successful and failed experiences at inter-task and intra-task levels.Experiments on EffiBench-X demonstrate that CSE consistently outperforms all baselines across various LLM backbones. Furthermore, CSE achieves higher efficiency from early generations and maintains continuous improvement throughout evolution. Our code is publicly available at https://github.com/QuantaAlpha/EvoControl.

