---
layout: default
title: Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics -- Rotating Detonation Engines
---

# Cheap2Rich: A Multi-Fidelity Framework for Data Assimilation and System Identification of Multiscale Physics -- Rotating Detonation Engines
**arXiv**：[2601.20295v1](https://arxiv.org/abs/2601.20295) · [PDF](https://arxiv.org/pdf/2601.20295.pdf)  
**作者**：Yuxuan Bao, Jan Zajac, Megan Powers, Venkat Raman, J. Nathan Kutz  

**一句话要点**：提出Cheap2Rich多保真度框架，用于旋转爆震发动机的数据同化和系统识别。

**关键词**：多保真度框架, 数据同化, 系统识别, 旋转爆震发动机, 多尺度物理, 可解释机器学习

## 3 点简述
- 核心问题：解决计算廉价模型与复杂多尺度物理系统之间的sim2real差距。
- 方法要点：结合快速低保真度先验与可解释的差异校正，从稀疏传感器数据重建高保真状态空间。
- 实验或效果：在旋转爆震发动机上成功重建高保真状态，并分离与注入器驱动效应相关的物理差异动态。

## 摘要（原文）

> Bridging the sim2real gap between computationally inexpensive models and complex physical systems remains a central challenge in machine learning applications to engineering problems, particularly in multi-scale settings where reduced-order models typically capture only dominant dynamics. In this work, we present Cheap2Rich, a multi-scale data assimilation framework that reconstructs high-fidelity state spaces from sparse sensor histories by combining a fast low-fidelity prior with learned, interpretable discrepancy corrections. We demonstrate the performance on rotating detonation engines (RDEs), a challenging class of systems that couple detonation-front propagation with injector-driven unsteadiness, mixing, and stiff chemistry across disparate scales. Our approach successfully reconstructs high-fidelity RDE states from sparse measurements while isolating physically meaningful discrepancy dynamics associated with injector-driven effects. The results highlight a general multi-fidelity framework for data assimilation and system identification in complex multi-scale systems, enabling rapid design exploration and real-time monitoring and control while providing interpretable discrepancy dynamics. Code for this project is is available at: github.com/kro0l1k/Cheap2Rich.

