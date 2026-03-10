---
layout: default
title: NaviDriveVLM: Decoupling High-Level Reasoning and Motion Planning for Autonomous Driving
---

# NaviDriveVLM: Decoupling High-Level Reasoning and Motion Planning for Autonomous Driving
**arXiv**：[2603.07901v1](https://arxiv.org/abs/2603.07901) · [PDF](https://arxiv.org/pdf/2603.07901.pdf)  
**作者**：Ximeng Tao, Pardis Taghavi, Dimitar Filev, Reza Langari, Gaurav Pandey  

**一句话要点**：提出NaviDriveVLM框架，通过解耦推理与规划解决自动驾驶中VLM的权衡问题。

**关键词**：自动驾驶, 视觉语言模型, 运动规划, 解耦框架, 端到端学习

## 3 点简述
- 现有VLM系统在高级推理与运动规划间存在权衡，大模型推理强但控制成本高，小模型反之。
- NaviDriveVLM采用解耦设计，用大规模Navigator进行推理，轻量Driver生成动作，保留推理能力并降低训练成本。
- 在nuScenes基准测试中，NaviDriveVLM在端到端运动规划上优于大型VLM基线。

## 摘要（原文）

> Vision-language models (VLMs) have emerged as a promising direction for end-to-end autonomous driving (AD) by jointly modeling visual observations, driving context, and language-based reasoning. However, existing VLM-based systems face a trade-off between high-level reasoning and motion planning: large models offer strong semantic understanding but are costly to adapt for precise control, whereas small VLM models can be fine-tuned efficiently but often exhibit weaker reasoning. We propose NaviDriveVLM, a decoupled framework that separates reasoning from action generation using a large-scale Navigator and a lightweight trainable Driver. This design preserves reasoning ability, reduces training cost, and provides an explicit interpretable intermediate representation for downstream planning. Experiments on the nuScenes benchmark show that NaviDriveVLM outperforms large VLM baselines in end-to-end motion planning.

