---
layout: default
title: IVRA: Improving Visual-Token Relations for Robot Action Policy with Training-Free Hint-Based Guidance
---

# IVRA: Improving Visual-Token Relations for Robot Action Policy with Training-Free Hint-Based Guidance
**arXiv**：[2601.16207v1](https://arxiv.org/abs/2601.16207) · [PDF](https://arxiv.org/pdf/2601.16207.pdf)  
**作者**：Jongwoo Park, Kanchana Ranasinghe, Jinhyeok Jang, Cristina Mata, Yoo Sung Jang, Michael S Ryoo  

**一句话要点**：提出IVRA方法，通过训练无关的提示引导改善视觉-语言-动作模型的空间理解能力

**关键词**：视觉-语言-动作模型, 空间理解, 训练无关方法, 机器人操作, 亲和性提示, 推理时干预

## 3 点简述
- 核心问题：VLA模型将图像块展平为1D序列，削弱了2D空间线索，影响精确操作。
- 方法要点：利用内置视觉编码器的亲和性提示，在推理时选择性注入到语言模型层，无需训练或外部编码器。
- 实验或效果：在2D和3D模拟基准及真实机器人任务中，IVRA提升了多种VLA架构的性能，如VIMA上平均成功率提高4.2%。

## 摘要（原文）

> Many Vision-Language-Action (VLA) models flatten image patches into a 1D token sequence, weakening the 2D spatial cues needed for precise manipulation. We introduce IVRA, a lightweight, training-free method that improves spatial understanding by exploiting affinity hints already available in the model's built-in vision encoder, without requiring any external encoder or retraining. IVRA selectively injects these affinity signals into a language-model layer in which instance-level features reside. This inference-time intervention realigns visual-token interactions and better preserves geometric structure while keeping all model parameters fixed. We demonstrate the generality of IVRA by applying it to diverse VLA architectures (LLaRA, OpenVLA, and FLOWER) across simulated benchmarks spanning both 2D and 3D manipulation (VIMA and LIBERO) and on various real-robot tasks. On 2D VIMA, IVRA improves average success by +4.2% over the baseline LLaRA in a low-data regime. On 3D LIBERO, it yields consistent gains over the OpenVLA and FLOWER baselines, including improvements when baseline accuracy is near saturation (96.3% to 97.1%). All code and models will be released publicly. Visualizations are available at: jongwoopark7978.github.io/IVRA

