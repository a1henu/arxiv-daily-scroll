---
layout: default
title: Accelerated Multi-Modal Motion Planning Using Context-Conditioned Diffusion Models
---

# Accelerated Multi-Modal Motion Planning Using Context-Conditioned Diffusion Models
**arXiv**：[2510.14615v1](https://arxiv.org/abs/2510.14615) · [PDF](https://arxiv.org/pdf/2510.14615.pdf)  
**作者**：Edward Sandra, Lander Vanroye, Dries Dirckx, Ruben Cartuyvels, Jan Swevers, Wilm Decré  

**一句话要点**：提出上下文感知运动规划扩散模型以解决机器人运动规划在未知环境中的泛化问题

**关键词**：运动规划, 扩散模型, 上下文条件, 多模态轨迹, 机器人操纵, 泛化能力

## 3 点简述
- 传统运动规划方法在高维状态空间和复杂环境中扩展性差
- 使用无分类器去噪扩散模型，通过注意力机制整合传感器无关上下文信息
- 在7自由度机械臂上验证，泛化至未见环境，生成高质量多模态轨迹，速度远超现有方法

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

