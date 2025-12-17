---
layout: default
title: gridfm-datakit-v1: A Python Library for Scalable and Realistic Power Flow and Optimal Power Flow Data Generation
---

# gridfm-datakit-v1: A Python Library for Scalable and Realistic Power Flow and Optimal Power Flow Data Generation
**arXiv**：[2512.14658v1](https://arxiv.org/abs/2512.14658) · [PDF](https://arxiv.org/pdf/2512.14658.pdf)  
**作者**：Alban Puech, Matteo Mazzonelli, Celia Cintas, Tamara R. Govindasamy, Mangaliso Mngomezulu, Jonas Weiss, Matteo Baù, Anna Varbella, François Mirallès, Kibaek Kim, Le Xie, Hendrik F. Hamann, Etienne Vos, Thomas Brunschwiler  

**一句话要点**：提出gridfm-datakit-v1库以生成多样且现实的电力潮流和最优潮流数据集，用于训练机器学习求解器。

**关键词**：电力潮流数据生成, 最优潮流数据生成, 机器学习求解器训练, 电网仿真, 开源Python库

## 3 点简述
- 现有数据集缺乏真实随机负载和拓扑扰动，限制场景多样性。
- 该库结合全局负载缩放与局部噪声，支持任意N-k拓扑扰动，生成超出运行限制的PF样本和可变成本的OPF数据。
- 可扩展至大型电网（如10,000节点），并与多个现有工具进行比较，代码开源。

## 摘要（原文）

> We introduce gridfm-datakit-v1, a Python library for generating realistic and diverse Power Flow (PF) and Optimal Power Flow (OPF) datasets for training Machine Learning (ML) solvers. Existing datasets and libraries face three main challenges: (1) lack of realistic stochastic load and topology perturbations, limiting scenario diversity; (2) PF datasets are restricted to OPF-feasible points, hindering generalization of ML solvers to cases that violate operating limits (e.g., branch overloads or voltage violations); and (3) OPF datasets use fixed generator cost functions, limiting generalization across varying costs. gridfm-datakit addresses these challenges by: (1) combining global load scaling from real-world profiles with localized noise and supporting arbitrary N-k topology perturbations to create diverse yet realistic datasets; (2) generating PF samples beyond operating limits; and (3) producing OPF data with varying generator costs. It also scales efficiently to large grids (up to 10,000 buses). Comparisons with OPFData, OPF-Learn, PGLearn, and PF$Δ$ are provided. Available on GitHub at https://github.com/gridfm/gridfm-datakit under Apache 2.0 and via `pip install gridfm-datakit`.

