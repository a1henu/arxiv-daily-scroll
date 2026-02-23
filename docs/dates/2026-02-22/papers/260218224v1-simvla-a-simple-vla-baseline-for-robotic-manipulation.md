---
layout: default
title: SimVLA: A Simple VLA Baseline for Robotic Manipulation
---

# SimVLA: A Simple VLA Baseline for Robotic Manipulation
**arXiv**：[2602.18224v1](https://arxiv.org/abs/2602.18224) · [PDF](https://arxiv.org/pdf/2602.18224.pdf)  
**作者**：Yuankai Luo, Woping Chen, Tong Liang, Baiqiao Wang, Zhenguo Li  

**一句话要点**：提出SimVLA作为机器人操作的简单VLA基线，以透明化性能增益来源

**关键词**：视觉-语言-动作模型, 机器人操作, 基线模型, 标准化训练, 轻量架构, 仿真基准

## 3 点简述
- VLA模型在机器人操作中性能提升来源不明确，因训练方法和实现细节多样
- SimVLA通过解耦感知与控制、使用标准骨干和轻量动作头，建立最小化设计
- 在仿真基准上超越多参数模型，无需机器人预训练，实机性能与pi0.5相当

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation, leveraging large-scale pre-training to achieve strong performance. The field has rapidly evolved with additional spatial priors and diverse architectural innovations. However, these advancements are often accompanied by varying training recipes and implementation details, which can make it challenging to disentangle the precise source of empirical gains. In this work, we introduce SimVLA, a streamlined baseline designed to establish a transparent reference point for VLA research. By strictly decoupling perception from control, using a standard vision-language backbone and a lightweight action head, and standardizing critical training dynamics, we demonstrate that a minimal design can achieve state-of-the-art performance. Despite having only 0.5B parameters, SimVLA outperforms multi-billion-parameter models on standard simulation benchmarks without robot pretraining. SimVLA also reaches on-par real-robot performance compared to pi0.5. Our results establish SimVLA as a robust, reproducible baseline that enables clear attribution of empirical gains to future architectural innovations. Website: https://frontierrobo.github.io/SimVLA

