---
layout: default
title: A Critical Assessment of Pattern Comparisons Between POD and Autoencoders in Intraventricular Flows
---

# A Critical Assessment of Pattern Comparisons Between POD and Autoencoders in Intraventricular Flows
**arXiv**：[2512.19376v1](https://arxiv.org/abs/2512.19376) · [PDF](https://arxiv.org/pdf/2512.19376.pdf)  
**作者**：Eneko Lazpita, Andrés Bell-Navas, Jesús Garicano-Mena, Petros Koumoutsakos, Soledad Le Clainche  

**一句话要点**：比较POD与自编码器在左心室血流模式提取中的表现，揭示自编码器模式退化问题

**关键词**：血流动力学, 降阶建模, 自编码器, POD, 模式提取, 可解释性

## 3 点简述
- 核心问题：如何从复杂血流数据中提取紧凑且物理可解释的流结构模式，以支持心血管疾病早期检测
- 方法要点：系统比较POD与多种自编码器变体（线性、非线性、卷积、变分）在左心室血流场中的应用
- 实验或效果：自编码器在特定潜在维度下可产生类似POD的正交模式，但随模式数增加会失去正交性，导致可解释性下降

## 摘要（原文）

> Understanding intraventricular hemodynamics requires compact and physically interpretable representations of the underlying flow structures, as characteristic flow patterns are closely associated with cardiovascular conditions and can support early detection of cardiac deterioration. Conventional visualization of velocity or pressure fields, however, provides limited insight into the coherent mechanisms driving these dynamics. Reduced-order modeling techniques, like Proper Orthogonal Decomposition (POD) and Autoencoder (AE) architectures, offer powerful alternatives to extract dominant flow features from complex datasets. This study systematically compares POD with several AE variants (Linear, Nonlinear, Convolutional, and Variational) using left ventricular flow fields obtained from computational fluid dynamics simulations. We show that, for a suitably chosen latent dimension, AEs produce modes that become nearly orthogonal and qualitatively resemble POD modes that capture a given percentage of kinetic energy. As the number of latent modes increases, AE modes progressively lose orthogonality, leading to linear dependence, spatial redundancy, and the appearance of repeated modes with substantial high-frequency content. This degradation reduces interpretability and introduces noise-like components into AE-based reduced-order models, potentially complicating their integration with physics-based formulations or neural-network surrogates. The extent of interpretability loss varies across the AEs, with nonlinear, convolutional, and variational models exhibiting distinct behaviors in orthogonality preservation and feature localization. Overall, the results indicate that AEs can reproduce POD-like coherent structures under specific latent-space configurations, while highlighting the need for careful mode selection to ensure physically meaningful representations of cardiac flow dynamics.

