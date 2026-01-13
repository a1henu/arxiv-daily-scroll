---
layout: default
title: PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials
---

# PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials
**arXiv**：[2601.07742v1](https://arxiv.org/abs/2601.07742) · [PDF](https://arxiv.org/pdf/2601.07742.pdf)  
**作者**：Teddy Koker, Abhijeet Gangan, Mit Kotak, Jaime Marian, Tess Smidt  

**一句话要点**：提出声子微调方法以提升机器学习原子间势能的高阶导数预测精度

**关键词**：机器学习原子间势能, 声子性质, Hessian矩阵微调, 高阶导数预测, 材料热力学

## 3 点简述
- 机器学习原子间势能标准训练导致曲率误差，影响振动性质预测
- PFT通过匹配能量Hessian矩阵与DFT力常数，直接监督二阶力常数
- 在MDR Phonon基准上平均提升55%，并改善热导率等三阶导数性质

## 摘要（原文）

> Many materials properties depend on higher-order derivatives of the potential energy surface, yet machine learned interatomic potentials (MLIPs) trained with standard a standard loss on energy, force, and stress errors can exhibit error in curvature, degrading the prediction of vibrational properties. We introduce phonon fine-tuning (PFT), which directly supervises second-order force constants of materials by matching MLIP energy Hessians to DFT-computed force constants from finite displacement phonon calculations. To scale to large supercells, PFT stochastically samples Hessian columns and computes the loss with a single Hessian-vector product. We also use a simple co-training scheme to incorporate upstream data to mitigate catastrophic forgetting. On the MDR Phonon benchmark, PFT improves Nequix MP (trained on Materials Project) by 55% on average across phonon thermodynamic properties and achieves state-of-the-art performance among models trained on Materials Project trajectories. PFT also generalizes to improve properties beyond second-derivatives, improving thermal conductivity predictions that rely on third-order derivatives of the potential energy.

