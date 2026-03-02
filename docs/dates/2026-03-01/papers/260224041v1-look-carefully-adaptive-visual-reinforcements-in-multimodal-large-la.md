---
layout: default
title: Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation
---

# Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation
**arXiv**：[2602.24041v1](https://arxiv.org/abs/2602.24041) · [PDF](https://arxiv.org/pdf/2602.24041.pdf)  
**作者**：Xingyu Zhu, Kesen Zhao, Liang Yi, Shuo Wang, Zhicai Wang, Beier Zhu, Hanwang Zhang  

**一句话要点**：提出自适应视觉增强框架以解决多模态大语言模型中的幻觉问题

**关键词**：多模态大语言模型, 幻觉缓解, 自适应视觉增强, 训练免费框架, 视觉令牌缩减, 补丁对齐

## 3 点简述
- 核心问题：MLLMs在视觉语言推理中易产生幻觉，现有方法成本高或延迟大
- 方法要点：通过原型令牌缩减和OT引导补丁增强，选择性强化关键视觉信息
- 实验或效果：在多个MLLMs上显著减少幻觉，同时保持通用能力

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable progress in vision-language reasoning, yet they remain vulnerable to hallucination, where generated content deviates from visual evidence. Existing mitigation strategies either require costly supervision during training or introduce additional latency at inference time. Recent vision enhancement methods attempt to address this issue by reinforcing visual tokens during decoding, but they typically inject all tokens indiscriminately, which causes interference from background regions and distracts the model from critical cues. To overcome this challenge, we propose Adaptive Visual Reinforcement (AIR), a training-free framework for MLLMs. AIR consists of two components. Prototype-based token reduction condenses the large pool of visual tokens into a compact subset to suppress redundancy. OT-guided patch reinforcement quantifies the alignment between hidden states and patch embeddings to selectively integrate the most consistent patches into feed-forward layers. As a result, AIR enhances the model's reliance on salient visual information and effectively mitigates hallucination. Extensive experiments across representative MLLMs demonstrate that AIR substantially reduces hallucination while preserving general capabilities, establishing it as an effective solution for building reliable MLLMs.

