---
layout: default
title: 3D-RFT: Reinforcement Fine-Tuning for Video-based 3D Scene Understanding
---

# 3D-RFT: Reinforcement Fine-Tuning for Video-based 3D Scene Understanding
**arXiv**：[2603.04976v1](https://arxiv.org/abs/2603.04976) · [PDF](https://arxiv.org/pdf/2603.04976.pdf)  
**作者**：Xiongkun Linghu, Jiangyong Huang, Baoxiong Jia, Siyuan Huang  

**一句话要点**：提出3D-RFT框架，通过强化微调优化视频3D场景理解任务性能。

**关键词**：视频3D场景理解, 强化微调, 多模态大语言模型, 3D感知, 策略优化

## 3 点简述
- 现有方法依赖监督微调，训练目标与任务性能存在偏差。
- 3D-RFT结合监督微调与强化微调，直接基于评估指标优化模型。
- 实验显示3D-RFT-4B在多项任务上超越更大模型，达到先进水平。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards ( RLVR ) has emerged as a transformative paradigm for enhancing the reasoning capabilities of Large Language Models ( LLMs), yet its potential in 3D scene understanding remains under-explored. Existing approaches largely rely on Supervised Fine-Tuning ( SFT), where the token-level cross-entropy loss acts as an indirect proxy for optimization, leading to a misalignment between training objectives and task performances. To bridge this gap, we present Reinforcement Fine-Tuning for Video-based 3D Scene Understanding (3D-RFT ), the first framework to extend RLVR to video-based 3D perception and reasoning. 3D-RFT shifts the paradigm by directly optimizing the model towards evaluation metrics. 3D-RFT first activates 3D-aware Multi-modal Large Language Models ( MLLM s) via SFT, followed by reinforcement fine-tuning using Group Relative Policy Optimization ( GRPO) with strictly verifiable reward functions. We design task-specific reward functions directly from metrics like 3D IoU and F1-Score to provide more effective signals to guide model training. Extensive experiments demonstrate that 3D-RFT-4B achieves state-of-the-art performance on various video-based 3D scene understanding tasks. Notably, 3D-RFT-4B significantly outperforms larger models (e.g., VG LLM-8B) on 3D video detection, 3D visual grounding, and spatial reasoning benchmarks. We further reveal good properties of 3D-RFT such as robust efficacy, and valuable insights into training strategies and data impact. We hope 3D-RFT can serve as a robust and promising paradigm for future development of 3D scene understanding.

