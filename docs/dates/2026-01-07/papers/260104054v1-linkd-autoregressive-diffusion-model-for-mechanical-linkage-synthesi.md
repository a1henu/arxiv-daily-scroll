---
layout: default
title: LinkD: AutoRegressive Diffusion Model for Mechanical Linkage Synthesis
---

# LinkD: AutoRegressive Diffusion Model for Mechanical Linkage Synthesis
**arXiv**：[2601.04054v1](https://arxiv.org/abs/2601.04054) · [PDF](https://arxiv.org/pdf/2601.04054.pdf)  
**作者**：Yayati Jadhav, Amir Barati Farimani  

**一句话要点**：提出自回归扩散模型LinkD，以解决机械连杆机构逆设计中的轨迹到配置映射难题。

**关键词**：机械连杆合成, 自回归扩散模型, 图生成, 逆设计, 计算运动学

## 3 点简述
- 核心问题：机械连杆设计需处理节点位置、拓扑结构和运动约束的复杂耦合，传统方法计算困难。
- 方法要点：结合因果Transformer和去噪扩散概率模型，自回归生成图结构，支持自适应纠错。
- 实验或效果：成功合成含20个节点的连杆系统，可扩展至任意节点数，超越传统优化方法。

## 摘要（原文）

> Designing mechanical linkages to achieve target end-effector trajectories presents a fundamental challenge due to the intricate coupling between continuous node placements, discrete topological configurations, and nonlinear kinematic constraints. The highly nonlinear motion-to-configuration relationship means small perturbations in joint positions drastically alter trajectories, while the combinatorially expanding design space renders conventional optimization and heuristic methods computationally intractable. We introduce an autoregressive diffusion framework that exploits the dyadic nature of linkage assembly by representing mechanisms as sequentially constructed graphs, where nodes correspond to joints and edges to rigid links. Our approach combines a causal transformer with a Denoising Diffusion Probabilistic Model (DDPM), both conditioned on target trajectories encoded via a transformer encoder. The causal transformer autoregressively predicts discrete topology node-by-node, while the DDPM refines each node's spatial coordinates and edge connectivity to previously generated nodes. This sequential generation enables adaptive trial-and-error synthesis where problematic nodes exhibiting kinematic locking or collisions can be selectively regenerated, allowing autonomous correction of degenerate configurations during design. Our graph-based, data-driven methodology surpasses traditional optimization approaches, enabling scalable inverse design that generalizes to mechanisms with arbitrary node counts. We demonstrate successful synthesis of linkage systems containing up to 20 nodes with extensibility to N-node architectures. This work advances autoregressive graph generation methodologies and computational kinematic synthesis, establishing new paradigms for scalable inverse design of complex mechanical systems.

