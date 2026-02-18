---
layout: default
title: Controlled oscillation modeling using port-Hamiltonian neural networks
---

# Controlled oscillation modeling using port-Hamiltonian neural networks
**arXiv**：[2602.15704v1](https://arxiv.org/abs/2602.15704) · [PDF](https://arxiv.org/pdf/2602.15704.pdf)  
**作者**：Maximino Linares, Guillaume Doras, Thomas Hélie  

**一句话要点**：提出嵌入二阶离散梯度方法的端口哈密顿神经网络以改进受控振荡系统建模

**关键词**：端口哈密顿神经网络, 离散梯度方法, 受控振荡系统, 守恒定律学习, 数值方法比较

## 3 点简述
- 数据驱动方法难以学习守恒定律，导致泛化能力受限
- 在端口哈密顿神经网络中嵌入二阶离散梯度方法，替代龙格-库塔法
- 实验表明该方法在三种受控振荡系统中性能优于同阶龙格-库塔法

## 摘要（原文）

> Learning dynamical systems through purely data-driven methods is challenging as they do not learn the underlying conservation laws that enable them to correctly generalize. Existing port-Hamiltonian neural network methods have recently been successfully applied for modeling mechanical systems. However, even though these methods are designed on power-balance principles, they usually do not consider power-preserving discretizations and often rely on Runge-Kutta numerical methods. In this work, we propose to use a second-order discrete gradient method embedded in the learning of dynamical systems with port-Hamiltonian neural networks. Numerical results are provided for three systems deliberately selected to span different ranges of dynamical behavior under control: a baseline harmonic oscillator with quadratic energy storage; a Duffing oscillator, with a non-quadratic Hamiltonian offering amplitude-dependent effects; and a self-sustained oscillator, which can stabilize in a controlled limit cycle through the incorporation of a nonlinear dissipation. We show how the use of this discrete gradient method outperforms the performance of a Runge-Kutta method of the same order. Experiments are also carried out to compare two theoretically equivalent port-Hamiltonian systems formulations and to analyze the impact of regularizing the Jacobian of port-Hamiltonian neural networks during training.

