---
layout: default
title: One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation
---

# One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation
**arXiv**：[2602.15400v1](https://arxiv.org/abs/2602.15400) · [PDF](https://arxiv.org/pdf/2602.15400.pdf)  
**作者**：Zerui Li, Hongpei Zheng, Fangguo Zhao, Aidan Chan, Jian Zhou, Sihao Lin, Shijie Li, Qi Wu  

**一句话要点**：提出解耦设计与交互式度量世界表示，以提升多模态大语言模型在视觉语言导航中的性能。

**关键词**：视觉语言导航, 多模态大语言模型, 解耦设计, 度量世界表示, 零-shot学习, 机器人导航

## 3 点简述
- 当前基于MLLMs的导航系统因紧密耦合设计而性能受限，需分离空间状态估计与语义规划。
- 引入交互式度量世界表示，提供丰富一致信息，支持MLLMs进行推理与决策，并确保动作物理有效性。
- 在模拟和真实环境中实验，零-shot性能达到新SOTA，并验证了跨不同机器人的泛化能力。

## 摘要（原文）

> A navigable agent needs to understand both high-level semantic instructions and precise spatial perceptions. Building navigation agents centered on Multimodal Large Language Models (MLLMs) demonstrates a promising solution due to their powerful generalization ability. However, the current tightly coupled design dramatically limits system performance. In this work, we propose a decoupled design that separates low-level spatial state estimation from high-level semantic planning. Unlike previous methods that rely on predefined, oversimplified textual maps, we introduce an interactive metric world representation that maintains rich and consistent information, allowing MLLMs to interact with and reason on it for decision-making. Furthermore, counterfactual reasoning is introduced to further elicit MLLMs' capacity, while the metric world representation ensures the physical validity of the produced actions. We conduct comprehensive experiments in both simulated and real-world environments. Our method establishes a new zero-shot state-of-the-art, achieving 48.8\% Success Rate (SR) in R2R-CE and 42.2\% in RxR-CE benchmarks. Furthermore, to validate the versatility of our metric representation, we demonstrate zero-shot sim-to-real transfer across diverse embodiments, including a wheeled TurtleBot 4 and a custom-built aerial drone. These real-world deployments verify that our decoupled framework serves as a robust, domain-invariant interface for embodied Vision-and-Language navigation.

