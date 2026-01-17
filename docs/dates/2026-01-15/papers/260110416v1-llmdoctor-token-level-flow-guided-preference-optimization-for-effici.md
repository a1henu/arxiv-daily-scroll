---
layout: default
title: LLMdoctor: Token-Level Flow-Guided Preference Optimization for Efficient Test-Time Alignment of Large Language Models
---

# LLMdoctor: Token-Level Flow-Guided Preference Optimization for Efficient Test-Time Alignment of Large Language Models
**arXiv**：[2601.10416v1](https://arxiv.org/abs/2601.10416) · [PDF](https://arxiv.org/pdf/2601.10416.pdf)  
**作者**：Tiesunlong Shen, Rui Mao, Jin Wang, Heming Sun, Jian Zhang, Xuejie Zhang, Erik Cambria  

**一句话要点**：提出LLMdoctor框架，通过细粒度令牌级流引导偏好优化实现高效测试时对齐大型语言模型

**关键词**：大型语言模型对齐, 测试时对齐, 令牌级优化, 流引导偏好优化, 患者-医生范式

## 3 点简述
- 核心问题：传统对齐方法计算成本高且不灵活，现有测试时对齐方法依赖扭曲轨迹级信号或低效采样，限制性能并损害生成多样性。
- 方法要点：采用患者-医生范式，从患者模型提取令牌级偏好信号，通过令牌级流引导偏好优化训练医生模型，实现精确令牌级对齐并保持多样性。
- 实验或效果：实验显示LLMdoctor显著优于现有测试时对齐方法，甚至超越DPO等全微调方法。

## 摘要（原文）

> Aligning Large Language Models (LLMs) with human preferences is critical, yet traditional fine-tuning methods are computationally expensive and inflexible. While test-time alignment offers a promising alternative, existing approaches often rely on distorted trajectory-level signals or inefficient sampling, fundamentally capping performance and failing to preserve the generative diversity of the base model. This paper introduces LLMdoctor, a novel framework for efficient test-time alignment that operates via a patient-doctor paradigm. It integrates token-level reward acquisition with token-level flow-guided preference optimization (TFPO) to steer a large, frozen patient LLM with a smaller, specialized doctor model. Unlike conventional methods that rely on trajectory-level rewards, LLMdoctor first extracts fine-grained, token-level preference signals from the patient model's behavioral variations. These signals then guide the training of the doctor model via TFPO, which establishes flow consistency across all subtrajectories, enabling precise token-by-token alignment while inherently preserving generation diversity. Extensive experiments demonstrate that LLMdoctor significantly outperforms existing test-time alignment methods and even surpasses the performance of full fine-tuning approaches like DPO.

