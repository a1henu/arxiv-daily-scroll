---
layout: default
title: Semantic Misalignment in Vision-Language Models under Perceptual Degradation
---

# Semantic Misalignment in Vision-Language Models under Perceptual Degradation
**arXiv**：[2601.08355v1](https://arxiv.org/abs/2601.08355) · [PDF](https://arxiv.org/pdf/2601.08355.pdf)  
**作者**：Guo Cheng  

**一句话要点**：研究视觉语言模型在感知退化下的语义错位，揭示像素级鲁棒性与多模态语义可靠性之间的脱节。

**关键词**：视觉语言模型, 感知退化, 语义错位, 安全关键应用, 鲁棒性评估

## 3 点简述
- 核心问题：视觉语言模型在自动驾驶等安全关键应用中，对上游视觉感知退化的鲁棒性未知，可能导致语义推理失败。
- 方法要点：使用Cityscapes数据集语义分割模拟感知退化，引入语言级错位指标量化幻觉、关键遗漏和安全误判。
- 实验或效果：发现感知退化仅轻微影响分割指标，但导致下游模型严重语义错位，凸显当前系统局限性。

## 摘要（原文）

> Vision-Language Models (VLMs) are increasingly deployed in autonomous driving and embodied AI systems, where reliable perception is critical for safe semantic reasoning and decision-making. While recent VLMs demonstrate strong performance on multimodal benchmarks, their robustness to realistic perception degradation remains poorly understood. In this work, we systematically study semantic misalignment in VLMs under controlled degradation of upstream visual perception, using semantic segmentation on the Cityscapes dataset as a representative perception module. We introduce perception-realistic corruptions that induce only moderate drops in conventional segmentation metrics, yet observe severe failures in downstream VLM behavior, including hallucinated object mentions, omission of safety-critical entities, and inconsistent safety judgments. To quantify these effects, we propose a set of language-level misalignment metrics that capture hallucination, critical omission, and safety misinterpretation, and analyze their relationship with segmentation quality across multiple contrastive and generative VLMs. Our results reveal a clear disconnect between pixel-level robustness and multimodal semantic reliability, highlighting a critical limitation of current VLM-based systems and motivating the need for evaluation frameworks that explicitly account for perception uncertainty in safety-critical applications.

