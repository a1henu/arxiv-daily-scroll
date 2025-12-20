---
layout: default
title: Physics-Informed Neural Networks for Modeling the Martian Induced Magnetosphere
---

# Physics-Informed Neural Networks for Modeling the Martian Induced Magnetosphere
**arXiv**：[2512.16175v1](https://arxiv.org/abs/2512.16175) · [PDF](https://arxiv.org/pdf/2512.16175.pdf)  
**作者**：Jiawei Gao, Chuanfei Dong, Chi Zhang, Yilan Qin, Simin Shekarpaz, Xinmin Li, Liang Wang, Hongyang Zhou, Abigail Tadlock  

**一句话要点**：提出物理信息神经网络以建模火星感应磁层，结合MAVEN观测与物理定律重建三维磁场。

**关键词**：物理信息神经网络, 火星感应磁层, MAVEN观测, 数据驱动建模, 太阳风-火星相互作用

## 3 点简述
- 核心问题：传统火星感应磁层模型依赖计算密集型物理模拟，难以高效处理多变太阳风条件。
- 方法要点：首次使用物理信息神经网络，整合MAVEN观测数据和物理定律，构建数据驱动模型。
- 实验或效果：模型在多种太阳风条件下准确重建三维磁场配置，揭示磁场对太阳风参数的依赖关系。

## 摘要（原文）

> Understanding the magnetic field environment around Mars and its response to upstream solar wind conditions provide key insights into the processes driving atmospheric ion escape. To date, global models of Martian induced magnetosphere have been exclusively physics-based, relying on computationally intensive simulations. For the first time, we develop a data-driven model of the Martian induced magnetospheric magnetic field using Physics-Informed Neural Network (PINN) combined with MAVEN observations and physical laws. Trained under varying solar wind conditions, including B_IMF, P_SW, and θ_cone, the data-driven model accurately reconstructs the three-dimensional magnetic field configuration and its variability in response to upstream solar wind drivers. Based on the PINN results, we identify key dependencies of magnetic field configuration on solar wind parameters, including the hemispheric asymmetries of the draped field line strength in the Mars-Solar-Electric coordinates. These findings demonstrate the capability of PINNs to reconstruct complex magnetic field structures in the Martian induced magnetosphere, thereby offering a promising tool for advancing studies of solar wind-Mars interactions.

