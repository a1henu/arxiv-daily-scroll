---
layout: default
title: Neural Modular Physics for Elastic Simulation
---

# Neural Modular Physics for Elastic Simulation
**arXiv**：[2512.15083v1](https://arxiv.org/abs/2512.15083) · [PDF](https://arxiv.org/pdf/2512.15083.pdf)  
**作者**：Yifei Li, Haixu Wu, Zeyi Xu, Tuur Stuyck, Wojciech Matusik  

**一句话要点**：提出神经模块化物理方法，结合神经网络与传统模拟器优势，用于弹性模拟。

**关键词**：弹性模拟, 神经模块化物理, 物理可解释性, 泛化性, 长时程模拟

## 3 点简述
- 核心问题：传统端到端神经网络模拟器缺乏物理可解释性和可靠性。
- 方法要点：将弹性动力学分解为物理意义明确的神经模块，通过中间物理量连接。
- 实验效果：在未见初始条件、分辨率下泛化性优，物理性质保持更好，模拟稳定。

## 摘要（原文）

> Learning-based methods have made significant progress in physics simulation, typically approximating dynamics with a monolithic end-to-end optimized neural network. Although these models offer an effective way to simulation, they may lose essential features compared to traditional numerical simulators, such as physical interpretability and reliability. Drawing inspiration from classical simulators that operate in a modular fashion, this paper presents Neural Modular Physics (NMP) for elastic simulation, which combines the approximation capacity of neural networks with the physical reliability of traditional simulators. Beyond the previous monolithic learning paradigm, NMP enables direct supervision of intermediate quantities and physical constraints by decomposing elastic dynamics into physically meaningful neural modules connected through intermediate physical quantities. With a specialized architecture and training strategy, our method transforms the numerical computation flow into a modular neural simulator, achieving improved physical consistency and generalizability. Experimentally, NMP demonstrates superior generalization to unseen initial conditions and resolutions, stable long-horizon simulation, better preservation of physical properties compared to other neural simulators, and greater feasibility in scenarios with unknown underlying dynamics than traditional simulators.

