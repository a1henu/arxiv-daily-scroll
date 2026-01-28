---
layout: default
title: m2sv: A Scalable Benchmark for Map-to-Street-View Spatial Reasoning
---

# m2sv: A Scalable Benchmark for Map-to-Street-View Spatial Reasoning
**arXiv**：[2601.19099v1](https://arxiv.org/abs/2601.19099) · [PDF](https://arxiv.org/pdf/2601.19099.pdf)  
**作者**：Yosub Shin, Michael Buriek, Igor Molybog  

**一句话要点**：提出m2sv基准以评估地图到街景的空间推理能力

**关键词**：地图到街景推理, 空间推理基准, 视觉语言模型评估, 几何对齐, 监督微调, 跨视角推理

## 3 点简述
- 核心问题：视觉语言模型在抽象地图与街景对齐的空间推理任务上表现脆弱
- 方法要点：构建地理多样、歧义可控的m2sv-20k基准及结构化推理轨迹集m2sv-sft-11k
- 实验或效果：最佳模型准确率65.2%，远低于人类基线95%，揭示几何对齐和推理一致性差距

## 摘要（原文）

> Vision--language models (VLMs) achieve strong performance on many multimodal benchmarks but remain brittle on spatial reasoning tasks that require aligning abstract overhead representations with egocentric views. We introduce m2sv, a scalable benchmark for map-to-street-view spatial reasoning that asks models to infer camera viewing direction by aligning a north-up overhead map with a Street View image captured at the same real-world intersection. We release m2sv-20k, a geographically diverse benchmark with controlled ambiguity, along with m2sv-sft-11k, a curated set of structured reasoning traces for supervised fine-tuning.
>   Despite strong performance on existing multimodal benchmarks, the best evaluated VLM achieves only 65.2% accuracy on m2sv, far below the human baseline of 95%. While supervised fine-tuning and reinforcement learning yield consistent gains, cross-benchmark evaluations reveal limited transfer. Beyond aggregate accuracy, we systematically analyze difficulty in map-to-street-view reasoning using both structural signals and human effort, and conduct an extensive failure analysis of adapted open models. Our findings highlight persistent gaps in geometric alignment, evidence aggregation, and reasoning consistency, motivating future work on grounded spatial reasoning across viewpoints.

