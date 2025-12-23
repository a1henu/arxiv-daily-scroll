---
layout: default
title: MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation
---

# MaP-AVR: A Meta-Action Planner for Agents Leveraging Vision Language Models and Retrieval-Augmented Generation
**arXiv**：[2512.19453v1](https://arxiv.org/abs/2512.19453) · [PDF](https://arxiv.org/pdf/2512.19453.pdf)  
**作者**：Zhenglong Guo, Yiming Zhao, Feng Jiang, Heng Jin, Zongbao Feng, Jianbin Zhou, Siyuan Xu  

**一句话要点**：提出MaP-AVR元动作规划器，通过元动作抽象和检索增强生成提升具身智能体任务规划能力。

**关键词**：具身智能, 元动作规划, 检索增强生成, 视觉语言模型, 任务分解, 机器人控制

## 3 点简述
- 核心问题：现有具身智能系统依赖任务规划器分解高级任务，但技能集定义不足，影响泛化能力。
- 方法要点：将规划结果抽象为元动作，结合检索增强生成技术，利用人类标注演示数据库进行上下文学习。
- 实验或效果：在GPT-4o和OmniGibson平台上验证，相比当前最优方法展现出有前景的性能。

## 摘要（原文）

> Embodied robotic AI systems designed to manage complex daily tasks rely on a task planner to understand and decompose high-level tasks. While most research focuses on enhancing the task-understanding abilities of LLMs/VLMs through fine-tuning or chain-of-thought prompting, this paper argues that defining the planned skill set is equally crucial. To handle the complexity of daily environments, the skill set should possess a high degree of generalization ability. Empirically, more abstract expressions tend to be more generalizable. Therefore, we propose to abstract the planned result as a set of meta-actions. Each meta-action comprises three components: {move/rotate, end-effector status change, relationship with the environment}. This abstraction replaces human-centric concepts, such as grasping or pushing, with the robot's intrinsic functionalities. As a result, the planned outcomes align seamlessly with the complete range of actions that the robot is capable of performing. Furthermore, to ensure that the LLM/VLM accurately produces the desired meta-action format, we employ the Retrieval-Augmented Generation (RAG) technique, which leverages a database of human-annotated planning demonstrations to facilitate in-context learning. As the system successfully completes more tasks, the database will self-augment to continue supporting diversity. The meta-action set and its integration with RAG are two novel contributions of our planner, denoted as MaP-AVR, the meta-action planner for agents composed of VLM and RAG. To validate its efficacy, we design experiments using GPT-4o as the pre-trained LLM/VLM model and OmniGibson as our robotic platform. Our approach demonstrates promising performance compared to the current state-of-the-art method. Project page: https://map-avr.github.io/.

