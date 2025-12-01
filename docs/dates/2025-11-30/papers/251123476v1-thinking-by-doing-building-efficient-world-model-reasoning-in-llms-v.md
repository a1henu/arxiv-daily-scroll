---
layout: default
title: Thinking by Doing: Building Efficient World Model Reasoning in LLMs via Multi-turn Interaction
---

# Thinking by Doing: Building Efficient World Model Reasoning in LLMs via Multi-turn Interaction
**arXiv**：[2511.23476v1](https://arxiv.org/abs/2511.23476) · [PDF](https://arxiv.org/pdf/2511.23476.pdf)  
**作者**：Bao Shu, Yan Cai, Jianjian Sun, Chunrui Han, En Yu, Liang Zhao, Jingcheng Hu, Yinmin Zhang, Haoran Lv, Yuang Peng, Zheng Ge, Xiangyu Zhang, Daxin Jiang, Xiangyu Yue  

**一句话要点**：提出WMAct方法，通过多轮交互构建高效世界模型推理，解决LLM在复杂环境中的规划问题。

**关键词**：世界模型推理, 多轮交互, 奖励重缩放, 交互频率退火, LLM代理, 主动学习

## 3 点简述
- 核心问题：现有多轮交互方法采用僵化推理过程，限制模型主动学习，阻碍高效世界模型推理。
- 方法要点：引入奖励重缩放机制和交互频率退火策略，解放模型结构化推理，促进主动学习和环境动态内化。
- 实验或效果：在Sokoban、Maze和Taxi等任务上验证，WMAct实现单轮解决多轮任务，提升推理基准性能并增强可迁移性。

## 摘要（原文）

> Developing robust world model reasoning is crucial for large language model (LLM) agents to plan and interact in complex environments. While multi-turn interaction offers a superior understanding of environmental dynamics via authentic feedback, current approaches often impose a rigid reasoning process, which constrains the model's active learning, ultimately hindering efficient world model reasoning. To address these issues, we explore world-model internalization through efficient interaction and active reasoning (WMAct), which liberates the model from structured reasoning, allowing the model to shape thinking directly through its doing, and achieves effective and efficient world model reasoning with two key mechanisms: (1) a reward rescaling mechanism adjusting outcome reward based on action efficacy to incentivize redundancy reduction and purposeful interaction; (2) an interaction frequency annealing strategy to progressively reduce the maximum allowed interaction turns, which compels the model to condense its learning and internalize environmental dynamics rather than over-relying on environmental cues. Our experiments on Sokoban, Maze, and Taxi show that WMAct yields effective world model reasoning capable of resolving tasks in a single turn that previously required multiple interactions and fosters strong transferability to complex environments, improving performance on a suite of reasoning benchmarks.

