---
layout: default
title: Efficient Parallel Algorithm for Decomposing Hard CircuitSAT Instances
---

# Efficient Parallel Algorithm for Decomposing Hard CircuitSAT Instances
**arXiv**：[2602.17130v1](https://arxiv.org/abs/2602.17130) · [PDF](https://arxiv.org/pdf/2602.17130.pdf)  
**作者**：Victor Kondratiev, Irina Gribanova, Alexander Semenov  

**一句话要点**：提出参数化并行算法以分解困难CircuitSAT实例，应用于逻辑等价检查和密码哈希函数攻击。

**关键词**：CircuitSAT分解, 并行算法, 逻辑等价检查, 密码哈希函数攻击, SAT实例分割

## 3 点简述
- 核心问题：分解困难CircuitSAT实例，如逻辑等价检查和密码哈希函数攻击中的SAT问题。
- 方法要点：使用专用约束将SAT实例分割为弱化公式族，基于并行计算的硬度估计指导参数调整。
- 实验或效果：在挑战性CircuitSAT实例上展示算法实用效能，具体性能指标未知。

## 摘要（原文）

> We propose a novel parallel algorithm for decomposing hard CircuitSAT instances. The technique employs specialized constraints to partition an original SAT instance into a family of weakened formulas. Our approach is implemented as a parameterized parallel algorithm, where adjusting the parameters allows efficient identification of high-quality decompositions, guided by hardness estimations computed in parallel. We demonstrate the algorithm's practical efficacy on challenging CircuitSAT instances, including those encoding Logical Equivalence Checking of Boolean circuits and preimage attacks on cryptographic hash functions.

