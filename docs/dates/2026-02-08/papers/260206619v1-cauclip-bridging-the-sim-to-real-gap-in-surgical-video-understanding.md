---
layout: default
title: CauCLIP: Bridging the Sim-to-Real Gap in Surgical Video Understanding via Causality-Inspired Vision-Language Modeling
---

# CauCLIP: Bridging the Sim-to-Real Gap in Surgical Video Understanding via Causality-Inspired Vision-Language Modeling
**arXiv**：[2602.06619v1](https://arxiv.org/abs/2602.06619) · [PDF](https://arxiv.org/pdf/2602.06619.pdf)  
**作者**：Yuxin He, An Li, Cheng Xue  

**一句话要点**：提出CauCLIP，通过因果启发的视觉语言建模解决手术视频理解中的模拟到真实域差距问题。

**关键词**：手术视频理解, 视觉语言建模, 域泛化, 因果学习, 模拟到真实适应

## 3 点简述
- 核心问题：手术阶段识别因标注临床视频有限和模拟与真实数据间大域差距而训练困难。
- 方法要点：结合频率增强和因果抑制损失，利用CLIP学习域不变表示，聚焦手术工作流的稳定因果因素。
- 实验或效果：在SurgVisDom硬适应基准上显著优于所有竞争方法，验证了因果引导模型的有效性。

## 摘要（原文）

> Surgical phase recognition is a critical component for context-aware decision support in intelligent operating rooms, yet training robust models is hindered by limited annotated clinical videos and large domain gaps between synthetic and real surgical data. To address this, we propose CauCLIP, a causality-inspired vision-language framework that leverages CLIP to learn domain-invariant representations for surgical phase recognition without access to target domain data. Our approach integrates a frequency-based augmentation strategy to perturb domain-specific attributes while preserving semantic structures, and a causal suppression loss that mitigates non-causal biases and reinforces causal surgical features. These components are combined in a unified training framework that enables the model to focus on stable causal factors underlying surgical workflows. Experiments on the SurgVisDom hard adaptation benchmark demonstrate that our method substantially outperforms all competing approaches, highlighting the effectiveness of causality-guided vision-language models for domain-generalizable surgical video understanding.

