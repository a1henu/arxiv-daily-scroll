---
layout: default
title: Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity
---

# Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity
**arXiv**：[2512.14320v1](https://arxiv.org/abs/2512.14320) · [PDF](https://arxiv.org/pdf/2512.14320.pdf)  
**作者**：Shuai Dong, Jie Zhang, Guoying Zhao, Shiguang Shan, Xilin Chen  

**一句话要点**：提出SIFM方法以增强图像对恶意扩散编辑的免疫能力

**关键词**：图像免疫, 扩散模型, 语义对齐, 特征扰动, 免疫评估, 多模态大语言模型

## 3 点简述
- 核心问题：现有图像免疫评估指标忽视语义对齐破坏，仅关注视觉差异。
- 方法要点：SIFM通过协同扰动扩散中间特征，最大化语义偏离并最小化特征范数以诱导感知退化。
- 实验或效果：引入ISR新指标，实验显示SIFM在保护视觉内容方面达到最先进性能。

## 摘要（原文）

> Text-guided image editing via diffusion models, while powerful, raises significant concerns about misuse, motivating efforts to immunize images against unauthorized edits using imperceptible perturbations. Prevailing metrics for evaluating immunization success typically rely on measuring the visual dissimilarity between the output generated from a protected image and a reference output generated from the unprotected original. This approach fundamentally overlooks the core requirement of image immunization, which is to disrupt semantic alignment with attacker intent, regardless of deviation from any specific output. We argue that immunization success should instead be defined by the edited output either semantically mismatching the prompt or suffering substantial perceptual degradations, both of which thwart malicious intent. To operationalize this principle, we propose Synergistic Intermediate Feature Manipulation (SIFM), a method that strategically perturbs intermediate diffusion features through dual synergistic objectives: (1) maximizing feature divergence from the original edit trajectory to disrupt semantic alignment with the expected edit, and (2) minimizing feature norms to induce perceptual degradations. Furthermore, we introduce the Immunization Success Rate (ISR), a novel metric designed to rigorously quantify true immunization efficacy for the first time. ISR quantifies the proportion of edits where immunization induces either semantic failure relative to the prompt or significant perceptual degradations, assessed via Multimodal Large Language Models (MLLMs). Extensive experiments show our SIFM achieves the state-of-the-art performance for safeguarding visual content against malicious diffusion-based manipulation.

