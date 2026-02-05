---
layout: default
title: Efficient Equivariant High-Order Crystal Tensor Prediction via Cartesian Local-Environment Many-Body Coupling
---

# Efficient Equivariant High-Order Crystal Tensor Prediction via Cartesian Local-Environment Many-Body Coupling
**arXiv**：[2602.04323v1](https://arxiv.org/abs/2602.04323) · [PDF](https://arxiv.org/pdf/2602.04323.pdf)  
**作者**：Dian Jin, Yancheng Yuan, Xiaoming Tao  

**一句话要点**：提出CEITNet以高效预测高阶晶体张量，通过笛卡尔局部环境多体耦合解决计算成本问题。

**关键词**：晶体张量预测, 等变模型, 笛卡尔张量, 多体耦合, 计算效率

## 3 点简述
- 问题：端到端预测高阶晶体张量时，球谐等变模型的张量积导致高计算和内存成本。
- 方法：构建多通道笛卡尔局部环境张量，通过可学习通道空间交互实现灵活多体混合。
- 效果：在二阶介电、三阶压电和四阶弹性张量预测基准上，CEITNet在准确性和计算效率上超越先前方法。

## 摘要（原文）

> End-to-end prediction of high-order crystal tensor properties from atomic structures remains challenging: while spherical-harmonic equivariant models are expressive, their Clebsch-Gordan tensor products incur substantial compute and memory costs for higher-order targets. We propose the Cartesian Environment Interaction Tensor Network (CEITNet), an approach that constructs a multi-channel Cartesian local environment tensor for each atom and performs flexible many-body mixing via a learnable channel-space interaction. By performing learning in channel space and using Cartesian tensor bases to assemble equivariant outputs, CEITNet enables efficient construction of high-order tensor. Across benchmark datasets for order-2 dielectric, order-3 piezoelectric, and order-4 elastic tensor prediction, CEITNet surpasses prior high-order prediction methods on key accuracy criteria while offering high computational efficiency.

