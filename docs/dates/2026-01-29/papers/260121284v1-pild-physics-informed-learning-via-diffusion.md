---
layout: default
title: PILD: Physics-Informed Learning via Diffusion
---

# PILD: Physics-Informed Learning via Diffusion
**arXiv**：[2601.21284v1](https://arxiv.org/abs/2601.21284) · [PDF](https://arxiv.org/pdf/2601.21284.pdf)  
**作者**：Tianyi Zeng, Tianyi Wang, Jiaru Zhang, Zimo Zeng, Feiyang Zhang, Yiming Xu, Sikai Chen, Yajie Zou, Yangyang Wang, Junfeng Jiao, Christian Claudel, Xinbo Chen  

**一句话要点**：提出PILD框架，通过扩散模型结合物理约束解决工程与科学问题中的生成任务。

**关键词**：扩散模型, 物理约束学习, 条件嵌入, 虚拟残差观测, 工程科学应用

## 3 点简述
- 核心问题：扩散模型纯数据驱动，难以满足物理定律约束，限制在工程科学中的应用。
- 方法要点：引入拉普拉斯分布虚拟残差观测监督训练，并设计条件嵌入模块在多层注入物理信息。
- 实验或效果：在车辆轨迹、达西流等任务中，PILD显著提升准确性、稳定性和泛化能力。

## 摘要（原文）

> Diffusion models have emerged as powerful generative tools for modeling complex data distributions, yet their purely data-driven nature limits applicability in practical engineering and scientific problems where physical laws need to be followed. This paper proposes Physics-Informed Learning via Diffusion (PILD), a framework that unifies diffusion modeling and first-principles physical constraints by introducing a virtual residual observation sampled from a Laplace distribution to supervise generation during training. To further integrate physical laws, a conditional embedding module is incorporated to inject physical information into the denoising network at multiple layers, ensuring consistent guidance throughout the diffusion process. The proposed PILD framework is concise, modular, and broadly applicable to problems governed by ordinary differential equations, partial differential equations, as well as algebraic equations or inequality constraints. Extensive experiments across engineering and scientific tasks including estimating vehicle trajectories, tire forces, Darcy flow and plasma dynamics, demonstrate that our PILD substantially improves accuracy, stability, and generalization over existing physics-informed and diffusion-based baselines.

