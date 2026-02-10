---
layout: default
title: What, Whether and How? Unveiling Process Reward Models for Thinking with Images Reasoning
---

# What, Whether and How? Unveiling Process Reward Models for Thinking with Images Reasoning
**arXiv**：[2602.08346v1](https://arxiv.org/abs/2602.08346) · [PDF](https://arxiv.org/pdf/2602.08346.pdf)  
**作者**：Yujin Zhou, Pengcheng Wen, Jiale Chen, Boqin Yin, Han Zhu, Jiaming Ji, Juntao Dai, Chi-Min Chan, Sirui Han  

**一句话要点**：提出首个图像思维推理过程奖励模型基准，以评估LVLMs在视觉推理过程中的错误识别能力。

**关键词**：过程奖励模型, 图像思维推理, 大型视觉语言模型, 基准评估, 视觉推理错误, 细粒度标注

## 3 点简述
- 核心问题：图像思维推理范式缺乏专门的过程奖励模型基准，现有基准以文本为中心，无法全面评估视觉推理错误。
- 方法要点：通过分析推理轨迹和引导搜索实验，定义7种细粒度错误类型，并构建包含1,206条手动标注轨迹的基准。
- 实验或效果：实验显示当前LVLMs作为过程奖励模型能力有限，存在性能差异、正向评估偏差和对步骤位置敏感等问题。

## 摘要（原文）

> The rapid advancement of Large Vision Language Models (LVLMs) has demonstrated excellent abilities in various visual tasks. Building upon these developments, the thinking with images paradigm has emerged, enabling models to dynamically edit and re-encode visual information at each reasoning step, mirroring human visual processing. However, this paradigm introduces significant challenges as diverse errors may occur during reasoning processes. This necessitates Process Reward Models (PRMs) for distinguishing positive and negative reasoning steps, yet existing benchmarks for PRMs are predominantly text-centric and lack comprehensive assessment under this paradigm. To address these gaps, this work introduces the first comprehensive benchmark specifically designed for evaluating PRMs under the thinking with images paradigm. Our main contributions are: (1) Through extensive analysis of reasoning trajectories and guided search experiments with PRMs, we define 7 fine-grained error types and demonstrate both the necessity for specialized PRMs and the potential for improvement. (2) We construct a comprehensive benchmark comprising 1,206 manually annotated thinking with images reasoning trajectories spanning 4 categories and 16 subcategories for fine-grained evaluation of PRMs. (3) Our experimental analysis reveals that current LVLMs fall short as effective PRMs, exhibiting limited capabilities in visual reasoning process evaluation with significant performance disparities across error types, positive evaluation bias, and sensitivity to reasoning step positions. These findings demonstrate the effectiveness of our benchmark and establish crucial foundations for advancing PRMs in LVLMs.

