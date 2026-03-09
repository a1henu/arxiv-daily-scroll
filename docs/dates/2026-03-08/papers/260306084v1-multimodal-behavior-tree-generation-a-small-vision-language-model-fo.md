---
layout: default
title: Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning
---

# Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning
**arXiv**：[2603.06084v1](https://arxiv.org/abs/2603.06084) · [PDF](https://arxiv.org/pdf/2603.06084.pdf)  
**作者**：Cristiano Battistini, Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci  

**一句话要点**：提出基于小规模视觉语言模型的多模态行为树生成方法，用于机器人任务规划。

**关键词**：视觉语言模型, 行为树生成, 机器人任务规划, 参数高效微调, 多模态数据集

## 3 点简述
- 核心问题：缺乏视觉观察与指令关联行为树的数据集，阻碍多模态任务规划。
- 方法要点：利用现有机器人数据构建数据集，通过参数高效微调训练500M至4B参数视觉语言模型。
- 实验或效果：微调后4B参数模型在家庭任务模拟中达到87%成功率，接近闭源模型性能。

## 摘要（原文）

> Large and small language models have been widely used for robotic task planning. At the same time, vision-language models (VLMs) have successfully tackled problems such as image captioning, scene understanding, and visual question answering. In this work, we combine these two approaches by deploying a compact, open-source multimodal model to generate behavior trees for robotic task planning. The main obstacle to achieving this goal is the lack of an existing dataset that links visual observations and instructions to executable behavior trees. We propose a method to construct such a dataset starting from existing robotic episodes (i.e., Open X-Embodiment), in which a large model serves as a teacher in a multi-stage generation pipeline. We use this dataset to fine-tune VLMs ranging from 500M to 4B parameters via parameter-efficient fine-tuning (PEFT). The generated behavior trees, compatible with the BehaviorTree.CPP library, are evaluated both offline, using structural and lexical metrics, and online through the execution of household tasks in a state-of-the-art embodied simulator. Our results demonstrate that our fine-tuned 4B-parameter VLM approaches the performance of state-of-the-art closed-source models, achieving an 87\% success rate while requiring only a fraction of the computational resources.

