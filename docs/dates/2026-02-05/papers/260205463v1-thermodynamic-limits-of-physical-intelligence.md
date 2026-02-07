---
layout: default
title: Thermodynamic Limits of Physical Intelligence
---

# Thermodynamic Limits of Physical Intelligence
**arXiv**：[2602.05463v1](https://arxiv.org/abs/2602.05463) · [PDF](https://arxiv.org/pdf/2602.05463.pdf)  
**作者**：Koichi Takahashi, Yusuke Hayashi  

**一句话要点**：提出基于热力学的比特每焦耳度量以评估物理智能效率，连接智能与能耗。

**关键词**：物理智能, 热力学效率, 比特每焦耳, 熵复杂度, 赋权, 能耗评估

## 3 点简述
- 核心问题：现代AI系统能耗高，需量化智能与物理效率的关系。
- 方法要点：定义热力学熵复杂度每焦耳和赋权每焦耳两个互补度量，分别对应识别与控制。
- 实验或效果：基于随机热力学推导闭循环基准，提出统一效率框架以减少歧义。

## 摘要（原文）

> Modern AI systems achieve remarkable capabilities at the cost of substantial energy consumption. To connect intelligence to physical efficiency, we propose two complementary bits-per-joule metrics under explicit accounting conventions: (1) Thermodynamic Epiplexity per Joule -- bits of structural information about a theoretical environment-instance variable newly encoded in an agent's internal state per unit measured energy within a stated boundary -- and (2) Empowerment per Joule -- the embodied sensorimotor channel capacity (control information) per expected energetic cost over a fixed horizon. These provide two axes of physical intelligence: recognition (model-building) vs.control (action influence). Drawing on stochastic thermodynamics, we show how a Landauer-scale closed-cycle benchmark for epiplexity acquisition follows as a corollary of a standard thermodynamic-learning inequality under explicit subsystem assumptions, and we clarify how Landauer-scaled costs act as closed-cycle benchmarks under explicit reset/reuse and boundary-closure assumptions; conversely, we give a simple decoupling construction showing that without such assumptions -- and without charging for externally prepared low-entropy resources (e.g.fresh memory) crossing the boundary -- information gain and in-boundary dissipation need not be tightly linked. For empirical settings where the latent structure variable is unavailable, we align the operational notion of epiplexity with compute-bounded MDL epiplexity and recommend reporting MDL-epiplexity / compression-gain surrogates as companions. Finally, we propose a unified efficiency framework that reports both metrics together with a minimal checklist of boundary/energy accounting, coarse-graining/noise, horizon/reset, and cost conventions to reduce ambiguity and support consistent bits-per-joule comparisons, and we sketch connections to energy-adjusted scaling analyses.

