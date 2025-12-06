---
layout: default
title: Bridging Probabilistic Inference and Behavior Trees: An Interactive Framework for Adaptive Multi-Robot Cooperation
---

# Bridging Probabilistic Inference and Behavior Trees: An Interactive Framework for Adaptive Multi-Robot Cooperation
**arXiv**：[2512.04404v1](https://arxiv.org/abs/2512.04404) · [PDF](https://arxiv.org/pdf/2512.04404.pdf)  
**作者**：Chaoran Wang, Jingyuan Sun, Yanhui Zhang, Changju Wu  

**一句话要点**：提出交互式推理行为树框架，以解决分布式多机器人自适应协作问题。

**关键词**：行为树, 主动推理, 多机器人协作, 自由能原理, 自适应决策, 分布式控制

## 3 点简述
- 核心问题：在部分可观测动态环境中，多机器人如何实现自适应协调决策。
- 方法要点：将行为树与主动推理结合，通过自由能最小化进行在线联合规划与执行。
- 实验或效果：仿真与实物实验验证，节点复杂度降低超70%，保持鲁棒性与可解释性。

## 摘要（原文）

> This paper proposes an Interactive Inference Behavior Tree (IIBT) framework that integrates behavior trees (BTs) with active inference under the free energy principle for distributed multi-robot decision-making. The proposed IIBT node extends conventional BTs with probabilistic reasoning, enabling online joint planning and execution across multiple robots. It remains fully compatible with standard BT architectures, allowing seamless integration into existing multi-robot control systems. Within this framework, multi-robot cooperation is formulated as a free-energy minimization process, where each robot dynamically updates its preference matrix based on perceptual inputs and peer intentions, thereby achieving adaptive coordination in partially observable and dynamic environments. The proposed approach is validated through both simulation and real-world experiments, including a multi-robot maze navigation and a collaborative manipulation task, compared against traditional BTs(https://youtu.be/KX_oT3IDTf4). Experimental results demonstrate that the IIBT framework reduces BT node complexity by over 70%, while maintaining robust, interpretable, and adaptive cooperative behavior under environmental uncertainty.

