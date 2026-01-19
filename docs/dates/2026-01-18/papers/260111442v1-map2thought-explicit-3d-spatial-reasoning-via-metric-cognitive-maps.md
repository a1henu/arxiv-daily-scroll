---
layout: default
title: Map2Thought: Explicit 3D Spatial Reasoning via Metric Cognitive Maps
---

# Map2Thought: Explicit 3D Spatial Reasoning via Metric Cognitive Maps
**arXiv**：[2601.11442v1](https://arxiv.org/abs/2601.11442) · [PDF](https://arxiv.org/pdf/2601.11442.pdf)  
**作者**：Xiangjun Gao, Zhensong Zhang, Dave Zhenyu Chen, Songcen Xu, Long Quan, Eduardo Pérez-Pellitero, Youngkyoon Jang  

**一句话要点**：提出Map2Thought框架，通过度量认知地图和认知思维链实现3D视觉语言模型的显式空间推理。

**关键词**：3D空间推理, 度量认知地图, 认知思维链, 视觉语言模型, 可解释AI, 几何理解

## 3 点简述
- 核心问题：3D视觉语言模型缺乏显式和可解释的空间推理能力。
- 方法要点：结合离散网格和连续度量表示的度量认知地图，以及基于确定性操作的认知思维链进行几何推理。
- 实验或效果：在VSI-Bench上，使用一半监督达到59.9%准确率，优于现有方法，尤其在低数据量下表现突出。

## 摘要（原文）

> We propose Map2Thought, a framework that enables explicit and interpretable spatial reasoning for 3D VLMs. The framework is grounded in two key components: Metric Cognitive Map (Metric-CogMap) and Cognitive Chain-of-Thought (Cog-CoT). Metric-CogMap provides a unified spatial representation by integrating a discrete grid for relational reasoning with a continuous, metric-scale representation for precise geometric understanding. Building upon the Metric-CogMap, Cog-CoT performs explicit geometric reasoning through deterministic operations, including vector operations, bounding-box distances, and occlusion-aware appearance order cues, producing interpretable inference traces grounded in 3D structure. Experimental results show that Map2Thought enables explainable 3D understanding, achieving 59.9% accuracy using only half the supervision, closely matching the 60.9% baseline trained with the full dataset. It consistently outperforms state-of-the-art methods by 5.3%, 4.8%, and 4.0% under 10%, 25%, and 50% training subsets, respectively, on the VSI-Bench.

