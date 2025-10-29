---
layout: default
title: Latent Sketchpad: Sketching Visual Thoughts to Elicit Multimodal Reasoning in MLLMs
---

# Latent Sketchpad: Sketching Visual Thoughts to Elicit Multimodal Reasoning in MLLMs
**arXiv**：[2510.24514v1](https://arxiv.org/abs/2510.24514) · [PDF](https://arxiv.org/pdf/2510.24514.pdf)  
**作者**：Huanyu Zhang, Wenshan Wu, Chengzu Li, Ning Shang, Yan Xia, Yangyu Huang, Yifan Zhang, Li Dong, Zhang Zhang, Liang Wang, Tieniu Tan, Furu Wei  

**一句话要点**：提出Latent Sketchpad框架，通过内部视觉草图增强MLLMs在复杂场景中的多模态推理能力

**关键词**：多模态大语言模型, 视觉推理, 草图生成, 自回归推理, 可解释性, 视觉规划

## 3 点简述
- 核心问题：MLLMs在需要视觉规划和想象的复杂场景中表现不佳，缺乏内部视觉思考能力
- 方法要点：集成视觉生成到自回归推理过程，使用Context-Aware Vision Head和Sketch Decoder生成可解释草图
- 实验或效果：在MazePlanning数据集上评估，推理性能与骨干模型相当或更优，并泛化至Gemma3和Qwen2.5-VL等模型

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) excel at visual understanding,
> they often struggle in complex scenarios that require visual planning and
> imagination. Inspired by how humans use sketching as a form of visual thinking
> to develop and communicate ideas, we introduce Latent Sketchpad, a framework
> that equips MLLMs with an internal visual scratchpad. The internal visual
> representations of MLLMs have traditionally been confined to perceptual
> understanding. We repurpose them to support generative visual thought without
> compromising reasoning ability. Building on frontier MLLMs, our approach
> integrates visual generation directly into their native autoregressive
> reasoning process. It allows the model to interleave textual reasoning with the
> generation of visual latents. These latents guide the internal thought process
> and can be translated into sketch images for interpretability. To realize this,
> we introduce two components: a Context-Aware Vision Head autoregressively
> produces visual representations, and a pretrained Sketch Decoder renders these
> into human-interpretable images. We evaluate the framework on our new dataset
> MazePlanning. Experiments across various MLLMs show that Latent Sketchpad
> delivers comparable or even superior reasoning performance to their backbone.
> It further generalizes across distinct frontier MLLMs, including Gemma3 and
> Qwen2.5-VL. By extending model's textual reasoning to visual thinking, our
> framework opens new opportunities for richer human-computer interaction and
> broader applications. More details and resources are available on our project
> page: https://latent-sketchpad.github.io/.

