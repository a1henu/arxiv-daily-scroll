---
layout: default
title: VIBE: Visual Instruction Based Editor
---

# VIBE: Visual Instruction Based Editor
**arXiv**：[2601.02242v1](https://arxiv.org/abs/2601.02242) · [PDF](https://arxiv.org/pdf/2601.02242.pdf)  
**作者**：Grigorii Alekseenko, Aleksandr Gordeev, Irina Tolstykh, Bulat Suleimanov, Vladimir Dokholyan, Georgii Fedorov, Sergey Yakubson, Aleksandra Tsybina, Mikhail Chernyshov, Maksim Kuprashevich  

**一句话要点**：提出VIBE：基于视觉指令的紧凑高效图像编辑管道，以低参数模型实现高质量编辑。

**关键词**：指令图像编辑, 紧凑模型, 扩散模型, 源一致性, 低内存推理, 高分辨率生成

## 3 点简述
- 核心问题：现有指令图像编辑模型参数大、计算成本高，开源方案质量有限。
- 方法要点：使用2B参数Qwen3-VL指导编辑，结合1.6B参数Sana1.5扩散模型生成图像。
- 实验或效果：在ImgEdit和GEdit基准上匹配或超越更大模型，特别擅长保持源图像一致性的编辑。

## 摘要（原文）

> Instruction-based image editing is among the fastest developing areas in generative AI. Over the past year, the field has reached a new level, with dozens of open-source models released alongside highly capable commercial systems. However, only a limited number of open-source approaches currently achieve real-world quality. In addition, diffusion backbones, the dominant choice for these pipelines, are often large and computationally expensive for many deployments and research settings, with widely used variants typically containing 6B to 20B parameters. This paper presents a compact, high-throughput instruction-based image editing pipeline that uses a modern 2B-parameter Qwen3-VL model to guide the editing process and the 1.6B-parameter diffusion model Sana1.5 for image generation. Our design decisions across architecture, data processing, training configuration, and evaluation target low-cost inference and strict source consistency while maintaining high quality across the major edit categories feasible at this scale. Evaluated on the ImgEdit and GEdit benchmarks, the proposed method matches or exceeds the performance of substantially heavier baselines, including models with several times as many parameters and higher inference cost, and is particularly strong on edits that require preserving the input image, such as an attribute adjustment, object removal, background edits, and targeted replacement. The model fits within 24 GB of GPU memory and generates edited images at up to 2K resolution in approximately 4 seconds on an NVIDIA H100 in BF16, without additional inference optimizations or distillation.

