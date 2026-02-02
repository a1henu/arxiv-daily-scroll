---
layout: default
title: AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
---

# AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement
**arXiv**：[2601.22758v1](https://arxiv.org/abs/2601.22758) · [PDF](https://arxiv.org/pdf/2601.22758.pdf)  
**作者**：Libin Qiu, Zhirong Gao, Junfu Chen, Yuhang Ye, Weizhi Huang, Xiaobo Xue, Wenkai Qiu, Shuo Tang  

**一句话要点**：提出AutoRefine框架，从轨迹中提取双形式经验模式以解决LLM代理持续精炼问题

**关键词**：LLM代理, 经验提取, 持续学习, 子任务协调, 知识维护, 轨迹分析

## 3 点简述
- 核心问题：LLM代理缺乏经验积累机制，现有方法无法捕获复杂子任务程序逻辑且经验库易退化
- 方法要点：提取双形式经验模式，包括子代理和技能模式，并引入持续维护机制进行评分、剪枝和合并
- 实验或效果：在ALFWorld、ScienceWorld和TravelPlanner上评估，性能提升显著，步骤减少20-73%，自动提取优于手动设计

## 摘要（原文）

> Large language model agents often fail to accumulate knowledge from experience, treating each task as an independent challenge. Recent methods extract experience as flattened textual knowledge, which cannot capture procedural logic of complex subtasks. They also lack maintenance mechanisms, causing repository degradation as experience accumulates. We introduce AutoRefine, a framework that extracts and maintains dual-form Experience Patterns from agent execution histories. For procedural subtasks, we extract specialized subagents with independent reasoning and memory. For static knowledge, we extract skill patterns as guidelines or code snippets. A continuous maintenance mechanism scores, prunes, and merges patterns to prevent repository degradation. Evaluated on ALFWorld, ScienceWorld, and TravelPlanner, AutoRefine achieves 98.4%, 70.4%, and 27.1% respectively, with 20-73% step reductions. On TravelPlanner, automatic extraction exceeds manually designed systems (27.1% vs 12.1%), demonstrating its ability to capture procedural coordination.

