---
layout: default
title: Latent Implicit Visual Reasoning
---

# Latent Implicit Visual Reasoning
**arXiv**：[2512.21218v1](https://arxiv.org/abs/2512.21218) · [PDF](https://arxiv.org/pdf/2512.21218.pdf)  
**作者**：Kelvin Li, Chuyi Shang, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig  

**一句话要点**：提出无监督视觉推理令牌机制，以增强大型多模态模型在视觉中心任务中的推理能力。

**关键词**：视觉推理, 无监督学习, 多模态模型, 任务自适应, 令牌机制

## 3 点简述
- 核心问题：大型多模态模型依赖文本推理，难以处理视觉主导任务，现有方法需监督且泛化性差。
- 方法要点：训练模型无监督发现和使用视觉推理令牌，全局关注并自适应重编码图像，无需人工标注。
- 实验或效果：在多样化视觉中心任务上超越直接微调，达到先进水平，并泛化至多任务指令调优。

## 摘要（原文）

> While Large Multimodal Models (LMMs) have made significant progress, they remain largely text-centric, relying on language as their core reasoning modality. As a result, they are limited in their ability to handle reasoning tasks that are predominantly visual. Recent approaches have sought to address this by supervising intermediate visual steps with helper images, depth maps, or image crops. However, these strategies impose restrictive priors on what "useful" visual abstractions look like, add heavy annotation costs, and struggle to generalize across tasks. To address this critical limitation, we propose a task-agnostic mechanism that trains LMMs to discover and use visual reasoning tokens without explicit supervision. These tokens attend globally and re-encode the image in a task-adaptive way, enabling the model to extract relevant visual information without hand-crafted supervision. Our approach outperforms direct fine-tuning and achieves state-of-the-art results on a diverse range of vision-centric tasks -- including those where intermediate abstractions are hard to specify -- while also generalizing to multi-task instruction tuning.

