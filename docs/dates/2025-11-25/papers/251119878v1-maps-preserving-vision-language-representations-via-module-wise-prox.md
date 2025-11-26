---
layout: default
title: MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization
---

# MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization
**arXiv**：[2511.19878v1](https://arxiv.org/abs/2511.19878) · [PDF](https://arxiv.org/pdf/2511.19878.pdf)  
**作者**：Chengyue Huang, Mellon M. Zhang, Robert Azarcon, Glen Chou, Zsolt Kira  

**一句话要点**：提出模块邻近调度以在视觉-语言-动作模型中保留预训练表示并提升泛化能力

**关键词**：视觉-语言-动作模型, 微调框架, 模块邻近调度, 泛化能力, 预训练表示保留

## 3 点简述
- 核心问题：视觉-语言-动作模型微调易破坏预训练表示，损害泛化能力
- 方法要点：通过模块邻近调度线性放松约束，平衡稳定性和灵活性
- 实验或效果：在多个基准和真实平台上提升性能，最高达30%

## 摘要（原文）

> Vision-Language-Action (VLA) models inherit strong priors from pretrained Vision-Language Models (VLMs), but naive fine-tuning often disrupts these representations and harms generalization. Existing fixes -- freezing modules or applying uniform regularization -- either overconstrain adaptation or ignore the differing roles of VLA components. We present MAPS (Module-Wise Proximity Scheduling), the first robust fine-tuning framework for VLAs. Through systematic analysis, we uncover an empirical order in which proximity constraints should be relaxed to balance stability and flexibility. MAPS linearly schedules this relaxation, enabling visual encoders to stay close to their pretrained priors while action-oriented language layers adapt more freely. MAPS introduces no additional parameters or data, and can be seamlessly integrated into existing VLAs. Across MiniVLA-VQ, MiniVLA-OFT, OpenVLA-OFT, and challenging benchmarks such as SimplerEnv, CALVIN, LIBERO, as well as real-world evaluations on the Franka Emika Panda platform, MAPS consistently boosts both in-distribution and out-of-distribution performance (up to +30%). Our findings highlight empirically guided proximity to pretrained VLMs as a simple yet powerful principle for preserving broad generalization in VLM-to-VLA transfer.

