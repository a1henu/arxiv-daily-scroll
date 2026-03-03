---
layout: default
title: MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interaction Potentials
---

# MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interaction Potentials
**arXiv**：[2603.02002v1](https://arxiv.org/abs/2603.02002) · [PDF](https://arxiv.org/pdf/2603.02002.pdf)  
**作者**：Yuanchang Zhou, Siyu Hu, Xiangyu Zhang, Hongyu Wang, Guangming Tan, Weile Jia  

**一句话要点**：提出MatRIS以高效建模三体相互作用，实现低成本高精度材料机器学习势函数

**关键词**：机器学习势函数, 三体相互作用, 注意力机制, 材料科学, 计算效率

## 3 点简述
- 问题：等变MLIPs计算成本高，难以高效利用大规模量子力学数据集。
- 方法：引入基于注意力的三体相互作用建模，采用线性复杂度可分离注意力机制。
- 效果：在多个基准测试中达到与领先等变模型相当的精度，训练成本更低。

## 摘要（原文）

> Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

