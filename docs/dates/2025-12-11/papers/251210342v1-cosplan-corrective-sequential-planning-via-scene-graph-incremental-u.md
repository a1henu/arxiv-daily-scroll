---
layout: default
title: CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates
---

# CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates
**arXiv**：[2512.10342v1](https://arxiv.org/abs/2512.10342) · [PDF](https://arxiv.org/pdf/2512.10342.pdf)  
**作者**：Shresth Grover, Priyank Pathak, Akash Kumar, Vibhav Vineet, Yogesh S Rawat  

**一句话要点**：提出基于场景图增量更新的无训练方法SGI，以增强视觉语言模型在纠错式视觉序列规划中的性能。

**关键词**：视觉序列规划, 纠错规划, 场景图推理, 视觉语言模型, 无训练方法, 基准评估

## 3 点简述
- 核心问题：视觉语言模型在视觉序列规划中难以检测和纠正非最优步骤，导致目标达成困难。
- 方法要点：引入场景图增量更新（SGI），在初始与目标状态间添加中间推理步骤，提升序列推理能力。
- 实验或效果：在CoSPlan基准上，SGI使VLMs平均性能提升5.2%，并泛化至传统规划任务如Plan-Bench和VQA。

## 摘要（原文）

> Large-scale Vision-Language Models (VLMs) exhibit impressive complex reasoning capabilities but remain largely unexplored in visual sequential planning, i.e., executing multi-step actions towards a goal. Additionally, practical sequential planning often involves non-optimal (erroneous) steps, challenging VLMs to detect and correct such steps. We propose Corrective Sequential Planning Benchmark (CoSPlan) to evaluate VLMs in error-prone, vision-based sequential planning tasks across 4 domains: maze navigation, block rearrangement, image reconstruction,and object reorganization. CoSPlan assesses two key abilities: Error Detection (identifying non-optimal action) and Step Completion (correcting and completing action sequences to reach the goal). Despite using state-of-the-art reasoning techniques such as Chain-of-Thought and Scene Graphs, VLMs (e.g. Intern-VLM and Qwen2) struggle on CoSPlan, failing to leverage contextual cues to reach goals. Addressing this, we propose a novel training-free method, Scene Graph Incremental updates (SGI), which introduces intermediate reasoning steps between the initial and goal states. SGI helps VLMs reason about sequences, yielding an average performance gain of 5.2%. In addition to enhancing reliability in corrective sequential planning, SGI generalizes to traditional planning tasks such as Plan-Bench and VQA.

