---
layout: default
title: Advancing Opinion Dynamics Modeling with Neural Diffusion-Convection-Reaction Equation
---

# Advancing Opinion Dynamics Modeling with Neural Diffusion-Convection-Reaction Equation
**arXiv**：[2602.05403v1](https://arxiv.org/abs/2602.05403) · [PDF](https://arxiv.org/pdf/2602.05403.pdf)  
**作者**：Chenghua Gong, Yihang Jiang, Hao Li, Rui Sun, Juyuan Zhang, Tianjun Gu, Liming Pan, Linyuan Lü  

**一句话要点**：提出OPINN框架，基于扩散-对流-反应系统建模意见动力学，以提升预测性能与物理可解释性。

**关键词**：意见动力学建模, 物理信息神经网络, 扩散-对流-反应系统, 神经ODE, 社会系统分析, 预测性能

## 3 点简述
- 现有方法基于不完整先验，难以整合局部、全局和内生动态，且惩罚约束导致优化问题与表示不透明。
- 引入扩散-对流-反应系统解释意见动力学，结合神经ODE协调神经网络与物理先验，构建OPINN框架。
- 在真实与合成数据集上评估，OPINN在意见演化预测中达到先进性能，促进网络-物理-社会系统融合。

## 摘要（原文）

> Advanced opinion dynamics modeling is vital for deciphering social behavior, emphasizing its role in mitigating polarization and securing cyberspace. To synergize mechanistic interpretability with data-driven flexibility, recent studies have explored the integration of Physics-Informed Neural Networks (PINNs) for opinion modeling. Despite this promise, existing methods are tailored to incomplete priors, lacking a comprehensive physical system to integrate dynamics from local, global, and endogenous levels. Moreover, penalty-based constraints adopted in existing methods struggle to deeply encode physical priors, leading to optimization pathologies and discrepancy between latent representations and physical transparency. To this end, we offer a physical view to interpret opinion dynamics via Diffusion-Convection-Reaction (DCR) system inspired by interacting particle theory. Building upon the Neural ODEs, we define the neural opinion dynamics to coordinate neural networks with physical priors, and further present the OPINN, a physics-informed neural framework for opinion dynamics modeling. Evaluated on real-world and synthetic datasets, OPINN achieves state-of-the-art performance in opinion evolution forecasting, offering a promising paradigm for the nexus of cyber, physical, and social systems.

