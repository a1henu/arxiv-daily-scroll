---
layout: default
title: VACoT: Rethinking Visual Data Augmentation with VLMs
---

# VACoT: Rethinking Visual Data Augmentation with VLMs
**arXiv**：[2512.02361v1](https://arxiv.org/abs/2512.02361) · [PDF](https://arxiv.org/pdf/2512.02361.pdf)  
**作者**：Zhengzhuo Xu, Chong Sun, SiNan Du, Chen Li, Jing Lyu, Chun Yuan  

**一句话要点**：提出VACoT框架，在推理时动态调用图像增强以提升视觉语言模型在对抗场景中的鲁棒性。

**关键词**：视觉语言模型, 图像增强, 推理时增强, 对抗鲁棒性, OCR, 后处理变换

## 3 点简述
- 视觉语言模型依赖大规模真实数据，传统增强方法在训练中效果有限，导致基础感知任务性能不足。
- VACoT在模型推理阶段集成通用视觉增强，通过去噪等后处理变换，减少训练复杂度和计算开销。
- 在13个感知基准测试中验证了VACoT的优越性，尤其在OCR相关对抗场景中显著提升鲁棒性。

## 摘要（原文）

> While visual data augmentation remains a cornerstone for training robust vision models, it has received limited attention in visual language models (VLMs), which predominantly rely on large-scale real data acquisition or synthetic diversity. Consequently, they may struggle with basic perception tasks that conventional models handle reliably. Given the substantial cost of pre-training and fine-tuning VLMs, continue training on augmented data yields limited and diminishing returns. In this paper, we present Visual Augmentation Chain-of-Thought (VACoT), a framework that dynamically invokes image augmentations during model inference. By incorporating post-hoc transformations such as denoising, VACoT substantially improves robustness on challenging and out-of-distribution inputs, especially in OCR-related adversarial scenarios. Distinct from prior approaches limited to local cropping, VACoT integrates a structured collection of general visual augmentations, broadening the query image views while reducing training complexity and computational overhead with efficient agentic reinforcement learning. We propose a conditional reward scheme that encourages necessary augmentation while penalizing verbose responses, ensuring concise and effective reasoning in perception tasks. We demonstrate the superiority of VACoT with extensive experiments on 13 perception benchmarks and further introduce AdvOCR to highlight the generalization benefits of post-hoc visual augmentations in adversarial scenarios.

