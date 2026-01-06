---
layout: default
title: Dancing Points: Synthesizing Ballroom Dancing with Three-Point Inputs
---

# Dancing Points: Synthesizing Ballroom Dancing with Three-Point Inputs
**arXiv**：[2601.02096v1](https://arxiv.org/abs/2601.02096) · [PDF](https://arxiv.org/pdf/2601.02096.pdf)  
**作者**：Peizhuo Li, Sebastian Starke, Yuting Ye, Olga Sorkine-Hornung  

**一句话要点**：提出基于三点轨迹的舞伴运动合成方法，以简化双人舞交互建模

**关键词**：运动合成, 三点轨迹, 双人舞交互, 确定性神经网络, 虚拟现实应用, 数据效率

## 3 点简述
- 核心问题：双人舞运动多样且交互复杂，高维全身运动建模困难
- 方法要点：使用VR设备三点轨迹作为运动描述符，通过MLP网络从领舞者轨迹预测伴舞者轨迹
- 实验或效果：方法在舞厅舞数据集上有效，并推广到LaFAN等更大数据集，提供高效解决方案

## 摘要（原文）

> Ballroom dancing is a structured yet expressive motion category. Its highly diverse movement and complex interactions between leader and follower dancers make the understanding and synthesis challenging. We demonstrate that the three-point trajectory available from a virtual reality (VR) device can effectively serve as a dancer's motion descriptor, simplifying the modeling and synthesis of interplay between dancers' full-body motions down to sparse trajectories. Thanks to the low dimensionality, we can employ an efficient MLP network to predict the follower's three-point trajectory directly from the leader's three-point input for certain types of ballroom dancing, addressing the challenge of modeling high-dimensional full-body interaction. It also prevents our method from overfitting thanks to its compact yet explicit representation. By leveraging the inherent structure of the movements and carefully planning the autoregressive procedure, we show a deterministic neural network is able to translate three-point trajectories into a virtual embodied avatar, which is typically considered under-constrained and requires generative models for common motions. In addition, we demonstrate this deterministic approach generalizes beyond small, structured datasets like ballroom dancing, and performs robustly on larger, more diverse datasets such as LaFAN. Our method provides a computationally- and data-efficient solution, opening new possibilities for immersive paired dancing applications. Code and pre-trained models for this paper are available at https://peizhuoli.github.io/dancing-points.

