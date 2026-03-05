---
layout: default
title: Unsupervised Surrogate-Assisted Synthesis of Free-Form Planar Antenna Topologies for IoT Applications
---

# Unsupervised Surrogate-Assisted Synthesis of Free-Form Planar Antenna Topologies for IoT Applications
**arXiv**：[2603.03802v1](https://arxiv.org/abs/2603.03802) · [PDF](https://arxiv.org/pdf/2603.03802.pdf)  
**作者**：Khadijeh Askaripour, Adrian Bekasiewicz, Slawomir Koziel  

**一句话要点**：提出无监督代理辅助框架，用于物联网应用中的自由形式平面天线拓扑合成

**关键词**：无监督天线设计, 代理辅助优化, 自由形式拓扑, 物联网应用, 变保真度框架, 梯度优化

## 3 点简述
- 核心问题：物联网天线设计面临多重要求与约束，传统方法易受人为误差影响，自动设计存在几何确定与优化成本高挑战。
- 方法要点：采用变保真度框架，通过代理辅助分类器从候选设计中识别合适拓扑，再经梯度优化进行双阶段调谐。
- 实验或效果：基于六次数值实验，在5-6 GHz和6-7 GHz频段开发带宽增强贴片天线，并进行方法基准测试与拓扑分析。

## 摘要（原文）

> Design of antenna structures for Internet of Things (IoT) applications is a challenging problem. Contemporary radiators are often subject to a number of electric and/or radiation-related requirements, but also constraints imposed by specifics of IoT systems and/or intended operational environments. Conventional approaches to antenna design typically involve manual development of topology intertwined with its tuning. Although proved useful, the approach is prone to errors and engineering bias. Alternatively, geometries can be generated and optimized without supervision of the designer. The process can be controlled by suitable algorithms to determine and then adjust the antenna geometry according to the specifications. Unfortunately, automatic design of IoT radiators is associated with challenges such as determination of desirable geometries or high optimization cost. In this work, a variable-fidelity framework for performance-oriented development of free-form antennas represented using the generic simulation models is proposed. The method employs a surrogate-assisted classifier capable of identifying a suitable radiator topology from a set of automatically generated (and stored for potential re-use) candidate designs. The obtained geometry is then subject to a bi-stage tuning performed using a gradient-based optimization engine. The presented framework is demonstrated based on six numerical experiments concerning unsupervised development of bandwidth-enhanced patch antennas dedicated to work within 5 GHz to 6 GHz and 6 GHz to 7 GHz bands, respectively. Extensive benchmarks of the method, as well as the generated topologies are also performed.

