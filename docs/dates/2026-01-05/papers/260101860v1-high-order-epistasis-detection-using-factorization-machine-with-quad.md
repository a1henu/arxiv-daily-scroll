---
layout: default
title: High-Order Epistasis Detection Using Factorization Machine with Quadratic Optimization Annealing and MDR-Based Evaluation
---

# High-Order Epistasis Detection Using Factorization Machine with Quadratic Optimization Annealing and MDR-Based Evaluation
**arXiv**：[2601.01860v1](https://arxiv.org/abs/2601.01860) · [PDF](https://arxiv.org/pdf/2601.01860.pdf)  
**作者**：Shuta Kikuchi, Shu Tanaka  

**一句话要点**：提出基于因子分解机与二次优化退火的MDR评估方法，以高效检测高阶上位性

**关键词**：上位性检测, 因子分解机, 二次优化退火, 多因子降维, 遗传关联研究, 黑盒优化

## 3 点简述
- 核心问题：高阶上位性检测因候选位点组合爆炸而计算困难
- 方法要点：将上位性检测定义为黑盒优化问题，使用因子分解机结合二次优化退火求解
- 实验或效果：在模拟病例对照数据中，该方法能有效识别预设高阶上位性，计算效率高

## 摘要（原文）

> Detecting high-order epistasis is a fundamental challenge in genetic association studies due to the combinatorial explosion of candidate locus combinations. Although multifactor dimensionality reduction (MDR) is a widely used method for evaluating epistasis, exhaustive MDR-based searches become computationally infeasible as the number of loci or the interaction order increases. In this paper, we define the epistasis detection problem as a black-box optimization problem and solve it with a factorization machine with quadratic optimization annealing (FMQA). We propose an efficient epistasis detection method based on FMQA, in which the classification error rate (CER) computed by MDR is used as a black-box objective function. Experimental evaluations were conducted using simulated case-control datasets with predefined high-order epistasis. The results demonstrate that the proposed method successfully identified ground-truth epistasis across various interaction orders and the numbers of genetic loci within a limited number of iterations. These results indicate that the proposed method is effective and computationally efficient for high-order epistasis detection.

