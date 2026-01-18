---
layout: default
title: V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation
---

# V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation
**arXiv**：[2601.10094v1](https://arxiv.org/abs/2601.10094) · [PDF](https://arxiv.org/pdf/2601.10094.pdf)  
**作者**：Han Wang, Yi Yang, Jingyuan Hu, Minfeng Zhu, Wei Chen  

**一句话要点**：提出V-Zero框架，通过无标注图像实现多模态推理的自改进

**关键词**：多模态推理, 自改进学习, 无监督训练, 视觉语言模型, 协同进化

## 3 点简述
- 核心问题：现有多模态学习依赖大规模人工标注，成本高且耗时。
- 方法要点：建立问答者与求解者协同进化循环，利用双轨推理奖励和多数投票伪标签进行迭代优化。
- 实验或效果：在Qwen2.5-VL-7B-Instruct上，无需人工标注，视觉数学推理提升+1.7，通用视觉中心任务提升+2.6。

## 摘要（原文）

> Recent advances in multimodal learning have significantly enhanced the reasoning capabilities of vision-language models (VLMs). However, state-of-the-art approaches rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire. To overcome this limitation, we introduce V-Zero, a general post-training framework that facilitates self-improvement using exclusively unlabeled images. V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver. The Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses. Both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement. Remarkably, without a single human annotation, V-Zero achieves consistent performance gains on Qwen2.5-VL-7B-Instruct, improving visual mathematical reasoning by +1.7 and general vision-centric by +2.6, demonstrating the potential of self-improvement in multimodal systems. Code is available at https://github.com/SatonoDia/V-Zero

