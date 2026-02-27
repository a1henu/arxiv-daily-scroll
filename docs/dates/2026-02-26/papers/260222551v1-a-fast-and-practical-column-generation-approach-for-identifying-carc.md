---
layout: default
title: A Fast and Practical Column Generation Approach for Identifying Carcinogenic Multi-Hit Gene Combinations
---

# A Fast and Practical Column Generation Approach for Identifying Carcinogenic Multi-Hit Gene Combinations
**arXiv**：[2602.22551v1](https://arxiv.org/abs/2602.22551) · [PDF](https://arxiv.org/pdf/2602.22551.pdf)  
**作者**：Rick S. H. Willemsen, Tenindra Abeywickrama, Ramu Anandakrishnan  

**一句话要点**：提出基于列生成的快速方法，以识别致癌多基因突变组合

**关键词**：癌症基因组学, 多基因突变组合, 列生成, 约束编程, 混合整数规划, 计算优化

## 3 点简述
- 核心问题：癌症常由2-9个基因突变组合驱动，需识别这些组合以理解致癌机制
- 方法要点：将问题形式化为MHCDSCP，采用约束编程和混合整数规划，并引入列生成启发式
- 实验或效果：在真实癌症基因组数据上，单CPU一分钟内达到先进方法性能，可求解小实例至最优

## 摘要（原文）

> Cancer is often driven by specific combinations of an estimated two to nine gene mutations, known as multi-hit combinations. Identifying these combinations is critical for understanding carcinogenesis and designing targeted therapies. We formalise this challenge as the Multi-Hit Cancer Driver Set Cover Problem (MHCDSCP), a binary classification problem that selects gene combinations to maximise coverage of tumor samples while minimising coverage of normal samples. Existing approaches typically rely on exhaustive search and supercomputing infrastructure. In this paper, we present constraint programming and mixed integer programming formulations of the MHCDSCP. Evaluated on real-world cancer genomics data, our methods achieve performance comparable to state-of-the-art methods while running on a single commodity CPU in under a minute. Furthermore, we introduce a column generation heuristic capable of solving small instances to optimality. These results suggest that solving the MHCDSCP is less computationally intensive than previously believed, thereby opening research directions for exploring modelling assumptions.

