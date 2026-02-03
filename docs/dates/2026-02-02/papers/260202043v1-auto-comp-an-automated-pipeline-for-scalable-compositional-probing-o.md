---
layout: default
title: Auto-Comp: An Automated Pipeline for Scalable Compositional Probing of Contrastive Vision-Language Models
---

# Auto-Comp: An Automated Pipeline for Scalable Compositional Probing of Contrastive Vision-Language Models
**arXiv**：[2602.02043v1](https://arxiv.org/abs/2602.02043) · [PDF](https://arxiv.org/pdf/2602.02043.pdf)  
**作者**：Cristian Sbrolli, Matteo Matteucci, Toshihiko Yamasaki  

**一句话要点**：提出Auto-Comp自动化管道，用于可扩展地评估视觉语言模型的组合推理能力。

**关键词**：视觉语言模型, 组合推理, 自动化基准生成, 可控评估, 属性绑定, 空间关系

## 3 点简述
- 现代视觉语言模型在组合推理中存在关键缺陷，如混淆颜色和形状属性。
- Auto-Comp通过生成可控的合成基准，分离核心绑定能力和视觉语言复杂性。
- 评估20个模型揭示普遍组合失败，并发现上下文对空间推理和属性绑定的权衡效应。

## 摘要（原文）

> Modern Vision-Language Models (VLMs) exhibit a critical flaw in compositional reasoning, often confusing "a red cube and a blue sphere" with "a blue cube and a red sphere". Disentangling the visual and linguistic roots of these failures is a fundamental challenge for robust evaluation. To enable fine-grained, controllable analysis, we introduce Auto-Comp, a fully automated and synthetic pipeline for generating scalable benchmarks. Its controllable nature is key to dissecting and isolating different reasoning skills. Auto-Comp generates paired images from Minimal (e.g., "a monitor to the left of a bicycle on a white background") and LLM-generated Contextual captions (e.g., "In a brightly lit photography studio, a monitor is positioned to the left of a bicycle"), allowing a controlled A/B test to disentangle core binding ability from visio-linguistic complexity. Our evaluation of 20 VLMs on novel benchmarks for color binding and spatial relations reveals universal compositional failures in both CLIP and SigLIP model families. Crucially, our novel "Confusion Benchmark" reveals a deeper flaw beyond simple attribute swaps: models are highly susceptible to low-entropy distractors (e.g., repeated objects or colors), demonstrating their compositional failures extend beyond known bag-of-words limitations. we uncover a surprising trade-off: visio-linguistic context, which provides global scene cues, aids spatial reasoning but simultaneously hinders local attribute binding by introducing visual clutter. We release the Auto-Comp pipeline to facilitate future benchmark creation, alongside all our generated benchmarks (https://huggingface.co/AutoComp).

