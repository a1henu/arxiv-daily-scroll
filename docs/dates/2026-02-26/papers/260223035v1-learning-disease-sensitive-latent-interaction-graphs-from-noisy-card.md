---
layout: default
title: Learning Disease-Sensitive Latent Interaction Graphs From Noisy Cardiac Flow Measurements
---

# Learning Disease-Sensitive Latent Interaction Graphs From Noisy Cardiac Flow Measurements
**arXiv**：[2602.23035v1](https://arxiv.org/abs/2602.23035) · [PDF](https://arxiv.org/pdf/2602.23035.pdf)  
**作者**：Viraj Patel, Marko Grujic, Philipp Aigner, Theodor Abart, Marcus Granegger, Deblina Bhattacharjee, Katharine Fraser  

**一句话要点**：提出基于物理的潜在关系框架，从噪声心脏血流测量中学习疾病敏感图以评估疾病严重性

**关键词**：心脏血流分析, 潜在图学习, 物理信息模型, 疾病评估, 跨模态泛化

## 3 点简述
- 核心问题：现有方法无法捕捉心脏血流中相干特征的关系结构，影响疾病评估。
- 方法要点：结合神经关系推断与物理启发的能量和动态，建模涡流为图节点，学习潜在图。
- 实验或效果：在主动脉缩窄模拟和左心室超声数据中，图熵与疾病严重性相关，实现跨模态泛化。

## 摘要（原文）

> Cardiac blood flow patterns contain rich information about disease severity and clinical interventions, yet current imaging and computational methods fail to capture underlying relational structures of coherent flow features. We propose a physics-informed, latent relational framework to model cardiac vortices as interacting nodes in a graph. Our model combines a neural relational inference architecture with physics-inspired interaction energy and birth-death dynamics, yielding a latent graph sensitive to disease severity and intervention level. We first apply this to computational fluid dynamics simulations of aortic coarctation. Learned latent graphs reveal that as the aortic radius narrows, vortex interactions become stronger and more frequent. This leads to a higher graph entropy, correlating monotonically with coarctation severity ($R^2=0.78$, Spearman $\|ρ\|=0.96$). We then extend this method to ultrasound datasets of left ventricles under varying levels of left ventricular assist device support. Again the latent graph representation captures the weakening of coherent vortical structures, thereby demonstrating cross-modal generalisation. Results show latent interaction graphs and entropy serve as robust and interpretable markers of cardiac disease and intervention.

