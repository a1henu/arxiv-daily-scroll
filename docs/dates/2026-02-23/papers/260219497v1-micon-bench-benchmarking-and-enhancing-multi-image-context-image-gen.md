---
layout: default
title: MICON-Bench: Benchmarking and Enhancing Multi-Image Context Image Generation in Unified Multimodal Models
---

# MICON-Bench: Benchmarking and Enhancing Multi-Image Context Image Generation in Unified Multimodal Models
**arXiv**：[2602.19497v1](https://arxiv.org/abs/2602.19497) · [PDF](https://arxiv.org/pdf/2602.19497.pdf)  
**作者**：Mingrui Wu, Hang Liu, Jiayi Ji, Xiaoshuai Sun, Rongrong Ji  

**一句话要点**：提出MICON-Bench基准和DAR机制以增强统一多模态模型的多图像上下文生成能力

**关键词**：多图像上下文生成, 统一多模态模型, 基准测试, 注意力机制, 自动评估, 图像生成

## 3 点简述
- 现有基准缺乏多图像上下文生成评估，聚焦文本到图像或单图像编辑任务
- 引入MICON-Bench基准和MLLM驱动评估框架，覆盖六项任务以评估跨图像组合与推理
- 提出动态注意力再平衡机制，无需训练即可提升生成一致性和减少幻觉

## 摘要（原文）

> Recent advancements in Unified Multimodal Models (UMMs) have enabled remarkable image understanding and generation capabilities. However, while models like Gemini-2.5-Flash-Image show emerging abilities to reason over multiple related images, existing benchmarks rarely address the challenges of multi-image context generation, focusing mainly on text-to-image or single-image editing tasks. In this work, we introduce \textbf{MICON-Bench}, a comprehensive benchmark covering six tasks that evaluate cross-image composition, contextual reasoning, and identity preservation. We further propose an MLLM-driven Evaluation-by-Checkpoint framework for automatic verification of semantic and visual consistency, where multimodal large language model (MLLM) serves as a verifier. Additionally, we present \textbf{Dynamic Attention Rebalancing (DAR)}, a training-free, plug-and-play mechanism that dynamically adjusts attention during inference to enhance coherence and reduce hallucinations. Extensive experiments on various state-of-the-art open-source models demonstrate both the rigor of MICON-Bench in exposing multi-image reasoning challenges and the efficacy of DAR in improving generation quality and cross-image coherence. Github: https://github.com/Angusliuuu/MICON-Bench.

