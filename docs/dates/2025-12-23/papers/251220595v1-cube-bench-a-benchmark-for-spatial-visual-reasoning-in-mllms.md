---
layout: default
title: Cube Bench: A Benchmark for Spatial Visual Reasoning in MLLMs
---

# Cube Bench: A Benchmark for Spatial Visual Reasoning in MLLMs
**arXiv**：[2512.20595v1](https://arxiv.org/abs/2512.20595) · [PDF](https://arxiv.org/pdf/2512.20595.pdf)  
**作者**：Dhruv Anand, Ehsan Shareghi  

**一句话要点**：提出Cube Bench基准，用于评估多模态大语言模型在魔方场景下的空间与序列推理能力。

**关键词**：多模态大语言模型, 空间推理, 序列推理, 基准测试, 魔方求解, 自校正

## 3 点简述
- 核心问题：现有MLLMs在复杂空间序列任务（如魔方求解）中的推理能力缺乏系统评估。
- 方法要点：设计包含五种技能（如面重构、多步规划）的标准化魔方基准，使用统一度量进行对比。
- 实验效果：模型性能随魔方复杂度急剧下降，开源与闭源模型差距显著，自校正效果有限。

## 摘要（原文）

> We introduce Cube Bench, a Rubik's-cube benchmark for evaluating spatial and sequential reasoning in multimodal large language models (MLLMs). The benchmark decomposes performance into five skills: (i) reconstructing cube faces from images and text, (ii) choosing the optimal next move, (iii) predicting the outcome of a candidate move without applying it, (iv) executing multi-step plans while recovering from mistakes, and (v) detecting and revising one's own errors. Using a shared set of scrambled cube states, identical prompts and parsers, and a single distance-to-solved metric, we compare recent MLLMs side by side as a function of scramble depth. Across seven MLLMs, accuracy drops sharply with depth; once a trajectory stalls or diverges, models rarely recover, and high face-reconstruction accuracy does not guarantee competent action selection or multi-step execution. A pronounced closed- vs open-source gap emerges: the strongest closed model leads on both single-step perception tasks and multi-step control tasks, while open-weight models cluster near chance on the hardest settings; yet even the best MLLM degrades at higher cube complexity. A simple self-correction via reflective thinking yields modest gains but can also introduce overthinking. Cube Bench offers a compact, reproducible probe of sequential spatial reasoning in MLLMs.

