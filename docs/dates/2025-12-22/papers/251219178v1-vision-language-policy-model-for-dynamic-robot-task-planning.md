---
layout: default
title: Vision-Language-Policy Model for Dynamic Robot Task Planning
---

# Vision-Language-Policy Model for Dynamic Robot Task Planning
**arXiv**：[2512.19178v1](https://arxiv.org/abs/2512.19178) · [PDF](https://arxiv.org/pdf/2512.19178.pdf)  
**作者**：Jin Wang, Kim Tien Ly, Jacques Cloete, Nikos Tsagarakis, Ioannis Havoutis  

**一句话要点**：提出基于视觉-语言-策略模型的动态机器人任务规划框架，以解决非结构化环境中自然语言指令与自主执行的差距问题。

**关键词**：机器人任务规划, 视觉-语言模型, 动态策略调整, 跨具身泛化, 非结构化环境

## 3 点简述
- 核心问题：传统机器人任务规划方法难以桥接低层执行与高层任务推理，且无法在指令变化时动态更新策略，限制适应性和通用性。
- 方法要点：基于真实数据微调的视觉-语言模型，通过解释语义指令和场景推理生成行为策略，支持动态调整任务策略以适应变化。
- 实验或效果：在不同机器人和多种真实任务实验中，模型能高效适应新场景并动态更新策略，展示强规划自主性和跨具身泛化能力。

## 摘要（原文）

> Bridging the gap between natural language commands and autonomous execution in unstructured environments remains an open challenge for robotics. This requires robots to perceive and reason over the current task scene through multiple modalities, and to plan their behaviors to achieve their intended goals. Traditional robotic task-planning approaches often struggle to bridge low-level execution with high-level task reasoning, and cannot dynamically update task strategies when instructions change during execution, which ultimately limits their versatility and adaptability to new tasks. In this work, we propose a novel language model-based framework for dynamic robot task planning. Our Vision-Language-Policy (VLP) model, based on a vision-language model fine-tuned on real-world data, can interpret semantic instructions and integrate reasoning over the current task scene to generate behavior policies that control the robot to accomplish the task. Moreover, it can dynamically adjust the task strategy in response to changes in the task, enabling flexible adaptation to evolving task requirements. Experiments conducted with different robots and a variety of real-world tasks show that the trained model can efficiently adapt to novel scenarios and dynamically update its policy, demonstrating strong planning autonomy and cross-embodiment generalization. Videos: https://robovlp.github.io/

