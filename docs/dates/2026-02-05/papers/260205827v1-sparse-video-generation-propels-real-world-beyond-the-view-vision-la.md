---
layout: default
title: Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation
---

# Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation
**arXiv**：[2602.05827v1](https://arxiv.org/abs/2602.05827) · [PDF](https://arxiv.org/pdf/2602.05827.pdf)  
**作者**：Hai Zhang, Siqi Liang, Li Chen, Yuxian Li, Yukuan Xu, Yichao Zhong, Fu Zhang, Hongyang Li  

**一句话要点**：提出SparseVideoNav，利用稀疏视频生成实现超越视野的视觉语言导航

**关键词**：超越视野导航, 稀疏视频生成, 视觉语言导航, 长时程监督, 零样本学习, 实时推理

## 3 点简述
- 核心问题：超越视野导航需在稀疏高层意图下定位未见过目标，现有LLM方法因短视监督而受限
- 方法要点：首次引入视频生成模型，通过生成稀疏未来轨迹实现长时程监督，优化后推理速度提升27倍
- 实验或效果：零样本实验中，在BVN任务上成功率比SOTA LLM基线高2.5倍，首次实现夜间场景导航

## 摘要（原文）

> Why must vision-language navigation be bound to detailed and verbose language instructions? While such details ease decision-making, they fundamentally contradict the goal for navigation in the real-world. Ideally, agents should possess the autonomy to navigate in unknown environments guided solely by simple and high-level intents. Realizing this ambition introduces a formidable challenge: Beyond-the-View Navigation (BVN), where agents must locate distant, unseen targets without dense and step-by-step guidance. Existing large language model (LLM)-based methods, though adept at following dense instructions, often suffer from short-sighted behaviors due to their reliance on short-horimzon supervision. Simply extending the supervision horizon, however, destabilizes LLM training. In this work, we identify that video generation models inherently benefit from long-horizon supervision to align with language instructions, rendering them uniquely suitable for BVN tasks. Capitalizing on this insight, we propose introducing the video generation model into this field for the first time. Yet, the prohibitive latency for generating videos spanning tens of seconds makes real-world deployment impractical. To bridge this gap, we propose SparseVideoNav, achieving sub-second trajectory inference guided by a generated sparse future spanning a 20-second horizon. This yields a remarkable 27x speed-up compared to the unoptimized counterpart. Extensive real-world zero-shot experiments demonstrate that SparseVideoNav achieves 2.5x the success rate of state-of-the-art LLM baselines on BVN tasks and marks the first realization of such capability in challenging night scenes.

