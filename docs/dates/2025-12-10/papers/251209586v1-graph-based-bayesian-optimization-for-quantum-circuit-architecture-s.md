---
layout: default
title: Graph-Based Bayesian Optimization for Quantum Circuit Architecture Search with Uncertainty Calibrated Surrogates
---

# Graph-Based Bayesian Optimization for Quantum Circuit Architecture Search with Uncertainty Calibrated Surrogates
**arXiv**：[2512.09586v1](https://arxiv.org/abs/2512.09586) · [PDF](https://arxiv.org/pdf/2512.09586.pdf)  
**作者**：Prashant Kumar Choudhary, Nouhaila Innan, Muhammad Shafique, Rajeev Singh  

**一句话要点**：提出基于图贝叶斯优化的量子电路架构搜索框架，用于网络安全数据集上的量子机器学习。

**关键词**：量子电路架构搜索, 贝叶斯优化, 图神经网络, 不确定性校准, 网络安全数据集, 噪声鲁棒性

## 3 点简述
- 量子电路设计是量子机器学习在复杂现实数据上的关键瓶颈。
- 使用图神经网络代理和蒙特卡洛dropout不确定性校准，通过图表示和突变自动搜索变分量子电路。
- 在网络安全数据集上评估，相比基线找到复杂度更低且分类精度竞争或更优的电路，并评估噪声鲁棒性。

## 摘要（原文）

> Quantum circuit design is a key bottleneck for practical quantum machine learning on complex, real-world data. We present an automated framework that discovers and refines variational quantum circuits (VQCs) using graph-based Bayesian optimization with a graph neural network (GNN) surrogate. Circuits are represented as graphs and mutated and selected via an expected improvement acquisition function informed by surrogate uncertainty with Monte Carlo dropout. Candidate circuits are evaluated with a hybrid quantum-classical variational classifier on the next generation firewall telemetry and network internet of things (NF-ToN-IoT-V2) cybersecurity dataset, after feature selection and scaling for quantum embedding. We benchmark our pipeline against an MLP-based surrogate, random search, and greedy GNN selection. The GNN-guided optimizer consistently finds circuits with lower complexity and competitive or superior classification accuracy compared to all baselines. Robustness is assessed via a noise study across standard quantum noise channels, including amplitude damping, phase damping, thermal relaxation, depolarizing, and readout bit flip noise. The implementation is fully reproducible, with time benchmarking and export of best found circuits, providing a scalable and interpretable route to automated quantum circuit discovery.

