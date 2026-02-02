---
layout: default
title: Best-of-Q: Improving VLM agents with Q-function Action Ranking at Inference
---

# Best-of-Q: Improving VLM agents with Q-function Action Ranking at Inference
**arXiv**：[2601.22701v1](https://arxiv.org/abs/2601.22701) · [PDF](https://arxiv.org/pdf/2601.22701.pdf)  
**作者**：Emilien Biré, María Santos, Kai Yuan  

**一句话要点**：提出Best-of-Q方法，通过Q函数在推理时重排动作以提升视觉语言模型代理在数字环境中的性能

**关键词**：视觉语言模型代理, Q函数重排, 推理时优化, 数字环境操作, 离线训练

## 3 点简述
- 核心问题：视觉语言模型代理在快速变化环境（如网页）中适应性差，微调需大量训练和数据收集
- 方法要点：冻结VLM策略生成候选动作，用离线训练的轻量Q函数重排，选择最高价值动作执行
- 实验或效果：在WebVoyager基准上，显著提升代理成功率，如Qwen2.5-VL-7B从38.8%提高到55.7%

## 摘要（原文）

> Vision-Language Models (VLMs) have become powerful backbones for agents to autonomously operate in digital environments like the web and operating systems. However, these models suffer from inadaptability to fast-changing environments like the web, which can be alleviated by fine-tuning requiring expansive model training and data collection. In this work, we introduce a novel paradigm for enhancing agentic VLM policies at inference without policy retraining. Fundamentally, our approach decouples the VLM's role as a high-capacity action proposer from the final action selection mechanism. We keep the VLM policy frozen and use it to generate a set of candidate actions for a given state. Then, a lightweight, offline-trained Q-function reranks these candidates, and the agent executes the action with the highest estimated value. The main contribution is to apply the Q-function directly during inference for immediate policy improvement, and not offline to relabel data for policy retraining. We demonstrate on the academic WebVoyager benchmark that our method significantly boosts agent success rates, improving a Qwen2.5-VL-7B agent from 38.8% to 55.7% and a proprietary GPT-4.1 agent from 82.4% to 88.8%.

