---
layout: default
title: Flow-Opt: Scalable Centralized Multi-Robot Trajectory Optimization with Flow Matching and Differentiable Optimization
---

# Flow-Opt: Scalable Centralized Multi-Robot Trajectory Optimization with Flow Matching and Differentiable Optimization
**arXiv**：[2510.09204v1](https://arxiv.org/abs/2510.09204) · [PDF](https://arxiv.org/pdf/2510.09204.pdf)  
**作者**：Simon Idoko, Arun Kumar Singh  

**一句话要点**：提出Flow-Opt以提升多机器人集中式轨迹优化的计算效率

**关键词**：多机器人轨迹优化, 流匹配, 可微优化, 安全过滤器, 扩散变换器

## 3 点简述
- 核心问题：集中式多机器人轨迹优化在复杂环境中计算不可行
- 方法要点：结合流匹配生成模型与可微安全过滤器进行快速推理
- 实验效果：在数十机器人场景中实现毫秒级轨迹生成，速度快于现有方法

## 摘要（原文）

> Centralized trajectory optimization in the joint space of multiple robots
> allows access to a larger feasible space that can result in smoother
> trajectories, especially while planning in tight spaces. Unfortunately, it is
> often computationally intractable beyond a very small swarm size. In this
> paper, we propose Flow-Opt, a learning-based approach towards improving the
> computational tractability of centralized multi-robot trajectory optimization.
> Specifically, we reduce the problem to first learning a generative model to
> sample different candidate trajectories and then using a learned
> Safety-Filter(SF) to ensure fast inference-time constraint satisfaction. We
> propose a flow-matching model with a diffusion transformer (DiT) augmented with
> permutation invariant robot position and map encoders as the generative model.
> We develop a custom solver for our SF and equip it with a neural network that
> predicts context-specific initialization. The initialization network is trained
> in a self-supervised manner, taking advantage of the differentiability of the
> SF solver. We advance the state-of-the-art in the following respects. First, we
> show that we can generate trajectories of tens of robots in cluttered
> environments in a few tens of milliseconds. This is several times faster than
> existing centralized optimization approaches. Moreover, our approach also
> generates smoother trajectories orders of magnitude faster than competing
> baselines based on diffusion models. Second, each component of our approach can
> be batched, allowing us to solve a few tens of problem instances in a fraction
> of a second. We believe this is a first such result; no existing approach
> provides such capabilities. Finally, our approach can generate a diverse set of
> trajectories between a given set of start and goal locations, which can capture
> different collision-avoidance behaviors.

