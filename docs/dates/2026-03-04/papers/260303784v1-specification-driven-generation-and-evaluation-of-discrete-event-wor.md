---
layout: default
title: Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism
---

# Specification-Driven Generation and Evaluation of Discrete-Event World Models via the DEVS Formalism
**arXiv**：[2603.03784v1](https://arxiv.org/abs/2603.03784) · [PDF](https://arxiv.org/pdf/2603.03784.pdf)  
**作者**：Zheyu Chen, Zhuohuan Li, Chuanhao Li  

**一句话要点**：提出基于DEVS形式化和LLM的离散事件世界模型生成方法，以结合显式模拟器可靠性与学习模型灵活性。

**关键词**：离散事件世界模型, DEVS形式化, LLM生成, 规范驱动验证, 在线适应, 事件轨迹分析

## 3 点简述
- 核心问题：现有世界模型方法在手工模拟器成本高与神经模型难验证间存在极端，缺乏可在线适应的可靠模型。
- 方法要点：采用DEVS形式化，通过分阶段LLM管道从自然语言规范合成显式可执行离散事件模型，分离结构推断与事件逻辑。
- 实验或效果：通过结构化事件轨迹验证规范约束，实现长时程一致性、可验证性和在线高效合成，适用于排队、任务规划等场景。

## 摘要（原文）

> World models are essential for planning and evaluation in agentic systems, yet existing approaches lie at two extremes: hand-engineered simulators that offer consistency and reproducibility but are costly to adapt, and implicit neural models that are flexible but difficult to constrain, verify, and debug over long horizons. We seek a principled middle ground that combines the reliability of explicit simulators with the flexibility of learned models, allowing world models to be adapted during online execution. By targeting a broad class of environments whose dynamics are governed by the ordering, timing, and causality of discrete events, such as queueing and service operations, embodied task planning, and message-mediated multi-agent coordination, we advocate explicit, executable discrete-event world models synthesized directly from natural-language specifications. Our approach adopts the DEVS formalism and introduces a staged LLM-based generation pipeline that separates structural inference of component interactions from component-level event and timing logic. To evaluate generated models without a unique ground truth, simulators emit structured event traces that are validated against specification-derived temporal and semantic constraints, enabling reproducible verification and localized diagnostics. Together, these contributions produce world models that are consistent over long-horizon rollouts, verifiable from observable behavior, and efficient to synthesize on demand during online execution.

