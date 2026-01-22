---
layout: default
title: Improving Regret Approximation for Unsupervised Dynamic Environment Generation
---

# Improving Regret Approximation for Unsupervised Dynamic Environment Generation
**arXiv**：[2601.14957v1](https://arxiv.org/abs/2601.14957) · [PDF](https://arxiv.org/pdf/2601.14957.pdf)  
**作者**：Harry Mead, Bruno Lacerda, Jakob Foerster, Nick Hawes  

**一句话要点**：提出DEGen和MNA以改进无监督动态环境生成中的遗憾近似和可扩展性

**关键词**：无监督环境设计, 强化学习, 动态环境生成, 遗憾近似, 可扩展性, 零样本性能

## 3 点简述
- 核心问题：无监督环境设计在环境规模增大时面临信用分配困难和遗憾近似不准确的问题
- 方法要点：引入DEGen提供更密集的奖励信号，并开发MNA作为改进的遗憾近似度量
- 实验或效果：MNA优于现有近似，结合DEGen在更大环境中持续超越现有方法

## 摘要（原文）

> Unsupervised Environment Design (UED) seeks to automatically generate training curricula for reinforcement learning (RL) agents, with the goal of improving generalisation and zero-shot performance. However, designing effective curricula remains a difficult problem, particularly in settings where small subsets of environment parameterisations result in significant increases in the complexity of the required policy. Current methods struggle with a difficult credit assignment problem and rely on regret approximations that fail to identify challenging levels, both of which are compounded as the size of the environment grows. We propose Dynamic Environment Generation for UED (DEGen) to enable a denser level generator reward signal, reducing the difficulty of credit assignment and allowing for UED to scale to larger environment sizes. We also introduce a new regret approximation, Maximised Negative Advantage (MNA), as a significantly improved metric to optimise for, that better identifies more challenging levels. We show empirically that MNA outperforms current regret approximations and when combined with DEGen, consistently outperforms existing methods, especially as the size of the environment grows. We have made all our code available here: https://github.com/HarryMJMead/Dynamic-Environment-Generation-for-UED.

