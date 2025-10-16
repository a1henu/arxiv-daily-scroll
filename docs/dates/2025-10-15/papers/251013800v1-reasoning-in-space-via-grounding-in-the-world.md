---
layout: default
title: Reasoning in Space via Grounding in the World
---

# Reasoning in Space via Grounding in the World
**arXiv**：[2510.13800v1](https://arxiv.org/abs/2510.13800) · [PDF](https://arxiv.org/pdf/2510.13800.pdf)  
**作者**：Yiming Chen, Zekun Qi, Wenyao Zhang, Xin Jin, Li Zhang, Peidong Liu  

**一句话要点**：提出GS-Reasoner以解决3D视觉定位与空间推理的融合问题

**关键词**：3D视觉定位, 空间推理, 双路径池化, 统一3D表示, 自回归定位, GCoT数据集

## 3 点简述
- 核心问题：现有3D LLMs缺乏统一表示，导致定位性能差或依赖外部模块
- 方法要点：采用双路径池化机制，构建统一图像块3D表示，无需增加输入令牌
- 实验或效果：在3D视觉定位和空间推理任务中达到先进性能，无需外部模块

## 摘要（原文）

> In this paper, we claim that 3D visual grounding is the cornerstone of
> spatial reasoning and introduce the Grounded-Spatial Reasoner (GS-Reasoner) to
> explore the effective spatial representations that bridge the gap between them.
> Existing 3D LLMs suffer from the absence of a unified 3D representation capable
> of jointly capturing semantic and geometric information. This deficiency is
> manifested either in poor performance on grounding or in an excessive reliance
> on external modules, ultimately hindering the seamless integration of grounding
> and spatial reasoning. To address this, we propose a simple yet effective
> dual-path pooling mechanism that tightly aligns geometric features with both
> semantic and positional cues, constructing a unified image patch-based 3D
> representation that encapsulates all essential information without increasing
> the number of input tokens. Leveraging this holistic representation,
> GS-Reasoner is the first 3D LLM that achieves autoregressive grounding entirely
> without external modules while delivering performance comparable to
> state-of-the-art models, establishing a unified and self-contained framework
> for 3D spatial reasoning. To further bridge grounding and spatial reasoning, we
> introduce the Grounded Chain-of-Thought (GCoT) dataset. This dataset is
> meticulously curated to include both 3D bounding box annotations for objects
> referenced in reasoning questions and step-by-step reasoning paths that
> integrate grounding as a core component of the problem-solving process.
> Extensive experiments demonstrate that GS-Reasoner achieves impressive results
> on 3D visual grounding, which in turn significantly enhances its spatial
> reasoning capabilities, leading to state-of-the-art performance.

