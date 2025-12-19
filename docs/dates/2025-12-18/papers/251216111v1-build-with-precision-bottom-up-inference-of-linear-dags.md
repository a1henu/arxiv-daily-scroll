---
layout: default
title: BUILD with Precision: Bottom-Up Inference of Linear DAGs
---

# BUILD with Precision: Bottom-Up Inference of Linear DAGs
**arXiv**：[2512.16111v1](https://arxiv.org/abs/2512.16111) · [PDF](https://arxiv.org/pdf/2512.16111.pdf)  
**作者**：Hamed Ajorlou, Samuel Rey, Gonzalo Mateos, Geert Leus, Antonio G. Marques  

**一句话要点**：提出BUILD算法以解决线性高斯SEM下DAG结构学习问题

**关键词**：有向无环图学习, 因果发现, 精度矩阵, 结构方程模型, 确定性算法

## 3 点简述
- 核心问题：从观测数据学习有向无环图结构，在因果发现和机器学习中至关重要
- 方法要点：利用精度矩阵的独特结构，通过逐步识别叶节点和父节点来精确重建DAG
- 实验或效果：在合成基准测试中表现优于现有算法，并通过重新估计精度矩阵增强鲁棒性

## 摘要（原文）

> Learning the structure of directed acyclic graphs (DAGs) from observational data is a central problem in causal discovery, statistical signal processing, and machine learning. Under a linear Gaussian structural equation model (SEM) with equal noise variances, the problem is identifiable and we show that the ensemble precision matrix of the observations exhibits a distinctive structure that facilitates DAG recovery. Exploiting this property, we propose BUILD (Bottom-Up Inference of Linear DAGs), a deterministic stepwise algorithm that identifies leaf nodes and their parents, then prunes the leaves by removing incident edges to proceed to the next step, exactly reconstructing the DAG from the true precision matrix. In practice, precision matrices must be estimated from finite data, and ill-conditioning may lead to error accumulation across BUILD steps. As a mitigation strategy, we periodically re-estimate the precision matrix (with less variables as leaves are pruned), trading off runtime for enhanced robustness. Reproducible results on challenging synthetic benchmarks demonstrate that BUILD compares favorably to state-of-the-art DAG learning algorithms, while offering an explicit handle on complexity.

