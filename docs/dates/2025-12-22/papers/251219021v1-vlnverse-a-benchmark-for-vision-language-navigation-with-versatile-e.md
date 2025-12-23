---
layout: default
title: VLNVerse: A Benchmark for Vision-Language Navigation with Versatile, Embodied, Realistic Simulation and Evaluation
---

# VLNVerse: A Benchmark for Vision-Language Navigation with Versatile, Embodied, Realistic Simulation and Evaluation
**arXiv**：[2512.19021v1](https://arxiv.org/abs/2512.19021) · [PDF](https://arxiv.org/pdf/2512.19021.pdf)  
**作者**：Sihao Lin, Zerui Li, Xunyi Zhao, Gengze Zhou, Liuyi Wang, Rong Wei, Rui Tang, Juncheng Li, Hanqing Wang, Jiangmiao Pang, Anton van den Hengel, Jiajun Liu, Qi Wu  

**一句话要点**：提出VLNVerse基准，以解决视觉语言导航中数据集固定、模拟简单和任务碎片化的问题。

**关键词**：视觉语言导航, 基准测试, 物理模拟, 多任务学习, 模拟到真实泛化

## 3 点简述
- 核心问题：现有VLN基准数据集规模小、物理模拟简单，限制了对模拟到真实泛化的洞察，且任务碎片化阻碍统一进展。
- 方法要点：VLNVerse提供大规模、可扩展的基准，统一碎片化任务，支持全运动学、基于物理引擎的逼真模拟。
- 实验或效果：利用VLNVerse的规模和多样性，全面评估从经典模型到MLLM代理的方法，并提出统一多任务模型。

## 摘要（原文）

> Despite remarkable progress in Vision-Language Navigation (VLN), existing benchmarks remain confined to fixed, small-scale datasets with naive physical simulation. These shortcomings limit the insight that the benchmarks provide into sim-to-real generalization, and create a significant research gap. Furthermore, task fragmentation prevents unified/shared progress in the area, while limited data scales fail to meet the demands of modern LLM-based pretraining. To overcome these limitations, we introduce VLNVerse: a new large-scale, extensible benchmark designed for Versatile, Embodied, Realistic Simulation, and Evaluation. VLNVerse redefines VLN as a scalable, full-stack embodied AI problem. Its Versatile nature unifies previously fragmented tasks into a single framework and provides an extensible toolkit for researchers. Its Embodied design moves beyond intangible and teleporting "ghost" agents that support full-kinematics in a Realistic Simulation powered by a robust physics engine. We leverage the scale and diversity of VLNVerse to conduct a comprehensive Evaluation of existing methods, from classic models to MLLM-based agents. We also propose a novel unified multi-task model capable of addressing all tasks within the benchmark. VLNVerse aims to narrow the gap between simulated navigation and real-world generalization, providing the community with a vital tool to boost research towards scalable, general-purpose embodied locomotion agents.

