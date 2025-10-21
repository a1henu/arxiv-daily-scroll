---
layout: default
title: Intent-Driven LLM Ensemble Planning for Flexible Multi-Robot Disassembly: Demonstration on EV Batteries
---

# Intent-Driven LLM Ensemble Planning for Flexible Multi-Robot Disassembly: Demonstration on EV Batteries
**arXiv**：[2510.17576v1](https://arxiv.org/abs/2510.17576) · [PDF](https://arxiv.org/pdf/2510.17576.pdf)  
**作者**：Cansu Erdogan, Cesar Alan Contreras, Alireza Rastegarpanah, Manolis Chiou, Rustam Stolkin  

**一句话要点**：提出意图驱动的LLM集成规划方法，用于多机器人协作拆卸电动汽车电池。

**关键词**：多机器人规划, 意图驱动, LLM集成, 拆卸任务, 计算机视觉, 电动汽车电池

## 3 点简述
- 核心问题：多机器人在非结构化场景中规划复杂操作序列，需处理物体位置和配置的任意性。
- 方法要点：集成感知到文本编码、LLM生成候选序列、验证器约束和一致性过滤。
- 实验效果：在真实场景中评估，可靠映射意图到安全可执行计划，降低用户负担。

## 摘要（原文）

> This paper addresses the problem of planning complex manipulation tasks, in
> which multiple robots with different end-effectors and capabilities, informed
> by computer vision, must plan and execute concatenated sequences of actions on
> a variety of objects that can appear in arbitrary positions and configurations
> in unstructured scenes. We propose an intent-driven planning pipeline which can
> robustly construct such action sequences with varying degrees of supervisory
> input from a human using simple language instructions. The pipeline integrates:
> (i) perception-to-text scene encoding, (ii) an ensemble of large language
> models (LLMs) that generate candidate removal sequences based on the operator's
> intent, (iii) an LLM-based verifier that enforces formatting and precedence
> constraints, and (iv) a deterministic consistency filter that rejects
> hallucinated objects. The pipeline is evaluated on an example task in which two
> robot arms work collaboratively to dismantle an Electric Vehicle battery for
> recycling applications. A variety of components must be grasped and removed in
> specific sequences, determined by human instructions and/or by task-order
> feasibility decisions made by the autonomous system. On 200 real scenes with
> 600 operator prompts across five component classes, we used metrics of
> full-sequence correctness and next-task correctness to evaluate and compare
> five LLM-based planners (including ablation analyses of pipeline components).
> We also evaluated the LLM-based human interface in terms of time to execution
> and NASA TLX with human participant experiments. Results indicate that our
> ensemble-with-verification approach reliably maps operator intent to safe,
> executable multi-robot plans while maintaining low user effort.

