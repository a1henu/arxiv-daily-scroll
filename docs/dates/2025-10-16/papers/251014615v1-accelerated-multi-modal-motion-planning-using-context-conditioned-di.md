---
layout: default
title: Accelerated Multi-Modal Motion Planning Using Context-Conditioned Diffusion Models
---

# Accelerated Multi-Modal Motion Planning Using Context-Conditioned Diffusion Models
**arXiv**：[2510.14615v1](https://arxiv.org/abs/2510.14615) · [PDF](https://arxiv.org/pdf/2510.14615.pdf)  
**作者**：Edward Sandra, Lander Vanroye, Dries Dirckx, Ruben Cartuyvels, Jan Swevers, Wilm Decré  

**一句话要点**：提出CAMPD方法，利用上下文条件扩散模型解决机器人运动规划在未知环境中的泛化问题。

**关键词**：机器人运动规划, 扩散模型, 上下文条件, 多模态轨迹生成, 泛化能力, U-Net架构

## 3 点简述
- 核心问题：传统运动规划方法在高维状态空间和复杂环境中扩展性差，且现有扩散模型方法难以泛化到未见环境。
- 方法要点：使用分类器自由去噪扩散模型，通过注意力机制整合传感器无关上下文信息，实现多模态轨迹生成。
- 实验或效果：在7自由度机械臂上评估，相比现有方法，泛化能力更强、轨迹质量高且计算时间大幅减少。

## 摘要（原文）

> Classical methods in robot motion planning, such as sampling-based and
> optimization-based methods, often struggle with scalability towards
> higher-dimensional state spaces and complex environments. Diffusion models,
> known for their capability to learn complex, high-dimensional and multi-modal
> data distributions, provide a promising alternative when applied to motion
> planning problems and have already shown interesting results. However, most of
> the current approaches train their model for a single environment, limiting
> their generalization to environments not seen during training. The techniques
> that do train a model for multiple environments rely on a specific camera to
> provide the model with the necessary environmental information and therefore
> always require that sensor. To effectively adapt to diverse scenarios without
> the need for retraining, this research proposes Context-Aware Motion Planning
> Diffusion (CAMPD). CAMPD leverages a classifier-free denoising probabilistic
> diffusion model, conditioned on sensor-agnostic contextual information. An
> attention mechanism, integrated in the well-known U-Net architecture,
> conditions the model on an arbitrary number of contextual parameters. CAMPD is
> evaluated on a 7-DoF robot manipulator and benchmarked against state-of-the-art
> approaches on real-world tasks, showing its ability to generalize to unseen
> environments and generate high-quality, multi-modal trajectories, at a fraction
> of the time required by existing methods.

