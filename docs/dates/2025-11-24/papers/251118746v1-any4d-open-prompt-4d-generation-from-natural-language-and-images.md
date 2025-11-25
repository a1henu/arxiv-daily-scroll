---
layout: default
title: Any4D: Open-Prompt 4D Generation from Natural Language and Images
---

# Any4D: Open-Prompt 4D Generation from Natural Language and Images
**arXiv**：[2511.18746v1](https://arxiv.org/abs/2511.18746) · [PDF](https://arxiv.org/pdf/2511.18746.pdf)  
**作者**：Hao Li, Qiao Sun  

**一句话要点**：提出Primitive Embodied World Models以解决具身数据稀缺与长视频生成难题

**关键词**：具身世界模型, 视频生成, 语言-动作对齐, 闭环控制, 数据效率, 推理优化

## 3 点简述
- 核心问题：具身数据稀缺、高维和收集困难，限制语言与动作的细粒度对齐和长视频生成。
- 方法要点：限制视频生成为短时域，结合VLM规划器和SGG机制，实现细粒度对齐和闭环控制。
- 实验或效果：提高数据效率、降低推理延迟，支持原始策略在复杂任务中的组合泛化。

## 摘要（原文）

> While video-generation-based embodied world models have gained increasing attention, their reliance on large-scale embodied interaction data remains a key bottleneck. The scarcity, difficulty of collection, and high dimensionality of embodied data fundamentally limit the alignment granularity between language and actions and exacerbate the challenge of long-horizon video generation--hindering generative models from achieving a \textit{"GPT moment"} in the embodied domain. There is a naive observation: \textit{the diversity of embodied data far exceeds the relatively small space of possible primitive motions}. Based on this insight, we propose \textbf{Primitive Embodied World Models} (PEWM), which restricts video generation to fixed shorter horizons, our approach \textit{1) enables} fine-grained alignment between linguistic concepts and visual representations of robotic actions, \textit{2) reduces} learning complexity, \textit{3) improves} data efficiency in embodied data collection, and \textit{4) decreases} inference latency. By equipping with a modular Vision-Language Model (VLM) planner and a Start-Goal heatmap Guidance mechanism (SGG), PEWM further enables flexible closed-loop control and supports compositional generalization of primitive-level policies over extended, complex tasks. Our framework leverages the spatiotemporal vision priors in video models and the semantic awareness of VLMs to bridge the gap between fine-grained physical interaction and high-level reasoning, paving the way toward scalable, interpretable, and general-purpose embodied intelligence.

