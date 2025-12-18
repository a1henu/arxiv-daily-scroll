---
layout: default
title: Learning Model Parameter Dynamics in a Combination Therapy for Bladder Cancer from Sparse Biological Data
---

# Learning Model Parameter Dynamics in a Combination Therapy for Bladder Cancer from Sparse Biological Data
**arXiv**：[2512.15706v1](https://arxiv.org/abs/2512.15706) · [PDF](https://arxiv.org/pdf/2512.15706.pdf)  
**作者**：Kayode Olumoyin, Lamees El Naqa, Katarzyna Rejniak  

**一句话要点**：提出基于物理信息神经网络的方法，从稀疏数据中学习膀胱癌联合疗法中细胞间时变相互作用。

**关键词**：物理信息神经网络, 稀疏数据建模, 时变相互作用, 膀胱癌治疗, 细胞动力学, 组合疗法

## 3 点简述
- 核心问题：传统固定参数模型难以捕捉生物系统在外部干预下的动态演化，且肿瘤体积数据稀疏。
- 方法要点：采用物理信息神经网络预测未观测时间点的细胞亚群轨迹，学习时变相互作用。
- 实验或效果：方法在稀疏数据场景下与生物学解释一致，提供学习演化相互作用的框架。

## 摘要（原文）

> In a mathematical model of interacting biological organisms, where external interventions may alter behavior over time, traditional models that assume fixed parameters usually do not capture the evolving dynamics. In oncology, this is further exacerbated by the fact that experimental data are often sparse and sometimes are composed of a few time points of tumor volume. In this paper, we propose to learn time-varying interactions between cells, such as those of bladder cancer tumors and immune cells, and their response to a combination of anticancer treatments in a limited data scenario. We employ the physics-informed neural network (PINN) approach to predict possible subpopulation trajectories at time points where no observed data are available. We demonstrate that our approach is consistent with the biological explanation of subpopulation trajectories. Our method provides a framework for learning evolving interactions among biological organisms when external interventions are applied to their environment.

