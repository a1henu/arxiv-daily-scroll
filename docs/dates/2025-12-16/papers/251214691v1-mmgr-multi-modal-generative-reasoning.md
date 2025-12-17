---
layout: default
title: MMGR: Multi-Modal Generative Reasoning
---

# MMGR: Multi-Modal Generative Reasoning
**arXiv**：[2512.14691v1](https://arxiv.org/abs/2512.14691) · [PDF](https://arxiv.org/pdf/2512.14691.pdf)  
**作者**：Zefan Cai, Haoyi Qiu, Tianyi Ma, Haozhe Zhao, Gengze Zhou, Kung-Hsiang Huang, Parisa Kordjamshidi, Minjia Zhang, Xiao Wen, Jiuxiang Gu, Nanyun Peng, Junjie Hu  

**一句话要点**：提出MMGR多模态生成推理评估框架，以解决视频基础模型在物理、逻辑和空间约束上的推理失败问题。

**关键词**：多模态生成推理, 视频基础模型评估, 物理逻辑约束, 抽象推理基准, 具身导航, 全局一致性

## 3 点简述
- 现有视频生成模型评估指标如FVD忽视推理能力，导致模型违反因果、物理和全局一致性约束。
- MMGR基于物理、逻辑、3D空间、2D空间和时间五种推理能力，构建统一评估框架，涵盖抽象推理、具身导航和物理常识三个领域。
- 基准测试显示模型在抽象推理和长程空间规划上表现差，MMGR为推理感知生成模型提供诊断路径。

## 摘要（原文）

> Video foundation models generate visually realistic and temporally coherent content, but their reliability as world simulators depends on whether they capture physical, logical, and spatial constraints. Existing metrics such as Frechet Video Distance (FVD) emphasize perceptual quality and overlook reasoning failures, including violations of causality, physics, and global consistency. We introduce MMGR (Multi-Modal Generative Reasoning Evaluation and Benchmark), a principled evaluation framework based on five reasoning abilities: Physical, Logical, 3D Spatial, 2D Spatial, and Temporal. MMGR evaluates generative reasoning across three domains: Abstract Reasoning (ARC-AGI, Sudoku), Embodied Navigation (real-world 3D navigation and localization), and Physical Commonsense (sports and compositional interactions). MMGR applies fine-grained metrics that require holistic correctness across both video and image generation. We benchmark leading video models (Veo-3, Sora-2, Wan-2.2) and image models (Nano-banana, Nano-banana Pro, GPT-4o-image, Qwen-image), revealing strong performance gaps across domains. Models show moderate success on Physical Commonsense tasks but perform poorly on Abstract Reasoning (below 10 percent accuracy on ARC-AGI) and struggle with long-horizon spatial planning in embodied settings. Our analysis highlights key limitations in current models, including overreliance on perceptual data, weak global state consistency, and objectives that reward visual plausibility over causal correctness. MMGR offers a unified diagnostic benchmark and a path toward reasoning-aware generative world models.

