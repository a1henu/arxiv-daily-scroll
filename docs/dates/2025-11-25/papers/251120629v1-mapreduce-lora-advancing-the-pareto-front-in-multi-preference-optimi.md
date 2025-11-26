---
layout: default
title: MapReduce LoRA: Advancing the Pareto Front in Multi-Preference Optimization for Generative Models
---

# MapReduce LoRA: Advancing the Pareto Front in Multi-Preference Optimization for Generative Models
**arXiv**：[2511.20629v1](https://arxiv.org/abs/2511.20629) · [PDF](https://arxiv.org/pdf/2511.20629.pdf)  
**作者**：Chieh-Yun Chen, Zhonghao Wang, Qi Chen, Zhifan Ye, Min Shi, Yue Zhao, Yinan Zhao, Hui Qu, Wei-An Lin, Yiru Shen, Ajinkya Kale, Irfan Essa, Humphrey Shi  

**一句话要点**：提出MapReduce LoRA与RaTE以解决生成模型多偏好优化中的对齐税问题

**关键词**：多偏好优化, LoRA专家训练, 奖励特定嵌入, 生成模型对齐, 强化学习反馈

## 3 点简述
- 多奖励联合优化常导致对齐税，改善一维却损害其他维度
- MapReduce LoRA并行训练偏好专家并迭代合并，RaTE学习奖励特定嵌入以灵活控制
- 实验在文本到图像、视频和语言任务中显著提升多项指标，设定新SOTA

## 摘要（原文）

> Reinforcement learning from human feedback (RLHF) with reward models has advanced alignment of generative models to human aesthetic and perceptual preferences. However, jointly optimizing multiple rewards often incurs an alignment tax, improving one dimension while degrading others. To address this, we introduce two complementary methods: MapReduce LoRA and Reward-aware Token Embedding (RaTE). MapReduce LoRA trains preference-specific LoRA experts in parallel and iteratively merges them to refine a shared base model; RaTE learns reward-specific token embeddings that compose at inference for flexible preference control. Experiments on Text-to-Image generation (Stable Diffusion 3.5 Medium and FLUX.1-dev) show improvements of 36.1%, 4.6%, and 55.7%, and 32.7%, 4.3%, and 67.1% on GenEval, PickScore, and OCR, respectively. On Text-to-Video generation (HunyuanVideo), visual and motion quality improve by 48.1% and 90.0%, respectively. On the language task, Helpful Assistant, with Llama-2 7B, helpful and harmless improve by 43.4% and 136.7%, respectively. Our framework sets a new state-of-the-art multi-preference alignment recipe across modalities.

