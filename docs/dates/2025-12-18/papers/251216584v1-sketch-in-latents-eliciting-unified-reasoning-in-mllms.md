---
layout: default
title: Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs
---

# Sketch-in-Latents: Eliciting Unified Reasoning in MLLMs
**arXiv**：[2512.16584v1](https://arxiv.org/abs/2512.16584) · [PDF](https://arxiv.org/pdf/2512.16584.pdf)  
**作者**：Jintao Tong, Jiaqi Gu, Yujing Lou, Lubin Fan, Yixiong Zou, Yue Wu, Jieping Ye, Ruixuan Li  

**一句话要点**：提出Sketch-in-Latents以在统一特征空间中实现多模态推理的视觉想象

**关键词**：多模态大语言模型, 视觉想象, 统一推理空间, 连续视觉嵌入, 自回归生成

## 3 点简述
- 核心问题：MLLMs在需要视觉想象的场景中表现不足，缺乏统一的视觉-文本推理空间
- 方法要点：扩展MLLMs的自回归能力，动态生成连续视觉嵌入作为视觉思维，无需外部工具
- 实验或效果：在视觉中心任务上表现优异，并泛化到多种多模态基准测试

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at visual understanding tasks through text reasoning, they often fall short in scenarios requiring visual imagination. Unlike current works that take predefined external toolkits or generate images during thinking, however, humans can form flexible visual-text imagination and interactions during thinking without predefined toolkits, where one important reason is that humans construct the visual-text thinking process in a unified space inside the brain. Inspired by this capability, given that current MLLMs already encode visual and text information in the same feature space, we hold that visual tokens can be seamlessly inserted into the reasoning process carried by text tokens, where ideally, all visual imagination processes can be encoded by the latent features. To achieve this goal, we propose Sketch-in-Latents (SkiLa), a novel paradigm for unified multi-modal reasoning that expands the auto-regressive capabilities of MLLMs to natively generate continuous visual embeddings, termed latent sketch tokens, as visual thoughts. During multi-step reasoning, the model dynamically alternates between textual thinking mode for generating textual think tokens and visual sketching mode for generating latent sketch tokens. A latent visual semantics reconstruction mechanism is proposed to ensure these latent sketch tokens are semantically grounded. Extensive experiments demonstrate that SkiLa achieves superior performance on vision-centric tasks while exhibiting strong generalization to diverse general multi-modal benchmarks. Codes will be released at https://github.com/TungChintao/SkiLa.

