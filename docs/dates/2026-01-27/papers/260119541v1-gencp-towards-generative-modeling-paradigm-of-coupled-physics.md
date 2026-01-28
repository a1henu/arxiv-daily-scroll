---
layout: default
title: GenCP: Towards Generative Modeling Paradigm of Coupled Physics
---

# GenCP: Towards Generative Modeling Paradigm of Coupled Physics
**arXiv**：[2601.19541v1](https://arxiv.org/abs/2601.19541) · [PDF](https://arxiv.org/pdf/2601.19541.pdf)  
**作者**：Tianrun Gao, Haoren Zheng, Wenhao Deng, Haodong Feng, Tao Zhang, Ruiqi Feng, Qianyi Chen, Tailin Wu  

**一句话要点**：提出GenCP生成建模范式，以解决耦合多物理系统模拟中的解耦数据训练和效率保真度问题。

**关键词**：多物理耦合模拟, 生成建模, 概率密度演化, 解耦数据训练, 误差可控性, 时空物理系统

## 3 点简述
- 核心问题：现实物理系统多物理耦合复杂，现有方法处理解耦数据困难，强耦合时空系统效率与保真度低。
- 方法要点：将耦合物理建模转化为概率建模，结合概率密度演化与迭代多物理耦合，实现解耦数据训练和采样时耦合推断。
- 实验或效果：在合成设置和三个挑战性多物理场景中评估，展示原理洞察和优越应用性能，代码已开源。

## 摘要（原文）

> Real-world physical systems are inherently complex, often involving the coupling of multiple physics, making their simulation both highly valuable and challenging. Many mainstream approaches face challenges when dealing with decoupled data. Besides, they also suffer from low efficiency and fidelity in strongly coupled spatio-temporal physical systems. Here we propose GenCP, a novel and elegant generative paradigm for coupled multiphysics simulation. By formulating coupled-physics modeling as a probability modeling problem, our key innovation is to integrate probability density evolution in generative modeling with iterative multiphysics coupling, thereby enabling training on data from decoupled simulation and inferring coupled physics during sampling. We also utilize operator-splitting theory in the space of probability evolution to establish error controllability guarantees for this "conditional-to-joint" sampling scheme. We evaluate our paradigm on a synthetic setting and three challenging multi-physics scenarios to demonstrate both principled insight and superior application performance of GenCP. Code is available at this repo: github.com/AI4Science-WestlakeU/GenCP.

