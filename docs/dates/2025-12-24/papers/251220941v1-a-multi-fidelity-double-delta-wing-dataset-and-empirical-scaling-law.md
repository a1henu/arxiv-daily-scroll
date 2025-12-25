---
layout: default
title: A Multi-fidelity Double-Delta Wing Dataset and Empirical Scaling Laws for GNN-based Aerodynamic Field Surrogate
---

# A Multi-fidelity Double-Delta Wing Dataset and Empirical Scaling Laws for GNN-based Aerodynamic Field Surrogate
**arXiv**：[2512.20941v1](https://arxiv.org/abs/2512.20941) · [PDF](https://arxiv.org/pdf/2512.20941.pdf)  
**作者**：Yiren Shen, Juan J. Alonso  

**一句话要点**：发布双三角翼多保真度数据集并基于GNN代理模型建立数据规模与预测精度的幂律缩放关系

**关键词**：多保真度数据集, 图神经网络代理模型, 气动场预测, 缩放定律, 数据规模优化

## 3 点简述
- 核心问题：开源多保真度数据集和数据集规模与模型性能关系的经验指南有限
- 方法要点：使用VLM和RANS求解器生成2448个流场快照，基于嵌套Saltelli采样构建几何
- 实验或效果：测试误差随数据规模以幂律指数-0.6122下降，估计最优采样密度为每维度约8个样本

## 摘要（原文）

> Data-driven surrogate models are increasingly adopted to accelerate vehicle design. However, open-source multi-fidelity datasets and empirical guidelines linking dataset size to model performance remain limited. This study investigates the relationship between training data size and prediction accuracy for a graph neural network (GNN) based surrogate model for aerodynamic field prediction. We release an open-source, multi-fidelity aerodynamic dataset for double-delta wings, comprising 2448 flow snapshots across 272 geometries evaluated at angles of attack from 11 (degree) to 19 (degree) at Ma=0.3 using both Vortex Lattice Method (VLM) and Reynolds-Averaged Navier-Stokes (RANS) solvers. The geometries are generated using a nested Saltelli sampling scheme to support future dataset expansion and variance-based sensitivity analysis. Using this dataset, we conduct a preliminary empirical scaling study of the MF-VortexNet surrogate by constructing six training datasets with sizes ranging from 40 to 1280 snapshots and training models with 0.1 to 2.4 million parameters under a fixed training budget. We find that the test error decreases with data size with a power-law exponent of -0.6122, indicating efficient data utilization. Based on this scaling law, we estimate that the optimal sampling density is approximately eight samples per dimension in a d-dimensional design space. The results also suggest improved data utilization efficiency for larger surrogate models, implying a potential trade-off between dataset generation cost and model training budget.

