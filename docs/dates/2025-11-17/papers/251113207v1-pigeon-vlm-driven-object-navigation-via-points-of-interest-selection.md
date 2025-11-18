---
layout: default
title: PIGEON: VLM-Driven Object Navigation via Points of Interest Selection
---

# PIGEON: VLM-Driven Object Navigation via Points of Interest Selection
**arXiv**：[2511.13207v1](https://arxiv.org/abs/2511.13207) · [PDF](https://arxiv.org/pdf/2511.13207.pdf)  
**作者**：Cheng Peng, Zhenzhe Zhang, Cheng Chi, Xiaobao Wei, Yanhao Zhang, Heng Wang, Pengwei Wang, Zhongyuan Wang, Jing Liu, Shanghang Zhang  

**一句话要点**：提出PIGEON方法，通过兴趣点选择解决未知环境中物体导航问题

**关键词**：物体导航, 视觉语言模型, 兴趣点选择, 强化学习, 零样本转移

## 3 点简述
- 核心问题：未知环境中物体导航决策频率与智能性难以平衡，导致短视或不连续动作
- 方法要点：使用VLM选择兴趣点，结合轻量语义记忆和低级规划器提高决策频率
- 实验或效果：零样本转移在基准测试中达SOTA，RLVR增强语义引导和实时推理能力

## 摘要（原文）

> Navigating to a specified object in an unknown environment is a fundamental yet challenging capability of embodied intelligence. However, current methods struggle to balance decision frequency with intelligence, resulting in decisions lacking foresight or discontinuous actions. In this work, we propose PIGEON: Point of Interest Guided Exploration for Object Navigation with VLM, maintaining a lightweight and semantically aligned snapshot memory during exploration as semantic input for the exploration strategy. We use a large Visual-Language Model (VLM), named PIGEON-VL, to select Points of Interest (PoI) formed during exploration and then employ a lower-level planner for action output, increasing the decision frequency. Additionally, this PoI-based decision-making enables the generation of Reinforcement Learning with Verifiable Reward (RLVR) data suitable for simulators. Experiments on classic object navigation benchmarks demonstrate that our zero-shot transfer method achieves state-of-the-art performance, while RLVR further enhances the model's semantic guidance capabilities, enabling deep reasoning during real-time navigation.

