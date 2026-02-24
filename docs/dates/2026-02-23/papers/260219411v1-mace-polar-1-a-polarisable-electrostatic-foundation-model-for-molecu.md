---
layout: default
title: MACE-POLAR-1: A Polarisable Electrostatic Foundation Model for Molecular Chemistry
---

# MACE-POLAR-1: A Polarisable Electrostatic Foundation Model for Molecular Chemistry
**arXiv**：[2602.19411v1](https://arxiv.org/abs/2602.19411) · [PDF](https://arxiv.org/pdf/2602.19411.pdf)  
**作者**：Ilyes Batatia, William J. Baldwin, Domantas Kuryla, Joseph Hart, Elliott Kasoar, Alin M. Elena, Harry Moore, Mikołaj J. Gawkowski, Benjamin X. Shi, Venkat Kapil, Panagiotis Kourtis, Ioan-Bogdan Magdău, Gábor Csányi  

**一句话要点**：提出MACE-POLAR-1极化静电基础模型，以解决分子化学中长程静电效应建模问题。

**关键词**：静电基础模型, 长程相互作用, 极化迭代, 电荷平衡, 分子化学, 机器学习原子间势能

## 3 点简述
- 核心问题：机器学习原子间势能模型依赖局部描述符，难以准确捕获长程静电相互作用和电荷转移。
- 方法要点：扩展MACE架构，结合局部几何特征与可学习电荷/自旋密度，通过极化迭代和全局电荷平衡处理静电感应。
- 实验或效果：在OMol25数据集上训练，实现化学精度，显著提升非共价相互作用和超分子复合物的描述准确性。

## 摘要（原文）

> Accurate modelling of electrostatic interactions and charge transfer is fundamental to computational chemistry, yet most machine learning interatomic potentials (MLIPs) rely on local atomic descriptors that cannot capture long-range electrostatic effects. We present a new electrostatic foundation model for molecular chemistry that extends the MACE architecture with explicit treatment of long-range interactions and electrostatic induction. Our approach combines local many-body geometric features with a non-self-consistent field formalism that updates learnable charge and spin densities through polarisable iterations to model induction, followed by global charge equilibration via learnable Fukui functions to control total charge and total spin. This design enables an accurate and physical description of systems with varying charge and spin states while maintaining computational efficiency. Trained on the OMol25 dataset of 100 million hybrid DFT calculations, our models achieve chemical accuracy across diverse benchmarks, with accuracy competitive with hybrid DFT on thermochemistry, reaction barriers, conformational energies, and transition metal complexes. Notably, we demonstrate that the inclusion of long-range electrostatics leads to a large improvement in the description of non-covalent interactions and supramolecular complexes over non-electrostatic models, including sub-kcal/mol prediction of molecular crystal formation energy in the X23-DMC dataset and a fourfold improvement over short-ranged models on protein-ligand interactions. The model's ability to handle variable charge and spin states, respond to external fields, provide interpretable spin-resolved charge densities, and maintain accuracy from small molecules to protein-ligand complexes positions it as a versatile tool for computational molecular chemistry and drug discovery.

