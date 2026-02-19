---
layout: default
title: DistributedEstimator: Distributed Training of Quantum Neural Networks via Circuit Cutting
---

# DistributedEstimator: Distributed Training of Quantum Neural Networks via Circuit Cutting
**arXiv**：[2602.16233v1](https://arxiv.org/abs/2602.16233) · [PDF](https://arxiv.org/pdf/2602.16233.pdf)  
**作者**：Prabhjot Singh, Adel N. Toosi, Rajkumar Buyya  

**一句话要点**：提出分布式训练框架，通过电路切割实现量子神经网络的高效分布式训练。

**关键词**：量子神经网络, 电路切割, 分布式训练, 系统开销, 经典重建, 训练效率

## 3 点简述
- 核心问题：电路切割在迭代训练中的端到端系统开销未被充分量化。
- 方法要点：设计分阶段分布式工作流，包括分区、子实验生成、并行执行和经典重建。
- 实验或效果：在Iris和MNIST任务上测量开销、扩展限制和准确性，重建阶段是主要瓶颈。

## 摘要（原文）

> Circuit cutting decomposes a large quantum circuit into a collection of smaller subcircuits. The outputs of these subcircuits are then classically reconstructed to recover the original expectation values. While prior work characterises cutting overhead largely in terms of subcircuit counts and sampling complexity, its end-to-end impact on iterative, estimator-driven training pipelines remains insufficiently measured from a systems perspective. In this paper, we propose a cut-aware estimator execution pipeline that treats circuit cutting as a staged distributed workload and instruments each estimator query into partitioning, subexperiment generation, parallel execution, and classical reconstruction phases. Using logged runtime traces and learning outcomes on two binary classification workloads (Iris and MNIST), we quantify cutting overheads, scaling limits, and sensitivity to injected stragglers, and we evaluate whether accuracy and robustness are preserved under matched training budgets. Our measurements show that cutting introduces substantial end-to-end overheads that grow with the number of cuts, and that reconstruction constitutes a dominant fraction of per-query time, bounding achievable speed-up under increased parallelism. Despite these systems costs, test accuracy and robustness are preserved in the measured regimes, with configuration-dependent improvements observed in some cut settings. These results indicate that practical scaling of circuit cutting for learning workloads hinges on reducing and overlapping reconstruction and on scheduling policies that account for barrier-dominated critical paths.

