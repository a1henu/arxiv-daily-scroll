---
layout: default
title: QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer
---

# QNeRF: Neural Radiance Fields on a Simulated Gate-Based Quantum Computer
**arXiv**：[2601.05250v1](https://arxiv.org/abs/2601.05250) · [PDF](https://arxiv.org/pdf/2601.05250.pdf)  
**作者**：Daniele Lizzio Bosco, Shuteng Wang, Giuseppe Serra, Vladislav Golyanik  

**一句话要点**：提出QNeRF，首个用于2D图像新视角合成的混合量子-经典模型。

**关键词**：量子机器学习, 神经辐射场, 新视角合成, 混合量子-经典模型, 参数化量子电路

## 3 点简述
- 核心问题：NeRF模型大、训练密集，量子视觉场在紧凑性和收敛速度上具潜力。
- 方法要点：利用参数化量子电路编码空间和视角信息，通过量子叠加和纠缠实现模型紧凑。
- 实验或效果：在中等分辨率图像上，QNeRF参数减半，性能匹配或超越经典NeRF基线。

## 摘要（原文）

> Recently, Quantum Visual Fields (QVFs) have shown promising improvements in model compactness and convergence speed for learning the provided 2D or 3D signals. Meanwhile, novel-view synthesis has seen major advances with Neural Radiance Fields (NeRFs), where models learn a compact representation from 2D images to render 3D scenes, albeit at the cost of larger models and intensive training. In this work, we extend the approach of QVFs by introducing QNeRF, the first hybrid quantum-classical model designed for novel-view synthesis from 2D images. QNeRF leverages parameterised quantum circuits to encode spatial and view-dependent information via quantum superposition and entanglement, resulting in more compact models compared to the classical counterpart. We present two architectural variants. Full QNeRF maximally exploits all quantum amplitudes to enhance representational capabilities. In contrast, Dual-Branch QNeRF introduces a task-informed inductive bias by branching spatial and view-dependent quantum state preparations, drastically reducing the complexity of this operation and ensuring scalability and potential hardware compatibility. Our experiments demonstrate that -- when trained on images of moderate resolution -- QNeRF matches or outperforms classical NeRF baselines while using less than half the number of parameters. These results suggest that quantum machine learning can serve as a competitive alternative for continuous signal representation in mid-level tasks in computer vision, such as 3D representation learning from 2D observations.

