---
layout: default
title: Reinforced Attention Learning
---

# Reinforced Attention Learning
**arXiv**：[2602.04884v1](https://arxiv.org/abs/2602.04884) · [PDF](https://arxiv.org/pdf/2602.04884.pdf)  
**作者**：Bangzheng Li, Jianmo Ni, Chen Qu, Ian Miao, Liu Yang, Xingyu Fu, Muhao Chen, Derek Zhiyuan Cheng  

**一句话要点**：提出强化注意力学习以优化多模态大语言模型中的注意力分布

**关键词**：多模态大语言模型, 强化学习, 注意力机制, 策略梯度, 跨模态对齐, 注意力蒸馏

## 3 点简述
- 核心问题：传统强化学习后训练在多模态大语言模型中通过冗长推理提升感知能力有限，甚至可能降低性能。
- 方法要点：采用策略梯度框架直接优化内部注意力分布，而非输出序列，促进信息有效分配和跨模态对齐。
- 实验或效果：在多种图像和视频基准测试中表现优于GRPO等基线，并引入在线策略注意力蒸馏提升跨模态对齐效果。

## 摘要（原文）

> Post-training with Reinforcement Learning (RL) has substantially improved reasoning in Large Language Models (LLMs) via test-time scaling. However, extending this paradigm to Multimodal LLMs (MLLMs) through verbose rationales yields limited gains for perception and can even degrade performance.
>   We propose Reinforced Attention Learning (RAL), a policy-gradient framework that directly optimizes internal attention distributions rather than output token sequences. By shifting optimization from what to generate to where to attend, RAL promotes effective information allocation and improved grounding in complex multimodal inputs. Experiments across diverse image and video benchmarks show consistent gains over GRPO and other baselines. We further introduce On-Policy Attention Distillation, demonstrating that transferring latent attention behaviors yields stronger cross-modal alignment than standard knowledge distillation. Our results position attention policies as a principled and general alternative for multimodal post-training.

