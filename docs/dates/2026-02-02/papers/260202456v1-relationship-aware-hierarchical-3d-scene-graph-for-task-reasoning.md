---
layout: default
title: Relationship-Aware Hierarchical 3D Scene Graph for Task Reasoning
---

# Relationship-Aware Hierarchical 3D Scene Graph for Task Reasoning
**arXiv**：[2602.02456v1](https://arxiv.org/abs/2602.02456) · [PDF](https://arxiv.org/pdf/2602.02456.pdf)  
**作者**：Albert Gassol Puigjaner, Angelos Zacharia, Kostas Alexis  

**一句话要点**：提出关系感知的层次化3D场景图，结合视觉语言模型和大语言模型，以增强自主机器人的任务推理能力。

**关键词**：3D场景图, 关系推理, 视觉语言模型, 大语言模型, 自主机器人, 任务推理

## 3 点简述
- 核心问题：传统SLAM方法缺乏高层次抽象和关系推理，限制了自主代理的环境理解和任务执行。
- 方法要点：构建增强的层次化3D场景图，集成开放词汇特征，利用视觉语言模型推断语义关系，并引入任务推理模块结合大语言模型进行解释。
- 实验或效果：在四足机器人上部署，验证了方法在多种环境和任务中的推理能力，提升了智能交互性能。

## 摘要（原文）

> Representing and understanding 3D environments in a structured manner is crucial for autonomous agents to navigate and reason about their surroundings. While traditional Simultaneous Localization and Mapping (SLAM) methods generate metric reconstructions and can be extended to metric-semantic mapping, they lack a higher level of abstraction and relational reasoning. To address this gap, 3D scene graphs have emerged as a powerful representation for capturing hierarchical structures and object relationships. In this work, we propose an enhanced hierarchical 3D scene graph that integrates open-vocabulary features across multiple abstraction levels and supports object-relational reasoning. Our approach leverages a Vision Language Model (VLM) to infer semantic relationships. Notably, we introduce a task reasoning module that combines Large Language Models (LLM) and a VLM to interpret the scene graph's semantic and relational information, enabling agents to reason about tasks and interact with their environment more intelligently. We validate our method by deploying it on a quadruped robot in multiple environments and tasks, highlighting its ability to reason about them.

