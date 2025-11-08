---
layout: default
title: SAFe-Copilot: Unified Shared Autonomy Framework
---

# SAFe-Copilot: Unified Shared Autonomy Framework
**arXiv**：[2511.04664v1](https://arxiv.org/abs/2511.04664) · [PDF](https://arxiv.org/pdf/2511.04664.pdf)  
**作者**：Phat Nguyen, Erfan Aasi, Shiva Sreeram, Guy Rosman, Andrew Silva, Sertac Karaman, Daniela Rus  

**一句话要点**：提出统一共享自治框架，通过高层抽象整合人类输入与自主规划，以解决自动驾驶在罕见场景中的脆弱性问题。

**关键词**：共享自治, 自动驾驶, 视觉语言模型, 意图推断, 语义仲裁, 基准测试

## 3 点简述
- 核心问题：自动驾驶在罕见、模糊和分布外场景中脆弱，而人类依赖上下文推理成功。
- 方法要点：利用视觉语言模型从多模态线索推断驾驶意图，并在语义层面仲裁人类与自主控制。
- 实验或效果：在Bench2Drive基准测试中，碰撞率显著降低，整体性能优于纯自主系统。

## 摘要（原文）

> Autonomous driving systems remain brittle in rare, ambiguous, and
> out-of-distribution scenarios, where human driver succeed through contextual
> reasoning. Shared autonomy has emerged as a promising approach to mitigate such
> failures by incorporating human input when autonomy is uncertain. However, most
> existing methods restrict arbitration to low-level trajectories, which
> represent only geometric paths and therefore fail to preserve the underlying
> driving intent. We propose a unified shared autonomy framework that integrates
> human input and autonomous planners at a higher level of abstraction. Our
> method leverages Vision Language Models (VLMs) to infer driver intent from
> multi-modal cues -- such as driver actions and environmental context -- and to
> synthesize coherent strategies that mediate between human and autonomous
> control. We first study the framework in a mock-human setting, where it
> achieves perfect recall alongside high accuracy and precision. A human-subject
> survey further shows strong alignment, with participants agreeing with
> arbitration outcomes in 92% of cases. Finally, evaluation on the Bench2Drive
> benchmark demonstrates a substantial reduction in collision rate and
> improvement in overall performance compared to pure autonomy. Arbitration at
> the level of semantic, language-based representations emerges as a design
> principle for shared autonomy, enabling systems to exercise common-sense
> reasoning and maintain continuity with human intent.

