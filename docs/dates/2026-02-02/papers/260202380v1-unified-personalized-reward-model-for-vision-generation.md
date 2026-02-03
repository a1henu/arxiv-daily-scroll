---
layout: default
title: Unified Personalized Reward Model for Vision Generation
---

# Unified Personalized Reward Model for Vision Generation
**arXiv**：[2602.02380v1](https://arxiv.org/abs/2602.02380) · [PDF](https://arxiv.org/pdf/2602.02380.pdf)  
**作者**：Yibin Wang, Yuhang Zang, Feng Han, Jiazi Bu, Yujie Zhou, Cheng Jin, Jiaqi Wang  

**一句话要点**：提出统一个性化奖励模型UnifiedReward-Flex，通过灵活上下文自适应推理解决视觉生成中偏好对齐不足的问题。

**关键词**：个性化奖励模型, 视觉生成, 上下文自适应推理, 直接偏好优化, 分层评估, 蒸馏训练

## 3 点简述
- 现有奖励模型采用通用偏好假设或固定评估标准，导致与主观、上下文相关的人类偏好系统性错位。
- 模型结合奖励建模与灵活推理，基于语义意图和视觉证据动态构建分层评估，包括预定义和自生成维度。
- 采用两阶段训练：先蒸馏闭源VLM推理轨迹进行SFT，再通过DPO优化偏好对，集成GRPO框架在图像和视频合成中验证优越性。

## 摘要（原文）

> Recent advancements in multimodal reward models (RMs) have significantly propelled the development of visual generation. Existing frameworks typically adopt Bradley-Terry-style preference modeling or leverage generative VLMs as judges, and subsequently optimize visual generation models via reinforcement learning. However, current RMs suffer from inherent limitations: they often follow a one-size-fits-all paradigm that assumes a monolithic preference distribution or relies on fixed evaluation rubrics. As a result, they are insensitive to content-specific visual cues, leading to systematic misalignment with subjective and context-dependent human preferences. To this end, inspired by human assessment, we propose UnifiedReward-Flex, a unified personalized reward model for vision generation that couples reward modeling with flexible and context-adaptive reasoning. Specifically, given a prompt and the generated visual content, it first interprets the semantic intent and grounds on visual evidence, then dynamically constructs a hierarchical assessment by instantiating fine-grained criteria under both predefined and self-generated high-level dimensions. Our training pipeline follows a two-stage process: (1) we first distill structured, high-quality reasoning traces from advanced closed-source VLMs to bootstrap SFT, equipping the model with flexible and context-adaptive reasoning behaviors; (2) we then perform direct preference optimization (DPO) on carefully curated preference pairs to further strengthen reasoning fidelity and discriminative alignment. To validate the effectiveness, we integrate UnifiedReward-Flex into the GRPO framework for image and video synthesis, and extensive results demonstrate its superiority.

