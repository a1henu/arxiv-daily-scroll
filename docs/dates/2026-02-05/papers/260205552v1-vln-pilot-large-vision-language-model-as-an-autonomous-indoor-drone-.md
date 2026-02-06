---
layout: default
title: VLN-Pilot: Large Vision-Language Model as an Autonomous Indoor Drone Operator
---

# VLN-Pilot: Large Vision-Language Model as an Autonomous Indoor Drone Operator
**arXiv**：[2602.05552v1](https://arxiv.org/abs/2602.05552) · [PDF](https://arxiv.org/pdf/2602.05552.pdf)  
**作者**：Bessie Dominguez-Dager, Sergio Suescun-Ferrandiz, Felix Escalona, Francisco Gomez-Donoso, Miguel Cazorla  

**一句话要点**：提出VLN-Pilot框架，利用大视觉语言模型作为自主室内无人机操作员，实现基于自然语言指令的导航。

**关键词**：视觉语言模型, 无人机导航, 室内自主飞行, 自然语言指令, 多模态推理, 语义理解

## 3 点简述
- 核心问题：在GPS缺失的室内环境中，如何实现无人机基于自由形式自然语言指令的自主导航，替代传统规则或几何路径规划方法。
- 方法要点：通过大视觉语言模型的多模态推理能力，将语言指令与视觉观察结合，进行语义理解和轨迹规划，支持空间关系推理和障碍物避让。
- 实验或效果：在自定义逼真室内模拟基准上验证，模型驱动的代理在复杂指令跟随任务中达到高成功率，包括多语义目标的长时程导航。

## 摘要（原文）

> This paper introduces VLN-Pilot, a novel framework in which a large Vision-and-Language Model (VLLM) assumes the role of a human pilot for indoor drone navigation. By leveraging the multimodal reasoning abilities of VLLMs, VLN-Pilot interprets free-form natural language instructions and grounds them in visual observations to plan and execute drone trajectories in GPS-denied indoor environments. Unlike traditional rule-based or geometric path-planning approaches, our framework integrates language-driven semantic understanding with visual perception, enabling context-aware, high-level flight behaviors with minimal task-specific engineering. VLN-Pilot supports fully autonomous instruction-following for drones by reasoning about spatial relationships, obstacle avoidance, and dynamic reactivity to unforeseen events. We validate our framework on a custom photorealistic indoor simulation benchmark and demonstrate the ability of the VLLM-driven agent to achieve high success rates on complex instruction-following tasks, including long-horizon navigation with multiple semantic targets. Experimental results highlight the promise of replacing remote drone pilots with a language-guided autonomous agent, opening avenues for scalable, human-friendly control of indoor UAVs in tasks such as inspection, search-and-rescue, and facility monitoring. Our results suggest that VLLM-based pilots may dramatically reduce operator workload while improving safety and mission flexibility in constrained indoor environments.

