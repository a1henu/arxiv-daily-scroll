---
layout: default
title: Magnetic Resonance Simulation of Effective Transverse Relaxation (T2*)
---

# Magnetic Resonance Simulation of Effective Transverse Relaxation (T2*)
**arXiv**：[2601.19246v1](https://arxiv.org/abs/2601.19246) · [PDF](https://arxiv.org/pdf/2601.19246.pdf)  
**作者**：Hidenori Takeshima  

**一句话要点**：提出基于线性相位模型的高效T2'模拟方法，以优化磁共振T2*仿真效率。

**关键词**：磁共振模拟, T2*弛豫, 线性相位模型, 计算加速, 洛伦兹函数

## 3 点简述
- 核心问题：传统T2'模拟需大量等色体，计算效率低。
- 方法要点：采用线性相位模型直接模拟洛伦兹函数，结合解析解和组合跃迁加速。
- 实验或效果：模拟时间仅增加2.0-2.7倍，加速技术提升达19倍。

## 摘要（原文）

> Purpose: To simulate effective transverse relaxation ($T_2^*$) as a part of MR simulation. $T_2^*$ consists of reversible ($T_2^{\prime}$) and irreversible ($T_2$) components. Whereas simulations of $T_2$ are easy, $T_2^{\prime}$ is not easily simulated if only magnetizations of individual isochromats are simulated.
>   Theory and Methods: Efficient methods for simulating $T_2^{\prime}$ were proposed. To approximate the Lorentzian function of $T_2^{\prime}$ realistically, conventional simulators require 100+ isochromats. This approximation can be avoided by utilizing a linear phase model for simulating an entire Lorentzian function directly. To represent the linear phase model, the partial derivatives of the magnetizations with respect to the frequency axis were also simulated. To accelerate the simulations with these partial derivatives, the proposed methods introduced two techniques: analytic solutions, and combined transitions. For understanding the fundamental mechanism of the proposed method, a simple one-isochromat simulation was performed. For evaluating realistic cases, several pulse sequences were simulated using two phantoms with and without $T_2^{\prime}$ simulations.
>   Results: The one-isochromat simulation demonstrated that $T_2^{\prime}$ simulations were possible. In the realistic cases, $T_2^{\prime}$ was recovered as expected without using 100+ isochromats for each point. The computational times with $T_2^{\prime}$ simulations were only 2.0 to 2.7 times longer than those without $T_2^{\prime}$ simulations. When the above-mentioned two techniques were utilized, the analytic solutions accelerated 19 times, and the combined transitions accelerated up to 17 times.
>   Conclusion: Both theory and results showed that the proposed methods simulated $T_2^{\prime}$ efficiently by utilizing a linear model with a Lorentzian function, analytic solutions, and combined transitions.

