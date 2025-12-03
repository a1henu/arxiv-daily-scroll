---
layout: default
title: Generative modeling using evolved quantum Boltzmann machines
---

# Generative modeling using evolved quantum Boltzmann machines
**arXiv**：[2512.02721v1](https://arxiv.org/abs/2512.02721) · [PDF](https://arxiv.org/pdf/2512.02721.pdf)  
**作者**：Mark M. Wilde  

**一句话要点**：提出基于Donsker-Varadhan变分表示和量子Boltzmann梯度估计器的训练方法，以解决量子Boltzmann机器在Born-rule生成建模中训练效率低的问题。

**关键词**：量子Boltzmann机器, Born-rule生成建模, Donsker-Varadhan变分表示, 量子梯度估计, 混合量子-经典算法, 极小极大优化

## 3 点简述
- 核心问题：量子Boltzmann机器在Born-rule生成建模中训练方法低效，阻碍其实际应用。
- 方法要点：结合Donsker-Varadhan变分表示和量子Boltzmann梯度估计器，提出适用于演化量子Boltzmann机器的训练方案。
- 实验或效果：提出四种混合量子-经典算法用于极小极大优化，并讨论其理论收敛保证。

## 摘要（原文）

> Born-rule generative modeling, a central task in quantum machine learning, seeks to learn probability distributions that can be efficiently sampled by measuring complex quantum states. One hope is for quantum models to efficiently capture probability distributions that are difficult to learn and simulate by classical means alone. Quantum Boltzmann machines were proposed about one decade ago for this purpose, yet efficient training methods have remained elusive. In this paper, I overcome this obstacle by proposing a practical solution that trains quantum Boltzmann machines for Born-rule generative modeling. Two key ingredients in the proposal are the Donsker-Varadhan variational representation of the classical relative entropy and the quantum Boltzmann gradient estimator of [Patel et al., arXiv:2410.12935]. I present the main result for a more general ansatz known as an evolved quantum Boltzmann machine [Minervini et al., arXiv:2501.03367], which combines parameterized real- and imaginary-time evolution. I also show how to extend the findings to other distinguishability measures beyond relative entropy. Finally, I present four different hybrid quantum-classical algorithms for the minimax optimization underlying training, and I discuss their theoretical convergence guarantees.

