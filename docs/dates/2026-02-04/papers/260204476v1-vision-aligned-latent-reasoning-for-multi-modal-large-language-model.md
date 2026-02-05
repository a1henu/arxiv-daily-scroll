---
layout: default
title: Vision-aligned Latent Reasoning for Multi-modal Large Language Model
---

# Vision-aligned Latent Reasoning for Multi-modal Large Language Model
**arXiv**：[2602.04476v1](https://arxiv.org/abs/2602.04476) · [PDF](https://arxiv.org/pdf/2602.04476.pdf)  
**作者**：Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin  

**一句话要点**：提出视觉对齐潜在推理框架以解决多模态大语言模型在长上下文推理中的视觉信息稀释问题

**关键词**：多模态大语言模型, 视觉对齐推理, 长上下文理解, 潜在空间对齐, 测试时缩放

## 3 点简述
- 核心问题：多模态大语言模型在长上下文生成中视觉信息逐渐稀释，阻碍多步推理能力
- 方法要点：动态生成视觉对齐潜在令牌，在推理步骤前对齐中间嵌入以保留视觉知识
- 实验或效果：在VSI-Bench等基准上显著提升性能，实现19.9%的增益，并展示测试时缩放行为

## 摘要（原文）

> Despite recent advancements in Multi-modal Large Language Models (MLLMs) on diverse understanding tasks, these models struggle to solve problems which require extensive multi-step reasoning. This is primarily due to the progressive dilution of visual information during long-context generation, which hinders their ability to fully exploit test-time scaling. To address this issue, we introduce Vision-aligned Latent Reasoning (VaLR), a simple, yet effective reasoning framework that dynamically generates vision-aligned latent tokens before each Chain of Thought reasoning step, guiding the model to reason based on perceptual cues in the latent space. Specifically, VaLR is trained to preserve visual knowledge during reasoning by aligning intermediate embeddings of MLLM with those from vision encoders. Empirical results demonstrate that VaLR consistently outperforms existing approaches across a wide range of benchmarks requiring long-context understanding or precise visual perception, while exhibiting test-time scaling behavior not observed in prior MLLMs. In particular, VaLR improves the performance significantly from 33.0% to 52.9% on VSI-Bench, achieving a 19.9%p gain over Qwen2.5-VL.

