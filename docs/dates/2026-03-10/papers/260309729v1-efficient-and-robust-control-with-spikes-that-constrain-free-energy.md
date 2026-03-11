---
layout: default
title: Efficient and robust control with spikes that constrain free energy
---

# Efficient and robust control with spikes that constrain free energy
**arXiv**：[2603.09729v1](https://arxiv.org/abs/2603.09729) · [PDF](https://arxiv.org/pdf/2603.09729.pdf)  
**作者**：André Urbano, Pablo Lanillos, Sander Keemink  

**一句话要点**：提出基于尖峰约束自由能的高效鲁棒控制框架，用于动态系统控制与神经形态硬件实现。

**关键词**：尖峰控制, 自由能原理, 神经形态硬件, 鲁棒性, 稀疏活动, 动态系统

## 3 点简述
- 核心问题：动物大脑高效鲁棒感知与行动的机制未知，阻碍认知理解与控制算法发展。
- 方法要点：构建尖峰网络作为自由能约束器，神经元仅在降低内部表示自由能时放电，具有生物真实性。
- 实验或效果：网络活动稀疏高效，性能匹配类似框架，对外部和内部扰动具有高鲁棒性。

## 摘要（原文）

> Animal brains exhibit remarkable efficiency in perception and action, while being robust to both external and internal perturbations. The means by which brains accomplish this remains, for now, poorly understood, hindering our understanding of animal and human cognition, as well as our own implementation of efficient algorithms for control of dynamical systems.A potential candidate for a robust mechanism of state estimation and action computation is the free energy principle, but existing implementations of this principle have largely relied on conventional, biologically implausible approaches without spikes. We propose a novel, efficient, and robust spiking control framework with realistic biological characteristics. The resulting networks function as free energy constrainers, in which neurons only fire if they reduce the free energy of their internal representation. The networks offer efficient operation through highly sparse activity while matching performance with other similar spiking frameworks, and have high resilience against both external (e.g. sensory noise or collisions) and internal perturbations (e.g. synaptic noise and delays or neuron silencing) that such a network would be faced with when deployed by either an organism or an engineer. Overall, our work provides a novel mathematical account for spiking control through constraining free energy, providing both better insight into how brain networks might leverage their spiking substrate and a new route for implementing efficient control algorithms in neuromorphic hardware.

