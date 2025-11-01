---
layout: default
title: Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling
---

# Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling
**arXiv**：[2510.26139v1](https://arxiv.org/abs/2510.26139) · [PDF](https://arxiv.org/pdf/2510.26139.pdf)  
**作者**：Minseo Kwon, Young J. Kim  

**一句话要点**：提出基于VLM引导和交错采样的运动动力学任务与运动规划框架，以解决长时域问题中的高成本问题。

**关键词**：任务与运动规划, 运动动力学约束, 视觉语言模型, 混合状态树, 采样优化

## 3 点简述
- 核心问题：传统任务与运动规划在长时域问题中因过度运动采样而成本高昂，LLM缺乏3D空间推理能力。
- 方法要点：使用混合状态树统一表示符号和数值状态，结合VLM引导探索和回溯，验证运动动力学约束。
- 实验效果：在模拟和真实环境中，相比传统和LLM方法，平均成功率提升32.14%-1166.67%，规划时间减少。

## 摘要（原文）

> Task and Motion Planning (TAMP) integrates high-level task planning with
> low-level motion feasibility, but existing methods are costly in long-horizon
> problems due to excessive motion sampling. While LLMs provide commonsense
> priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic
> feasibility. We propose a kinodynamic TAMP framework based on a hybrid state
> tree that uniformly represents symbolic and numeric states during planning,
> enabling task and motion decisions to be jointly decided. Kinodynamic
> constraints embedded in the TAMP problem are verified by an off-the-shelf
> motion planner and physics simulator, and a VLM guides exploring a TAMP
> solution and backtracks the search based on visual rendering of the states.
> Experiments on the simulated domains and in the real world show 32.14% -
> 1166.67% increased average success rates compared to traditional and LLM-based
> TAMP planners and reduced planning time on complex problems, with ablations
> further highlighting the benefits of VLM guidance.

