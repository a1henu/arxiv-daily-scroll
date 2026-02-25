---
layout: default
title: Bridging Physically Based Rendering and Diffusion Models with Stochastic Differential Equation
---

# Bridging Physically Based Rendering and Diffusion Models with Stochastic Differential Equation
**arXiv**：[2602.20725v1](https://arxiv.org/abs/2602.20725) · [PDF](https://arxiv.org/pdf/2602.20725.pdf)  
**作者**：Junwei Shu, Wenjie Liu, Changgu Chen, Hantang Liu, Yang Li, Changbo Wang  

**一句话要点**：提出统一随机微分方程框架，以物理渲染控制扩散模型生成结果

**关键词**：随机微分方程, 物理渲染, 扩散模型, 蒙特卡洛积分, 材质编辑

## 3 点简述
- 核心问题：扩散模型缺乏对物理渲染属性的显式控制，而物理渲染缺乏提示驱动的灵活性
- 方法要点：基于中心极限定理，将蒙特卡洛渲染建模为随机微分方程，并扩展到扩散模型
- 实验或效果：在渲染和材质编辑等任务中，实现基于物理的扩散生成控制

## 摘要（原文）

> Diffusion-based image generators excel at producing realistic content from text or image conditions, but they offer only limited explicit control over low-level, physically grounded shading and material properties. In contrast, physically based rendering (PBR) offers fine-grained physical control but lacks prompt-driven flexibility. Although these two paradigms originate from distinct communities, both share a common evolution -- from noisy observations to clean images. In this paper, we propose a unified stochastic formulation that bridges Monte Carlo rendering and diffusion-based generative modeling. First, a general stochastic differential equation (SDE) formulation for Monte Carlo integration under the Central Limit Theorem is modeled. Through instantiation via physically based path tracing, we convert it into a physically grounded SDE representation. Moreover, we provide a systematic analysis of how the physical characteristics of path tracing can be extended to existing diffusion models from the perspective of noise variance. Extensive experiments across multiple tasks show that our method can exert physically grounded control over diffusion-generated results, covering tasks such as rendering and material editing.

