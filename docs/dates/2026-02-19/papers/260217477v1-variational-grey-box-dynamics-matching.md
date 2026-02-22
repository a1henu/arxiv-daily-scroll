---
layout: default
title: Variational Grey-Box Dynamics Matching
---

# Variational Grey-Box Dynamics Matching
**arXiv**：[2602.17477v1](https://arxiv.org/abs/2602.17477) · [PDF](https://arxiv.org/pdf/2602.17477.pdf)  
**作者**：Gurjeet Sangra Singh, Frantzeska Lavda, Giangiacomo Mercatali, Alexandros Kalousis  

**一句话要点**：提出变分灰盒动力学匹配方法，以整合不完全物理模型到生成模型中，解决黑盒生成模型忽视物理与物理模型不完整的问题。

**关键词**：灰盒建模, 流匹配, 变分推断, 物理信息先验, 二阶动力学, 生成模型

## 3 点简述
- 核心问题：黑盒生成模型忽视物理，物理模型不完整，无法完全描述观测数据。
- 方法要点：在流匹配框架内建模结构化变分分布，使用两个潜在编码分别建模缺失随机性和物理参数。
- 实验或效果：在ODE/PDE问题上性能优于或持平数据驱动方法，保持物理模型可解释性。

## 摘要（原文）

> Deep generative models such as flow matching and diffusion models have shown great potential in learning complex distributions and dynamical systems, but often act as black-boxes, neglecting underlying physics. In contrast, physics-based simulation models described by ODEs/PDEs remain interpretable, but may have missing or unknown terms, unable to fully describe real-world observations. We bridge this gap with a novel grey-box method that integrates incomplete physics models directly into generative models. Our approach learns dynamics from observational trajectories alone, without ground-truth physics parameters, in a simulation-free manner that avoids scalability and stability issues of Neural ODEs. The core of our method lies in modelling a structured variational distribution within the flow matching framework, by using two latent encodings: one to model the missing stochasticity and multi-modal velocity, and a second to encode physics parameters as a latent variable with a physics-informed prior. Furthermore, we present an adaptation of the framework to handle second-order dynamics. Our experiments on representative ODE/PDE problems show that our method performs on par with or superior to fully data-driven approaches and previous grey-box baselines, while preserving the interpretability of the physics model. Our code is available at https://github.com/DMML-Geneva/VGB-DM.

