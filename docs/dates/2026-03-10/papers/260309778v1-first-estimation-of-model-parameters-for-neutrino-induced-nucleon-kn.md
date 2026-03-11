---
layout: default
title: First Estimation of Model Parameters for Neutrino-Induced Nucleon Knockout Using Simulation-Based Inference
---

# First Estimation of Model Parameters for Neutrino-Induced Nucleon Knockout Using Simulation-Based Inference
**arXiv**：[2603.09778v1](https://arxiv.org/abs/2603.09778) · [PDF](https://arxiv.org/pdf/2603.09778.pdf)  
**作者**：Karla Tame-Narvaez, Steven Gardiner, Aleksandra Ćiprijanović, Giuseppe Cerati  

**一句话要点**：应用模拟推理首次估计中微子诱导核子敲出模型参数

**关键词**：模拟推理, 中微子相互作用, 参数估计, 机器学习, 核物理模拟

## 3 点简述
- 核心问题：加速器中微子实验需高精度核相互作用模拟，现有模拟缺陷常依赖经验调参。
- 方法要点：采用模拟推理技术，基于GENIE事件生成器调优配置，估计物理参数。
- 实验或效果：在MicroBooNE数据上，SBI算法获得略优拟合度，并能近似NuWro模拟。

## 摘要（原文）

> To enable an accurate determination of oscillation parameters, accelerator-based neutrino experiments require detailed simulations of nuclear interaction physics in the GeV regime. While substantial effort from both theory and experiment is currently being invested to improve the fidelity of these simulations, their present deficiencies typically oblige experimental collaborations to resort to empirical tuning of simulation model parameters. As the precision requirements of the field continue to become more stringent, machine learning techniques may provide a powerful means of handling corresponding growth in the complexity of future neutrino interaction model tuning exercises. To study the suitability of simulation-based inference (SBI) for this physics application, in this paper we revisit a tuned configuration of the GENIE neutrino event generator that was originally developed by the MicroBooNE collaboration. Despite closely reproducing the adopted values of four physics parameters when confronted with the tuned cross-section predictions as input, we find that our trained SBI algorithm prefers modestly different values (within MicroBooNE's assigned uncertainties) and achieves slightly better goodness-of-fit when inference is run on the experimental data set originally used by MicroBooNE. We also find that our trained algorithm can create a fair approximation of an alternative neutrino scattering simulation, NuWro, that shares only a subset of its physics model parameters with GENIE.

