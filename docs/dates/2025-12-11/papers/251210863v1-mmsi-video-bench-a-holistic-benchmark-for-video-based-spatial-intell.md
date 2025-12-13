---
layout: default
title: MMSI-Video-Bench: A Holistic Benchmark for Video-Based Spatial Intelligence
---

# MMSI-Video-Bench: A Holistic Benchmark for Video-Based Spatial Intelligence
**arXiv**：[2512.10863v1](https://arxiv.org/abs/2512.10863) · [PDF](https://arxiv.org/pdf/2512.10863.pdf)  
**作者**：Jingli Lin, Runsen Xu, Shaohao Zhu, Sihan Yang, Peizhou Cao, Yunlong Ran, Miao Hu, Chenming Zhu, Yiman Xie, Yilin Long, Wenbo Hu, Dahua Lin, Tai Wang, Jiangmiao Pang  

**一句话要点**：提出MMSI-Video-Bench基准，全面评估多模态大语言模型的视频空间智能能力。

**关键词**：视频空间智能, 多模态大语言模型, 基准评估, 几何推理, 跨视频推理, 人类标注

## 3 点简述
- 核心问题：缺乏全面评估视频空间智能的基准，阻碍MLLMs在物理环境中的发展。
- 方法要点：基于四层框架（感知、规划、预测、跨视频推理），构建包含1,106个问题的基准，数据来自25个数据集和内部视频。
- 实验或效果：评估25个模型，发现人类与AI差距显著，最佳模型落后人类近60%，并揭示模型在几何推理等任务上的系统性失败。

## 摘要（原文）

> Spatial understanding over continuous visual input is crucial for MLLMs to evolve into general-purpose assistants in physical environments. Yet there is still no comprehensive benchmark that holistically assesses the progress toward this goal. In this work, we introduce MMSI-Video-Bench, a fully human-annotated benchmark for video-based spatial intelligence in MLLMs. It operationalizes a four-level framework, Perception, Planning, Prediction, and Cross-Video Reasoning, through 1,106 questions grounded in 1,278 clips from 25 datasets and in-house videos. Each item is carefully designed and reviewed by 3DV experts with explanatory rationales to ensure precise, unambiguous grounding. Leveraging its diverse data sources and holistic task coverage, MMSI-Video-Bench also supports three domain-oriented sub-benchmarks (Indoor Scene Perception Bench, Robot Bench and Grounding Bench) for targeted capability assessment. We evaluate 25 strong open-source and proprietary MLLMs, revealing a striking human--AI gap: many models perform near chance, and the best reasoning model lags humans by nearly 60%. We further find that spatially fine-tuned models still fail to generalize effectively on our benchmark. Fine-grained error analysis exposes systematic failures in geometric reasoning, motion grounding, long-horizon prediction, and cross-video correspondence. We also show that typical frame-sampling strategies transfer poorly to our reasoning-intensive benchmark, and that neither 3D spatial cues nor chain-of-thought prompting yields meaningful gains. We expect our benchmark to establish a solid testbed for advancing video-based spatial intelligence.

