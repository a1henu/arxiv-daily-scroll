---
layout: default
title: Towards Continuous Intelligence Growth: Self-Training, Continual Learning, and Dual-Scale Memory in SuperIntelliAgent
---

# Towards Continuous Intelligence Growth: Self-Training, Continual Learning, and Dual-Scale Memory in SuperIntelliAgent
**arXiv**：[2511.23436v1](https://arxiv.org/abs/2511.23436) · [PDF](https://arxiv.org/pdf/2511.23436.pdf)  
**作者**：Jianzhe Lin, Zeyu Pan, Yun Zhu, Ruiqi Song, Jining Yang  

**一句话要点**：提出SuperIntelliAgent框架，通过自训练与双尺度记忆实现持续智能增长

**关键词**：持续学习, 自训练, 双尺度记忆, 直接偏好优化, 智能体框架

## 3 点简述
- 核心问题：传统监督微调依赖标注，难以实现持续智能增长
- 方法要点：结合可训练扩散模型与冻结大语言模型，通过自监督交互生成DPO对进行优化
- 实验或效果：少量自动生成DPO对即可提升基准测试性能，表明机制有效

## 摘要（原文）

> We introduce SuperIntelliAgent, an agentic learning framework that couples a trainable small diffusion model (the learner) with a frozen large language model (the verifier) to enable continual intelligence growth through self-supervised interaction. Unlike conventional supervised fine-tuning, SuperIntelliAgent learns autonomously without annotation: the learner generates candidate outputs, the verifier evaluates them through step-by-step reasoning, and their interaction produces chosen/rejected pairs for Direct Preference Optimization (DPO). This converts each input into a pseudo-training signal for continual improvement. The framework integrates dual-scale memory: short-term in-context memory that preserves reasoning traces across refinement cycles, and long-term memory that consolidates acquired knowledge through lightweight on-the-fly fine-tuning. A replay buffer retains samples that show verifiable progress and replays them as auxiliary supervision, reinforcing recent learning while forming adaptive curricula. SuperIntelliAgent is infrastructure-agnostic and can be plugged into existing agentic frameworks while turning ordinary inference loops into a lifelong optimization process. We posit that pairing a trainable learner with a reasoning-capable verifier forms a minimal reliable unit of growing intelligence, as paired feedback and partial-history replay yield richer learning curricula and stronger preference alignment. With a small number of automatically generated DPO pairs, the learner improves across all benchmarks, indicating that this mechanism provides a promising direction for continual intelligence accumulation and real-world deployment.

