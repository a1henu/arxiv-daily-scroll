---
layout: default
title: Fast and accurate quasi-atom method for simultaneous atomistic and continuum simulation of solids
---

# Fast and accurate quasi-atom method for simultaneous atomistic and continuum simulation of solids
**arXiv**：[2602.14867v1](https://arxiv.org/abs/2602.14867) · [PDF](https://arxiv.org/pdf/2602.14867.pdf)  
**作者**：Artem Chuprov, Egor E. Nuzhin, Alexey A. Tsukanov, Nikolay V. Brilliantov  

**一句话要点**：提出准原子方法以高效准确模拟固体关键区域的原子与连续介质耦合

**关键词**：准原子方法, 原子-连续介质耦合, 机器学习优化, 分子动力学模拟, 固体模拟, 计算效率

## 3 点简述
- 核心问题：固体关键区域（如接触面、裂纹）需原子模拟，其他部分用连续介质模拟，但耦合方法计算成本高。
- 方法要点：使用不同尺寸准原子构建复合介质，通过机器学习优化势参数以匹配弹性性质，兼容标准分子动力学软件。
- 实验或效果：在Lennard-Jones和Tersoff势系统中验证，相比全原子模拟，计算速度显著提升，优于其他混合方法如AtC。

## 摘要（原文）

> We report a novel hybrid method of simultaneous atomistic simulation of solids in critical regions (contacts surfaces, cracks areas, etc.), along with continuum modeling of other parts. The continuum is treated in terms of quasi-atoms of different size, comprising composite medium. The parameters of interaction potential between the quasi-atoms are optimized to match elastic properties of the composite medium to those of the atomic one. The optimization method coincides conceptually with the online Machine Learning (ML) methods, making it computationally very efficient. Such an approach allows a straightforward application of standard software packages for molecular dynamics (MD), supplemented by the ML-based optimizer. The new method is applied to model systems with a simple, pairwise Lennard-Jones potential, as well with multi-body Tersoff potential, describing covalent bonds. Using LAMMPS software we simulate collision of particles of different size. Comparing simulation results, obtained by the novel method, with full-atomic simulations, we demonstrate its accuracy, validity and overwhelming superiority in computational speed. Furthermore, we compare our method with other hybrid methods, specifically, with the closest one -- AtC (Atomic to Continuum) method. We demonstrate a significant superiority of our approach in computational speed and implementation convenience. Finally, we discuss a possible extension of the method for modeling other phenomena.

