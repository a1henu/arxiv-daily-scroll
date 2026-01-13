---
layout: default
title: Machine learning nonequilibrium phase transitions in charge-density wave insulators
---

# Machine learning nonequilibrium phase transitions in charge-density wave insulators
**arXiv**：[2601.07583v1](https://arxiv.org/abs/2601.07583) · [PDF](https://arxiv.org/pdf/2601.07583.pdf)  
**作者**：Yunhao Fan, Sheng Zhang, Gia-Wei Chern  

**一句话要点**：提出机器学习框架以高效模拟电荷密度波绝缘体中的非平衡相变动力学

**关键词**：非平衡相变, 机器学习力场, 电荷密度波, Holstein模型, 非平衡格林函数, 晶格动力学

## 3 点简述
- 核心问题：电压驱动相变中非平衡电子力计算成本高，阻碍长时间动力学模拟。
- 方法要点：利用电子响应的局域性，训练神经网络从晶格构型直接预测瞬时局部电子力。
- 实验或效果：结合布朗动力学，定量再现相变动态，计算效率提升数个数量级。

## 摘要（原文）

> Nonequilibrium electronic forces play a central role in voltage-driven phase transitions but are notoriously expensive to evaluate in dynamical simulations. Here we develop a machine learning framework for adiabatic lattice dynamics coupled to nonequilibrium electrons, and demonstrate it for a gating induced insulator to metal transition out of a charge density wave state in the Holstein model. Although exact electronic forces can be obtained from nonequilibrium Green's function (NEGF) calculations, their high computational cost renders long time dynamical simulations prohibitively expensive. By exploiting the locality of the electronic response, we train a neural network to directly predict instantaneous local electronic forces from the lattice configuration, thereby bypassing repeated NEGF calculations during time evolution. When combined with Brownian dynamics, the resulting machine learning force field quantitatively reproduces domain wall motion and nonequilibrium phase transition dynamics obtained from full NEGF simulations, while achieving orders of magnitude gains in computational efficiency. Our results establish direct force learning as an efficient and accurate approach for simulating nonequilibrium lattice dynamics in driven quantum materials.

