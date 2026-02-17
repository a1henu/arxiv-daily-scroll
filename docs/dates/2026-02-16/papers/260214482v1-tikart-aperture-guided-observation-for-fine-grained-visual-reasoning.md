---
layout: default
title: TikArt: Aperture-Guided Observation for Fine-Grained Visual Reasoning via Reinforcement Learning
---

# TikArt: Aperture-Guided Observation for Fine-Grained Visual Reasoning via Reinforcement Learning
**arXiv**：[2602.14482v1](https://arxiv.org/abs/2602.14482) · [PDF](https://arxiv.org/pdf/2602.14482.pdf)  
**作者**：Hao Ding, Zhichuan Yang, Weijie Ge, Ziqin Gao, Chaoyi Lu, Lei Zhao  

**一句话要点**：提出TikArt，通过强化学习优化多模态大语言模型在细粒度视觉推理中的区域观察策略。

**关键词**：细粒度视觉推理, 多模态大语言模型, 强化学习, 区域观察, 孔径引导, 视觉语言任务

## 3 点简述
- 核心问题：细粒度视觉推理中关键证据易在全局图像编码中丢失，如微小物体或杂乱区域。
- 方法要点：基于Think-Aperture-Observe循环，使用Zoom和Segment动作引导区域观察，结合AGRPO强化学习优化策略。
- 实验或效果：在多个基准测试中优于骨干模型，提供可解释的孔径轨迹，提升高分辨率推理性能。

## 摘要（原文）

> We address fine-grained visual reasoning in multimodal large language models (MLLMs), where key evidence may reside in tiny objects, cluttered regions, or subtle markings that are lost under a single global image encoding. We introduce TikArt (Thinking Aperture), an aperture-guided agent that casts multi-step vision-language reasoning as a decision process over regions of interest. TikArt follows a Think-Aperture-Observe loop, alternating between language generation and two aperture actions: Zoom extracts rectangular crops, while Segment invokes SAM2 to obtain mask-based crops for irregular targets. After every action, the model must produce an explicit observation, turning local visual cues into persistent linguistic memory. Built on Qwen3-VL-8B, TikArt optimizes its reasoning policy with AGRPO, a GRPO-style reinforcement learning algorithm with a two-stage curriculum: it warms up segmentation actions and then jointly optimizes visual math, fine-grained VQA, and segmentation, using rewards that couple task success with purposeful aperture use. Experiments on V*, HR-Bench-4K/8K, MME-RealWorld-Lite, MMStar, RefCOCO, and ReasonSeg show consistent gains over the backbone and yield interpretable aperture trajectories for high-resolution reasoning.

