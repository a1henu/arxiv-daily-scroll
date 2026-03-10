---
layout: default
title: R2F: Repurposing Ray Frontiers for LLM-free Object Navigation
---

# R2F: Repurposing Ray Frontiers for LLM-free Object Navigation
**arXiv**：[2603.08475v1](https://arxiv.org/abs/2603.08475) · [PDF](https://arxiv.org/pdf/2603.08475.pdf)  
**作者**：Francesco Argenziano, John Mark Alexis Marcelo, Michele Brienza, Abdel Hakim Drid, Emanuele Musumeci, Daniele Nardi, Domenico D. Bloisi, Vincenzo Suriani  

**一句话要点**：提出R2F框架，利用射线前沿实现无大语言模型的室内开放词汇物体导航

**关键词**：物体导航, 射线前沿, 零样本学习, 实时系统, 语义映射, 机器人规划

## 3 点简述
- 核心问题：基于大模型的导航系统存在推理延迟和计算开销，限制实时部署。
- 方法要点：重新解释射线前沿为方向条件语义假设，通过嵌入评分和规划消除迭代大模型查询。
- 实验或效果：在模拟和真实机器人平台上实现竞争性零样本性能，运行速度比基于大模型的方案快达6倍。

## 摘要（原文）

> Zero-shot open-vocabulary object navigation has progressed rapidly with the emergence of large Vision-Language Models (VLMs) and Large Language Models (LLMs), now widely used as high-level decision-makers instead of end-to-end policies. Although effective, such systems often rely on iterative large-model queries at inference time, introducing latency and computational overhead that limit real-time deployment. To address this problem, we repurpose ray frontiers (R2F), a recently proposed frontier-based exploration paradigm, to develop an LLM-free framework for indoor open-vocabulary object navigation. While ray frontiers were originally used to bias exploration using semantic cues carried along rays, we reinterpret frontier regions as explicit, direction-conditioned semantic hypotheses that serve as navigation goals. Language-aligned features accumulated along out-of-range rays are stored sparsely at frontiers, where each region maintains multiple directional embeddings encoding plausible unseen content. In this way, navigation then reduces to embedding-based frontier scoring and goal tracking within a classical mapping and planning pipeline, eliminating iterative large-model reasoning. We further introduce R2F-VLN, a lightweight extension for free-form language instructions using syntactic parsing and relational verification without additional VLM or LLM components. Experiments in Habitat-sim and on a real robotic platform demonstrate competitive state-of-the-art zero-shot performance with real-time execution, achieving up to 6 times faster runtime than VLM-based alternatives.

