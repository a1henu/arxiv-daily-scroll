---
layout: default
title: QTabGAN: A Hybrid Quantum-Classical GAN for Tabular Data Synthesis
---

# QTabGAN: A Hybrid Quantum-Classical GAN for Tabular Data Synthesis
**arXiv**：[2602.12704v1](https://arxiv.org/abs/2602.12704) · [PDF](https://arxiv.org/pdf/2602.12704.pdf)  
**作者**：Subhangi Kumari, Rakesh Achutha, Vignesh Sivaraman  

**一句话要点**：提出QTabGAN，一种混合量子-经典GAN，用于稀缺或隐私受限场景下的表格数据合成。

**关键词**：表格数据合成, 混合量子-经典GAN, 量子电路, 隐私保护, 生成对抗网络

## 3 点简述
- 核心问题：表格数据合成因特征异构和高维性而具挑战性。
- 方法要点：利用量子电路学习复杂分布，通过经典神经网络映射到表格特征。
- 实验或效果：在分类数据集上实现高达54.07%的性能提升，优于现有生成模型。

## 摘要（原文）

> Synthesizing realistic tabular data is challenging due to heterogeneous feature types and high dimensionality. We introduce QTabGAN, a hybrid quantum-classical generative adversarial framework for tabular data synthesis. QTabGAN is especially designed for settings where real data are scarce or restricted by privacy constraints. The model exploits the expressive power of quantum circuits to learn complex data distributions, which are then mapped to tabular features using classical neural networks. We evaluate QTabGAN on multiple classification and regression datasets and benchmark it against leading state-of-the-art generative models. Experiments show that QTabGAN achieves up to 54.07% improvement across various classification datasets and evaluation metrics, thus establishing a scalable quantum approach to tabular data synthesis and highlighting its potential for quantum-assisted generative modelling.

