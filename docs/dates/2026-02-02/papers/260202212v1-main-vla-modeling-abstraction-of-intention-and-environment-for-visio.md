---
layout: default
title: MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models
---

# MAIN-VLA: Modeling Abstraction of Intention and eNvironment for Vision-Language-Action Models
**arXiv**：[2602.02212v1](https://arxiv.org/abs/2602.02212) · [PDF](https://arxiv.org/pdf/2602.02212.pdf)  
**作者**：Zheyuan Zhou, Liang Du, Zixun Sun, Xiaoyu Zhou, Ruimin Ye, Qihao Chen, Yinda Chen, Lemiao Qiu  

**一句话要点**：提出MAIN-VLA框架，通过建模意图与环境抽象，提升视觉-语言-动作模型在复杂动态环境中的决策效率与质量。

**关键词**：视觉-语言-动作模型, 意图抽象, 环境语义抽象, 语义对齐, 推理效率, 复杂动态环境

## 3 点简述
- 核心问题：现有视觉-语言-动作模型在复杂动态环境中难以从冗余传感器流中提取动作关键信号，导致决策效率低下。
- 方法要点：引入意图抽象和环境语义抽象，将语言指令和视觉流转换为紧凑语义原语和结构化拓扑表示，实现深度语义对齐。
- 实验或效果：在开放世界Minecraft和大规模PvP游戏中验证，MAIN-VLA在决策质量、泛化能力和推理效率上达到新最优水平。

## 摘要（原文）

> Despite significant progress in Visual-Language-Action (VLA), in highly complex and dynamic environments that involve real-time unpredictable interactions (such as 3D open worlds and large-scale PvP games), existing approaches remain inefficient at extracting action-critical signals from redundant sensor streams. To tackle this, we introduce MAIN-VLA, a framework that explicitly Models the Abstraction of Intention and eNvironment to ground decision-making in deep semantic alignment rather than superficial pattern matching. Specifically, our Intention Abstraction (IA) extracts verbose linguistic instructions and their associated reasoning into compact, explicit semantic primitives, while the Environment Semantics Abstraction (ESA) projects overwhelming visual streams into a structured, topological affordance representation. Furthermore, aligning these two abstract modalities induces an emergent attention-concentration effect, enabling a parameter-free token-pruning strategy that filters out perceptual redundancy without degrading performance. Extensive experiments in open-world Minecraft and large-scale PvP environments (Game for Peace and Valorant) demonstrate that MAIN-VLA sets a new state-of-the-art, which achieves superior decision quality, stronger generalization, and cutting-edge inference efficiency.

