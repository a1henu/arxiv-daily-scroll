---
layout: default
title: Accelerating High-Throughput Catalyst Screening by Direct Generation of Equilibrium Adsorption Structures
---

# Accelerating High-Throughput Catalyst Screening by Direct Generation of Equilibrium Adsorption Structures
**arXiv**：[2512.15228v1](https://arxiv.org/abs/2512.15228) · [PDF](https://arxiv.org/pdf/2512.15228.pdf)  
**作者**：Songze Huo, Xiao-Ming Cao  

**一句话要点**：提出DBCata模型以加速催化剂高通量筛选，通过直接生成平衡吸附结构提升预测可靠性。

**关键词**：催化剂筛选, 吸附结构生成, 布朗桥模型, 等变图神经网络, 高通量计算, 机器学习势能

## 3 点简述
- 核心问题：传统机器学习势能模型因训练数据分布有限，导致吸附结构和能量预测不可靠。
- 方法要点：结合周期性布朗桥框架和等变图神经网络，建立未松弛与DFT松弛结构间的低维过渡流形。
- 实验或效果：在Catalysis-Hub数据集上，DMAE达0.035 Å，优于现有最佳模型近三倍；94%案例中DFT精度提升在0.1 eV内。

## 摘要（原文）

> The adsorption energy serves as a crucial descriptor for the large-scale screening of catalysts. Nevertheless, the limited distribution of training data for the extensively utilised machine learning interatomic potential (MLIP), predominantly sourced from near-equilibrium structures, results in unreliable adsorption structures and consequent adsorption energy predictions. In this context, we present DBCata, a deep generative model that integrates a periodic Brownian-bridge framework with an equivariant graph neural network to establish a low-dimensional transition manifold between unrelaxed and DFT-relaxed structures, without requiring explicit energy or force information. Upon training, DBCata effectively generates high-fidelity adsorption geometries, achieving an interatomic distance mean absolute error (DMAE) of 0.035 \textÅ on the Catalysis-Hub dataset, which is nearly three times superior to that of the current state-of-the-art machine learning potential models. Moreover, the corresponding DFT accuracy can be improved within 0.1 eV in 94\% of instances by identifying and refining anomalous predictions through a hybrid chemical-heuristic and self-supervised outlier detection approach. We demonstrate that the remarkable performance of DBCata facilitates accelerated high-throughput computational screening for efficient alloy catalysts in the oxygen reduction reaction, highlighting the potential of DBCata as a powerful tool for catalyst design and optimisation.

