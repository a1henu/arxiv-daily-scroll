---
layout: default
title: IROSA: Interactive Robot Skill Adaptation using Natural Language
---

# IROSA: Interactive Robot Skill Adaptation using Natural Language
**arXiv**：[2603.03897v1](https://arxiv.org/abs/2603.03897) · [PDF](https://arxiv.org/pdf/2603.03897.pdf)  
**作者**：Markus Knauer, Samuel Bustamante, Thomas Eiband, Alin Albu-Schäffer, Freek Stulp, João Silvério  

**一句话要点**：提出IROSA框架，通过自然语言交互实现工业机器人技能自适应

**关键词**：机器人技能自适应, 自然语言交互, 基础模型应用, 工业机器人, 模仿学习, 工具化架构

## 3 点简述
- 核心问题：结合基础模型与模仿学习以实现机器人技能自适应，在工业部署中应用有限
- 方法要点：采用基于工具的架构，利用预训练LLM选择和参数化工具，无需微调或直接交互
- 实验或效果：在7自由度扭矩控制机器人上演示，通过自然语言命令成功调整速度、轨迹和避障

## 摘要（原文）

> Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

