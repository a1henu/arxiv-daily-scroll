---
layout: default
title: Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding
---

# Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding
**arXiv**：[2512.17532v1](https://arxiv.org/abs/2512.17532) · [PDF](https://arxiv.org/pdf/2512.17532.pdf)  
**作者**：Jiaqi Tang, Jianmin Chen, Wei Wei, Xiaogang Xu, Runtao Liu, Xiangyu Wu, Qipeng Xie, Jiafei Wu, Lei Zhang, Qifeng Chen  

**一句话要点**：提出Robust-R1框架，通过结构化推理链显式建模视觉退化，以提升多模态大语言模型在极端现实世界视觉退化下的鲁棒性。

**关键词**：视觉退化建模, 结构化推理链, 多模态大语言模型, 鲁棒性增强, 现实世界视觉处理

## 3 点简述
- 核心问题：多模态大语言模型在极端现实世界视觉退化下性能不可靠，现有方法依赖隐式训练，缺乏可解释性和孤立优化。
- 方法要点：集成监督微调、奖励驱动对齐和动态推理深度缩放，构建退化感知推理链。
- 实验或效果：在R-Bench等基准测试中实现最先进鲁棒性，优于所有通用和鲁棒基线。

## 摘要（原文）

> Multimodal Large Language Models struggle to maintain reliable performance under extreme real-world visual degradations, which impede their practical robustness. Existing robust MLLMs predominantly rely on implicit training/adaptation that focuses solely on visual encoder generalization, suffering from limited interpretability and isolated optimization. To overcome these limitations, we propose Robust-R1, a novel framework that explicitly models visual degradations through structured reasoning chains. Our approach integrates: (i) supervised fine-tuning for degradation-aware reasoning foundations, (ii) reward-driven alignment for accurately perceiving degradation parameters, and (iii) dynamic reasoning depth scaling adapted to degradation intensity. To facilitate this approach, we introduce a specialized 11K dataset featuring realistic degradations synthesized across four critical real-world visual processing stages, each annotated with structured chains connecting degradation parameters, perceptual influence, pristine semantic reasoning chain, and conclusion. Comprehensive evaluations demonstrate state-of-the-art robustness: Robust-R1 outperforms all general and robust baselines on the real-world degradation benchmark R-Bench, while maintaining superior anti-degradation performance under multi-intensity adversarial degradations on MMMB, MMStar, and RealWorldQA.

