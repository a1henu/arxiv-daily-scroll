---
layout: default
title: VIDEOP2R: Video Understanding from Perception to Reasoning
---

# VIDEOP2R: Video Understanding from Perception to Reasoning
**arXiv**：[2511.11113v1](https://arxiv.org/abs/2511.11113) · [PDF](https://arxiv.org/pdf/2511.11113.pdf)  
**作者**：Yifan Jiang, Yueying Wang, Rui Zhao, Toufiq Parag, Zhimin Chen, Zhenyu Liao, Jayakrishnan Unnikrishnan  

**一句话要点**：提出VideoP2R框架，通过过程感知建模增强视频语言模型的推理能力。

**关键词**：视频语言模型, 强化微调, 过程感知建模, 链式思维数据集, 视频推理, 策略优化

## 3 点简述
- 核心问题：将强化微调扩展到大型视频语言模型存在挑战，需提升视频推理能力。
- 方法要点：采用两阶段框架，包括监督微调和过程感知分组相对策略优化算法。
- 实验或效果：在七个视频推理基准中，六个达到最优性能，验证过程感知有效性。

## 摘要（原文）

> Reinforcement fine-tuning (RFT), a two-stage framework consisting of supervised fine-tuning (SFT) and reinforcement learning (RL) has shown promising results on improving reasoning ability of large language models (LLMs). Yet extending RFT to large video language models (LVLMs) remains challenging. We propose VideoP2R, a novel process-aware video RFT framework that enhances video reasoning by modeling perception and reasoning as distinct processes. In the SFT stage, we develop a three-step pipeline to generate VideoP2R-CoT-162K, a high-quality, process-aware chain-of-thought (CoT) dataset for perception and reasoning. In the RL stage, we introduce a novel process-aware group relative policy optimization (PA-GRPO) algorithm that supplies separate rewards for perception and reasoning. Extensive experiments show that VideoP2R achieves state-of-the-art (SotA) performance on six out of seven video reasoning and understanding benchmarks. Ablation studies further confirm the effectiveness of our process-aware modeling and PA-GRPO and demonstrate that model's perception output is information-sufficient for downstream reasoning.

