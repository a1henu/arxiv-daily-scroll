---
layout: default
title: GlueNN: gluing patchwise analytic solutions with neural networks
---

# GlueNN: gluing patchwise analytic solutions with neural networks
**arXiv**：[2601.05889v1](https://arxiv.org/abs/2601.05889) · [PDF](https://arxiv.org/pdf/2601.05889.pdf)  
**作者**：Doyoung Kim, Donghee Lee, Hye-Sung Lee, Jiheon Lee, Jaeok Yi  

**一句话要点**：提出GlueNN框架，通过神经网络学习尺度依赖系数函数以解决物理工程中微分方程分片解析解匹配失效问题。

**关键词**：微分方程求解, 神经网络框架, 渐近解析解, 尺度依赖系数, 物理工程应用, 全局解插值

## 3 点简述
- 核心问题：复杂微分方程分片近似解析解在匹配边界处可能失效，导致全局解不准确。
- 方法要点：将渐近解析解的积分常数提升为尺度依赖函数，用神经网络约束以平滑插值渐近区域。
- 实验或效果：在化学动力学和宇宙学问题中验证，准确生成全局解，优于传统匹配方法。

## 摘要（原文）

> In many problems in physics and engineering, one encounters complicated differential equations with strongly scale-dependent terms for which exact analytical or numerical solutions are not available. A common strategy is to divide the domain into several regions (patches) and simplify the equation in each region. When approximate analytic solutions can be obtained in each patch, they are then matched at the interfaces to construct a global solution. However, this patching procedure can fail to reproduce the correct solution, since the approximate forms may break down near the matching boundaries. In this work, we propose a learning framework in which the integration constants of asymptotic analytic solutions are promoted to scale-dependent functions. By constraining these coefficient functions with the original differential equation over the domain, the network learns a globally valid solution that smoothly interpolates between asymptotic regimes, eliminating the need for arbitrary boundary matching. We demonstrate the effectiveness of this framework in representative problems from chemical kinetics and cosmology, where it accurately reproduces global solutions and outperforms conventional matching procedures.

