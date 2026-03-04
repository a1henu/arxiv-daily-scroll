---
layout: default
title: From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?
---

# From Language to Action: Can LLM-Based Agents Be Used for Embodied Robot Cognition?
**arXiv**：[2603.03148v1](https://arxiv.org/abs/2603.03148) · [PDF](https://arxiv.org/pdf/2603.03148.pdf)  
**作者**：Shinas Shaji, Fabian Huppertz, Alex Mitrevski, Sebastian Houben  

**一句话要点**：提出基于LLM的认知架构，用于模拟家庭环境中机器人任务规划与执行

**关键词**：大语言模型, 机器人认知架构, 任务规划, 模拟环境, 记忆机制, 执行恢复

## 3 点简述
- 研究LLM作为核心组件在机器人认知架构中的适用性，以桥接语言与低层功能
- 设计包含工作记忆和情景记忆的架构，支持经验学习和适应，通过高层工具实现环境交互
- 在模拟家庭任务中评估，LLM驱动代理能完成结构化任务，但存在幻觉和指令遵循问题

## 摘要（原文）

> In order to flexibly act in an everyday environment, a robotic agent needs a variety of cognitive capabilities that enable it to reason about plans and perform execution recovery. Large language models (LLMs) have been shown to demonstrate emergent cognitive aspects, such as reasoning and language understanding; however, the ability to control embodied robotic agents requires reliably bridging high-level language to low-level functionalities for perception and control. In this paper, we investigate the extent to which an LLM can serve as a core component for planning and execution reasoning in a cognitive robot architecture. For this purpose, we propose a cognitive architecture in which an agentic LLM serves as the core component for planning and reasoning, while components for working and episodic memories support learning from experience and adaptation. An instance of the architecture is then used to control a mobile manipulator in a simulated household environment, where environment interaction is done through a set of high-level tools for perception, reasoning, navigation, grasping, and placement, all of which are made available to the LLM-based agent. We evaluate our proposed system on two household tasks (object placement and object swapping), which evaluate the agent's reasoning, planning, and memory utilisation. The results demonstrate that the LLM-driven agent can complete structured tasks and exhibits emergent adaptation and memory-guided planning, but also reveal significant limitations, such as hallucinations about the task success and poor instruction following by refusing to acknowledge and complete sequential tasks. These findings highlight both the potential and challenges of employing LLMs as embodied cognitive controllers for autonomous robots.

