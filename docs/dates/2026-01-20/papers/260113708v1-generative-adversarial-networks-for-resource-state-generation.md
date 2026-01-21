---
layout: default
title: Generative Adversarial Networks for Resource State Generation
---

# Generative Adversarial Networks for Resource State Generation
**arXiv**：[2601.13708v1](https://arxiv.org/abs/2601.13708) · [PDF](https://arxiv.org/pdf/2601.13708.pdf)  
**作者**：Shahbaz Shaik, Sourav Chatterjee, Sayantan Pramanik, Indranil Chakrabarty  

**一句话要点**：提出物理信息生成对抗网络框架，将量子资源态生成重构为逆设计任务。

**关键词**：生成对抗网络, 量子资源态生成, 逆设计, 物理信息学习, 量子态保真度, 约束驱动发现

## 3 点简述
- 核心问题：量子资源态生成作为逆设计任务，需满足物理约束如厄米性、迹一和正定性。
- 方法要点：嵌入任务特定效用函数于训练中，比较分解式与直接生成架构，结构强制约束优于仅损失方法。
- 实验或效果：在类Werner和Bell对角态上复现理论边界，保真度超98%，展示轻量有效约束驱动量子态发现。

## 摘要（原文）

> We introduce a physics-informed Generative Adversarial Network framework that recasts quantum resource-state generation as an inverse-design task. By embedding task-specific utility functions into training, the model learns to generate valid two-qubit states optimized for teleportation and entanglement broadcasting. Comparing decomposition-based and direct-generation architectures reveals that structural enforcement of Hermiticity, trace-one, and positivity yields higher fidelity and training stability than loss-only approaches. The framework reproduces theoretical resource boundaries for Werner-like and Bell-diagonal states with fidelities exceeding ~98%, establishing adversarial learning as a lightweight yet effective method for constraint-driven quantum-state discovery. This approach provides a scalable foundation for automated design of tailored quantum resources for information-processing applications, exemplified with teleportation and broadcasting of entanglement, and it opens up the possibility of using such states in efficient quantum network design.

