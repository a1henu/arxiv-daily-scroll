---
layout: default
title: Posterior Distribution-assisted Evolutionary Dynamic Optimization as an Online Calibrator for Complex Social Simulations
---

# Posterior Distribution-assisted Evolutionary Dynamic Optimization as an Online Calibrator for Complex Social Simulations
**arXiv**：[2601.19481v1](https://arxiv.org/abs/2601.19481) · [PDF](https://arxiv.org/pdf/2601.19481.pdf)  
**作者**：Peng Yang, Zhenhua Yang, Boquan Jiang, Chenkai Wang, Ke Tang, Xin Yao  

**一句话要点**：提出基于后验分布的进化动态优化方法，用于在线校准复杂社会模拟器

**关键词**：在线校准, 进化动态优化, 后验分布, 社会模拟, 动态优化问题, 参数估计

## 3 点简述
- 在线校准复杂社会模拟器被建模为动态优化问题，需适应系统内部变化
- 方法显式学习参数和观测数据的后验分布，促进变化检测和环境适应
- 在经济学和金融模拟器上验证，后验分布能有效提升进化动态优化性能

## 摘要（原文）

> The calibration of simulators for complex social systems aims to identify the optimal parameter that drives the output of the simulator best matching the target data observed from the system. As many social systems may change internally over time, calibration naturally becomes an online task, requiring parameters to be updated continuously to maintain the simulator's fidelity. In this work, the online setting is first formulated as a dynamic optimization problem (DOP), requiring the search for a sequence of optimal parameters that fit the simulator to real system changes. However, in contrast to traditional DOP formulations, online calibration explicitly incorporates the observational data as the driver of environmental dynamics. Due to this fundamental difference, existing Evolutionary Dynamic Optimization (EDO) methods, despite being extensively studied for black-box DOPs, are ill-equipped to handle such a scenario. As a result, online calibration problems constitute a new set of challenging DOPs. Here, we propose to explicitly learn the posterior distributions of the parameters and the observational data, thereby facilitating both change detection and environmental adaptation of existing EDOs for this scenario. We thus present a pretrained posterior model for implementation, and fine-tune it during the optimization. Extensive tests on both economic and financial simulators verify that the posterior distribution strongly promotes EDOs in such DOPs widely existed in social science.

