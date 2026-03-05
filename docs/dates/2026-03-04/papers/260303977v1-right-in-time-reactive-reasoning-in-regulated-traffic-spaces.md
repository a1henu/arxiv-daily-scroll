---
layout: default
title: Right in Time: Reactive Reasoning in Regulated Traffic Spaces
---

# Right in Time: Reactive Reasoning in Regulated Traffic Spaces
**arXiv**：[2603.03977v1](https://arxiv.org/abs/2603.03977) · [PDF](https://arxiv.org/pdf/2603.03977.pdf)  
**作者**：Simon Kohaut, Benedict Flade, Julian Eggert, Kristian Kersting, Devendra Singh Dhami  

**一句话要点**：提出反应式任务设计框架，结合概率逻辑与反应推理，实现交通空间中自主代理的在线精确推理。

**关键词**：概率一阶逻辑, 反应推理, 自主代理, 交通法规, 在线推理, 混合域推理

## 3 点简述
- 核心问题：概率一阶逻辑推理在共享交通空间中计算成本高，限制在线应用。
- 方法要点：整合概率任务设计与反应电路，基于数据流变化频率细分推理公式，实现局部重评估。
- 实验或效果：在真实船舶和模拟无人机场景中，相比非反应式方法，速度提升数个数量级。

## 摘要（原文）

> Exact inference in probabilistic First-Order Logic offers a promising yet computationally costly approach for regulating the behavior of autonomous agents in shared traffic spaces. While prior methods have combined logical and probabilistic data into decision-making frameworks, their application is often limited to pre-flight checks due to the complexity of reasoning across vast numbers of possible universes. In this work, we propose a reactive mission design framework that jointly considers uncertain environmental data and declarative, logical traffic regulations. By synthesizing Probabilistic Mission Design (ProMis) with reactive reasoning facilitated by Reactive Circuits (RC), we enable online, exact probabilistic inference over hybrid domains. Our approach leverages the Frequency of Change inherent in heterogeneous data streams to subdivide inference formulas into memoized, isolated tasks, ensuring that only the specific components affected by new sensor data are re-evaluated. In experiments involving both real-world vessel data and simulated drone traffic in dense urban scenarios, we demonstrate that our approach provides orders of magnitude in speedup over ProMis without reactive paradigms. This allows intelligent transportation systems, such as Unmanned Aircraft Systems (UAS), to actively assert safety and legal compliance during operations rather than relying solely on preparation procedures.

