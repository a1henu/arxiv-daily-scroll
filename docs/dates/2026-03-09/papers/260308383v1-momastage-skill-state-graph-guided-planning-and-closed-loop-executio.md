---
layout: default
title: MoMaStage: Skill-State Graph Guided Planning and Closed-Loop Execution for Long-Horizon Indoor Mobile Manipulation
---

# MoMaStage: Skill-State Graph Guided Planning and Closed-Loop Execution for Long-Horizon Indoor Mobile Manipulation
**arXiv**：[2603.08383v1](https://arxiv.org/abs/2603.08383) · [PDF](https://arxiv.org/pdf/2603.08383.pdf)  
**作者**：Chenxu Li, Zixuan Chen, Yetao Li, Jiapeng Xu, Hongyu Ding, Jieqi Shi, Jing Huo, Yang Gao  

**一句话要点**：提出MoMaStage框架，通过技能状态图引导规划与闭环执行，解决室内移动操作的长时程挑战。

**关键词**：室内移动操作, 长时程规划, 技能状态图, 视觉语言模型, 闭环执行, 语义重规划

## 3 点简述
- 核心问题：长时程室内移动操作中，级联错误和泛化能力不足导致逻辑一致性和适应性差。
- 方法要点：结合视觉语言模型、分层技能库和技能状态图，实现结构化任务分解与闭环语义重规划。
- 实验或效果：在仿真和真实环境中优于基线，显著提高规划成功率和整体任务成功率，降低计算开销。

## 摘要（原文）

> Indoor mobile manipulation (MoMA) enables robots to translate natural language instructions into physical actions, yet long-horizon execution remains challenging due to cascading errors and limited generalization across diverse environments. Learning-based approaches often fail to maintain logical consistency over extended horizons, while methods relying on explicit scene representations impose rigid structural assumptions that reduce adaptability in dynamic settings. To address these limitations, we propose MoMaStage, a structured vision-language framework for long-horizon MoMA that eliminates the need for explicit scene mapping. MoMaStage grounds a Vision-Language Model (VLM) within a Hierarchical Skill Library and a topology-aware Skill-State Graph, constraining task decomposition and skill composition within a feasible transition space. This structured grounding ensures that generated plans remain logically consistent and topologically valid with respect to the agent's evolving physical state. To enhance robustness, MoMaStage incorporates a closed-loop execution mechanism that monitors proprioceptive feedback and triggers graph-constrained semantic replanning when deviations are detected, maintaining alignment between planned skills and physical outcomes. Extensive experiments in physics-rich simulations and real-world environments demonstrate that MoMaStage outperforms state-of-the-art baselines, achieving substantially higher planning success, reducing token overhead, and significantly improving overall task success rates in long-horizon mobile manipulation. Video demonstrations are available on the project website: https://chenxuli-cxli.github.io/MoMaStage/.

