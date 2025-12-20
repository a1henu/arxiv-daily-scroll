---
layout: default
title: Can Transformers overcome the lack of data in the simulation of history-dependent flows?
---

# Can Transformers overcome the lack of data in the simulation of history-dependent flows?
**arXiv**：[2512.16305v1](https://arxiv.org/abs/2512.16305) · [PDF](https://arxiv.org/pdf/2512.16305.pdf)  
**作者**：P. Urdeitx, I. Alfaro, D. Gonzalez, F. Chinesta, E. Cueto  

**一句话要点**：评估Transformer在历史依赖流模拟中处理数据缺失的能力，优于结构保持网络

**关键词**：Transformer架构, 历史依赖流, 数据缺失, 流体模拟, 结构保持网络, 基准评估

## 3 点简述
- 研究Transformer能否应对历史依赖流中实验数据缺失的问题
- 方法在无历史依赖、Oldroyd-B和FENE模型三个基准问题上评估
- 结果显示Transformer在数据缺失时优于结构保持网络，但后者在数据完整时更优

## 摘要（原文）

> It is well known that the lack of information about certain variables necessary for the description of a dynamical system leads to the introduction of historical dependence (lack of Markovian character of the model) and noise. Traditionally, scientists have made up for these shortcomings by designing phenomenological variables that take into account this historical dependence (typically, conformational tensors in fluids). Often, these phenomenological variables are not easily measurable experimentally. In this work, we study to what extent Transformer architectures are able to cope with the lack of experimental data on these variables. The methodology is evaluated on three benchmark problems: a cylinder flow with no history dependence, a viscoelastic Couette flow modeled via the Oldroyd-B formalism, and a non-linear polymeric fluid described by the FENE model. Our results show that the Transformer outperforms a thermodynamically consistent, structure-preserving neural network with metriplectic bias in systems with missing experimental data, providing lower errors even in low-dimensional latent spaces. In contrast, for systems whose state variables can be fully known, the metriplectic model achieves superior performance.

