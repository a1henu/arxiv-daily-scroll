---
layout: default
title: Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning
---

# Memory Matters More: Event-Centric Memory as a Logic Map for Agent Searching and Reasoning
**arXiv**：[2601.04726v1](https://arxiv.org/abs/2601.04726) · [PDF](https://arxiv.org/pdf/2601.04726.pdf)  
**作者**：Yuyang Hu, Jiongnan Liu, Jiejun Tan, Yutao Zhu, Zhicheng Dou  

**一句话要点**：提出事件中心记忆框架CompassMem，以事件图组织记忆支持智能代理的长时推理

**关键词**：智能代理, 记忆机制, 事件图, 长时推理, 逻辑检索

## 3 点简述
- 现有记忆方法组织扁平且检索依赖浅层语义，难以捕获逻辑关系
- CompassMem基于事件分割理论，将经验分段为事件并构建逻辑关系图
- 在LoCoMo和NarrativeQA实验中，CompassMem提升多骨干模型的检索与推理性能

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed as intelligent agents that reason, plan, and interact with their environments. To effectively scale to long-horizon scenarios, a key capability for such agents is a memory mechanism that can retain, organize, and retrieve past experiences to support downstream decision-making. However, most existing approaches organize and store memories in a flat manner and rely on simple similarity-based retrieval techniques. Even when structured memory is introduced, existing methods often struggle to explicitly capture the logical relationships among experiences or memory units. Moreover, memory access is largely detached from the constructed structure and still depends on shallow semantic retrieval, preventing agents from reasoning logically over long-horizon dependencies. In this work, we propose CompassMem, an event-centric memory framework inspired by Event Segmentation Theory. CompassMem organizes memory as an Event Graph by incrementally segmenting experiences into events and linking them through explicit logical relations. This graph serves as a logic map, enabling agents to perform structured and goal-directed navigation over memory beyond superficial retrieval, progressively gathering valuable memories to support long-horizon reasoning. Experiments on LoCoMo and NarrativeQA demonstrate that CompassMem consistently improves both retrieval and reasoning performance across multiple backbone models.

