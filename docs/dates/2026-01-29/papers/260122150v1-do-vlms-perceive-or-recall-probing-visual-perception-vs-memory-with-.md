---
layout: default
title: Do VLMs Perceive or Recall? Probing Visual Perception vs. Memory with Classic Visual Illusions
---

# Do VLMs Perceive or Recall? Probing Visual Perception vs. Memory with Classic Visual Illusions
**arXiv**：[2601.22150v1](https://arxiv.org/abs/2601.22150) · [PDF](https://arxiv.org/pdf/2601.22150.pdf)  
**作者**：Xiaoxiao Sun, Mingyang Li, Kun yuan, Min Woo Sun, Mark Endo, Shengguang Wu, Changlin Li, Yuhui Zhang, Zeyu Wang, Serena Yeung-Levy  

**一句话要点**：提出VI-Probe框架以探究大视觉语言模型在经典视觉错觉中的感知与记忆机制

**关键词**：视觉语言模型, 视觉错觉, 感知与记忆, 可控框架, 异质机制, 基于探针的评估

## 3 点简述
- 核心问题：大视觉语言模型对视觉错觉的响应是否基于感知变化或记忆模式
- 方法要点：引入可控视觉错觉框架，通过分级扰动和匹配视觉控制分离感知与记忆
- 实验或效果：发现响应持续性源于异质原因，如记忆覆盖、感知-记忆竞争和视觉处理限制

## 摘要（原文）

> Large Vision-Language Models (VLMs) often answer classic visual illusions "correctly" on original images, yet persist with the same responses when illusion factors are inverted, even though the visual change is obvious to humans. This raises a fundamental question: do VLMs perceive visual changes or merely recall memorized patterns? While several studies have noted this phenomenon, the underlying causes remain unclear. To move from observations to systematic understanding, this paper introduces VI-Probe, a controllable visual-illusion framework with graded perturbations and matched visual controls (without illusion inducer) that disentangles visually grounded perception from language-driven recall. Unlike prior work that focuses on averaged accuracy, we measure stability and sensitivity using Polarity-Flip Consistency, Template Fixation Index, and an illusion multiplier normalized against matched controls. Experiments across different families reveal that response persistence arises from heterogeneous causes rather than a single mechanism. For instance, GPT-5 exhibits memory override, Claude-Opus-4.1 shows perception-memory competition, while Qwen variants suggest visual-processing limits. Our findings challenge single-cause views and motivate probing-based evaluation that measures both knowledge and sensitivity to controlled visual change. Data and code are available at https://sites.google.com/view/vi-probe/.

