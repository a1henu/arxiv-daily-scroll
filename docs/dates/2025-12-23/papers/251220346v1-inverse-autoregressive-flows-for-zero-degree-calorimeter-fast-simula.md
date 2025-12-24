---
layout: default
title: Inverse Autoregressive Flows for Zero Degree Calorimeter fast simulation
---

# Inverse Autoregressive Flows for Zero Degree Calorimeter fast simulation
**arXiv**：[2512.20346v1](https://arxiv.org/abs/2512.20346) · [PDF](https://arxiv.org/pdf/2512.20346.pdf)  
**作者**：Emilia Majerz, Witold Dzwinel, Jacek Kitowski  

**一句话要点**：提出基于逆自回归流和物理知识嵌入的快速模拟方法，以加速ALICE实验零度量热器的粒子簇射仿真。

**关键词**：物理知识嵌入, 归一化流, 快速仿真, 粒子簇射模拟, 损失函数设计, 师生生成框架

## 3 点简述
- 核心问题：加速零度量热器仿真，需准确模拟粒子簇射的空间分布和形态，同时减少罕见伪影影响。
- 方法要点：结合物理知识嵌入，设计新损失函数和输出变异性缩放机制，在师生生成框架中应用归一化流。
- 实验或效果：模型比经典数据驱动方法更优，比现有归一化流实现快421倍，提升仿真效率和准确性。

## 摘要（原文）

> Physics-based machine learning blends traditional science with modern data-driven techniques. Rather than relying exclusively on empirical data or predefined equations, this methodology embeds domain knowledge directly into the learning process, resulting in models that are both more accurate and robust. We leverage this paradigm to accelerate simulations of the Zero Degree Calorimeter (ZDC) of the ALICE experiment at CERN. Our method introduces a novel loss function and an output variability-based scaling mechanism, which enhance the model's capability to accurately represent the spatial distribution and morphology of particle showers in detector outputs while mitigating the influence of rare artefacts on the training. Leveraging Normalizing Flows (NFs) in a teacher-student generative framework, we demonstrate that our approach not only outperforms classic data-driven model assimilation but also yields models that are 421 times faster than existing NF implementations in ZDC simulation literature.

