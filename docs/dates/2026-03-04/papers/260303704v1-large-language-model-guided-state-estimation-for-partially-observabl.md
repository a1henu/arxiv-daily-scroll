---
layout: default
title: Large-Language-Model-Guided State Estimation for Partially Observable Task and Motion Planning
---

# Large-Language-Model-Guided State Estimation for Partially Observable Task and Motion Planning
**arXiv**：[2603.03704v1](https://arxiv.org/abs/2603.03704) · [PDF](https://arxiv.org/pdf/2603.03704.pdf)  
**作者**：Yoonwoo Kim, Raghav Arora, Roberto Martín-Martín, Peter Stone, Ben Abbatematteo, Yoonchang Sung  

**一句话要点**：提出CoCo-TAMP框架，利用大语言模型引导状态估计以解决部分可观测环境下的机器人任务与运动规划问题。

**关键词**：部分可观测规划, 大语言模型引导, 分层状态估计, 任务与运动规划, 常识推理

## 3 点简述
- 核心问题：部分可观测环境中机器人规划需处理不确定性，传统方法忽略任务无关对象。
- 方法要点：引入大语言模型提供常识知识，指导分层状态估计以优化任务相关对象信念。
- 实验或效果：相比无常识知识基线，在仿真和真实演示中分别平均减少62.7%和72.6%的规划与执行时间。

## 摘要（原文）

> Robot planning in partially observable environments, where not all objects are known or visible, is a challenging problem, as it requires reasoning under uncertainty through partially observable Markov decision processes. During the execution of a computed plan, a robot may unexpectedly observe task-irrelevant objects, which are typically ignored by naive planners. In this work, we propose incorporating two types of common-sense knowledge: (1) certain objects are more likely to be found in specific locations; and (2) similar objects are likely to be co-located, while dissimilar objects are less likely to be found together. Manually engineering such knowledge is complex, so we explore leveraging the powerful common-sense reasoning capabilities of large language models (LLMs). Our planning and execution framework, CoCo-TAMP, introduces a hierarchical state estimation that uses LLM-guided information to shape the belief over task-relevant objects, enabling efficient solutions to long-horizon task and motion planning problems. In experiments, CoCo-TAMP achieves an average reduction of 62.7 in planning and execution time in simulation, and 72.6 in real-world demonstrations, compared to a baseline that does not incorporate either type of common-sense knowledge.

