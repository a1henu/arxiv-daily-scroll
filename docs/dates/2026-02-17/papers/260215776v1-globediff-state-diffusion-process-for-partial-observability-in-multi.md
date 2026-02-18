---
layout: default
title: GlobeDiff: State Diffusion Process for Partial Observability in Multi-Agent Systems
---

# GlobeDiff: State Diffusion Process for Partial Observability in Multi-Agent Systems
**arXiv**：[2602.15776v1](https://arxiv.org/abs/2602.15776) · [PDF](https://arxiv.org/pdf/2602.15776.pdf)  
**作者**：Yiqin Yang, Xu Yang, Yuhua Jiang, Ni Mu, Hao Hu, Runpeng Xie, Ziyou Zhang, Siyuan Li, Yuan-Hua Ni, Qianchuan Zhao, Bo Xu  

**一句话要点**：提出GlobeDiff算法，通过多模态扩散过程解决多智能体系统中的部分可观测性问题。

**关键词**：多智能体系统, 部分可观测性, 状态推断, 扩散过程, 全局状态估计

## 3 点简述
- 核心问题：多智能体系统中部分可观测性阻碍协调与决策，现有方法如信念估计和通信存在局限。
- 方法要点：将状态推断建模为多模态扩散过程，基于局部观测推断全局状态，减少估计模糊性。
- 实验或效果：理论证明估计误差有界，实验显示能准确推断全局状态，性能优于现有方法。

## 摘要（原文）

> In the realm of multi-agent systems, the challenge of \emph{partial observability} is a critical barrier to effective coordination and decision-making. Existing approaches, such as belief state estimation and inter-agent communication, often fall short. Belief-based methods are limited by their focus on past experiences without fully leveraging global information, while communication methods often lack a robust model to effectively utilize the auxiliary information they provide. To solve this issue, we propose Global State Diffusion Algorithm~(GlobeDiff) to infer the global state based on the local observations. By formulating the state inference process as a multi-modal diffusion process, GlobeDiff overcomes ambiguities in state estimation while simultaneously inferring the global state with high fidelity. We prove that the estimation error of GlobeDiff under both unimodal and multi-modal distributions can be bounded. Extensive experimental results demonstrate that GlobeDiff achieves superior performance and is capable of accurately inferring the global state.

