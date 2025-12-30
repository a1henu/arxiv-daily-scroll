---
layout: default
title: REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation
---

# REVEALER: Reinforcement-Guided Visual Reasoning for Element-Level Text-Image Alignment Evaluation
**arXiv**：[2512.23169v1](https://arxiv.org/abs/2512.23169) · [PDF](https://arxiv.org/pdf/2512.23169.pdf)  
**作者**：Fulin Shi, Wenyi Xiao, Bin Chen, Liang Din, Leilei Gan  

**一句话要点**：提出REVEALER框架，基于强化引导视觉推理解决文本-图像元素级对齐评估问题

**关键词**：文本-图像对齐评估, 强化学习优化, 多模态大语言模型, 元素级视觉推理, 可解释性评估

## 3 点简述
- 现有文本-图像对齐评估方法缺乏细粒度可解释性，难以反映人类偏好
- 采用结构化'定位-推理-结论'范式，利用多模态大语言模型进行元素级对齐判断
- 在多个基准测试中实现最优性能，超越专有模型和监督基线，推理效率高

## 摘要（原文）

> Evaluating the alignment between textual prompts and generated images is critical for ensuring the reliability and usability of text-to-image (T2I) models. However, most existing evaluation methods rely on coarse-grained metrics or static QA pipelines, which lack fine-grained interpretability and struggle to reflect human preferences. To address this, we propose REVEALER, a unified framework for element-level alignment evaluation based on reinforcement-guided visual reasoning. Adopting a structured "grounding-reasoning-conclusion" paradigm, our method enables Multimodal Large Language Models (MLLMs) to explicitly localize semantic elements and derive interpretable alignment judgments. We optimize the model via Group Relative Policy Optimization(GRPO) using a composite reward function that incorporates structural format, grounding accuracy, and alignment fidelity. Extensive experiments across four benchmarks-EvalMuse-40K, RichHF, MHaluBench, and GenAI-Bench-demonstrate that REVEALER achieves state-of-the-art performance. Our approach consistently outperforms both strong proprietary models and supervised baselines while demonstrating superior inference efficiency compared to existing iterative visual reasoning methods.

