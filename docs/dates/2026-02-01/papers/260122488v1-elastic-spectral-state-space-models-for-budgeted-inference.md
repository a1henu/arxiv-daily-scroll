---
layout: default
title: Elastic Spectral State Space Models for Budgeted Inference
---

# Elastic Spectral State Space Models for Budgeted Inference
**arXiv**：[2601.22488v1](https://arxiv.org/abs/2601.22488) · [PDF](https://arxiv.org/pdf/2601.22488.pdf)  
**作者**：Dachuan Song, Xuan Wang  

**一句话要点**：提出弹性谱状态空间模型，通过一次训练支持运行时任意尺度截断以适应预算推理

**关键词**：弹性谱状态空间模型, 预算推理, 长序列处理, 一次训练多尺度部署, 谱滤波, 输入自适应门

## 3 点简述
- 核心问题：基础模型训练固定，部署需适应不同资源约束，现有方法需额外训练且不支持细粒度运行时调整
- 方法要点：基于Hankel谱滤波和状态空间模型，结合轻量输入自适应门和共享掩码归一化，使预测能力集中于低索引分量
- 实验或效果：在文本、逻辑、检索、视觉和音频长序列基准测试中，单模型截断后性能与Transformer和SSM基线竞争，预算-性能曲线平滑稳定

## 摘要（原文）

> Foundation models are typically trained at a fixed computational capacity, while real-world applications require deployment across platforms with different resource constraints. Current approaches usually rely on training families of model variants or model distillation, which requires additional training and supports only a pre-selected set of sizes rather than fine-grained adaptation at runtime. In this paper, we propose Elastic Spectral State Space Models (ES-SSM), which require only one-time training at full capacity, but can be directly truncated into arbitrary scales for budgeted, runtime inference without retraining. Our ES-SSM builds on Hankel spectral filtering over a state space model (SSM), coupled with a lightweight input-adaptive gate trained under randomized spectral budgets. Using a shared masked normalization rule over the ordered spectral channels, we encourage predictive capability to concentrate in low-index components, while higher-index components act primarily as refinement. We test our algorithm across long-sequence benchmarks spanning text, logic, retrieval, vision, and audio. We demonstrate that a single ES-SSM model trained once can be truncated to provide competitive performance compared with modern Transformer and SSM baselines at similar parameter scales. Furthermore, by testing under various runtime budgets, we observe smooth and stable budget-performance curves over a wide range of truncation levels.

