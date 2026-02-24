---
layout: default
title: Anticipate, Adapt, Act: A Hybrid Framework for Task Planning
---

# Anticipate, Adapt, Act: A Hybrid Framework for Task Planning
**arXiv**：[2602.19518v1](https://arxiv.org/abs/2602.19518) · [PDF](https://arxiv.org/pdf/2602.19518.pdf)  
**作者**：Nabanita Dash, Ayush Kaura, Shivam Singh, Ramandeep Singh, Snehasis Banerjee, Mohan Sridharan, K. Madhava Krishna  

**一句话要点**：提出混合框架整合LLM与RDDL，以提升机器人在复杂任务中预测和适应失败的能力。

**关键词**：任务规划, 混合框架, LLM集成, 概率决策, 失败预测, 机器人协作

## 3 点简述
- 核心问题：机器人在不确定任务中预测和适应失败以有效协作人类仍具挑战。
- 方法要点：结合LLM的通用预测与RDDL的概率序列决策，预测并处理能力或对象缺失导致的失败。
- 实验或效果：在VirtualHome 3D模拟环境中评估，相比基线性能显著提升。

## 摘要（原文）

> Anticipating and adapting to failures is a key capability robots need to collaborate effectively with humans in complex domains. This continues to be a challenge despite the impressive performance of state of the art AI planning systems and Large Language Models (LLMs) because of the uncertainty associated with the tasks and their outcomes. Toward addressing this challenge, we present a hybrid framework that integrates the generic prediction capabilities of an LLM with the probabilistic sequential decision-making capability of Relational Dynamic Influence Diagram Language. For any given task, the robot reasons about the task and the capabilities of the human attempting to complete it; predicts potential failures due to lack of ability (in the human) or lack of relevant domain objects; and executes actions to prevent such failures or recover from them. Experimental evaluation in the VirtualHome 3D simulation environment demonstrates substantial improvement in performance compared with state of the art baselines.

