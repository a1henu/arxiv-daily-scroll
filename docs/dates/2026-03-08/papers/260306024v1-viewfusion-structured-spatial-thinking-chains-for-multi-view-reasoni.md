---
layout: default
title: ViewFusion: Structured Spatial Thinking Chains for Multi-View Reasoning
---

# ViewFusion: Structured Spatial Thinking Chains for Multi-View Reasoning
**arXiv**：[2603.06024v1](https://arxiv.org/abs/2603.06024) · [PDF](https://arxiv.org/pdf/2603.06024.pdf)  
**作者**：Xingjian Tao, Yiwei Wang, Yujun Cai, Yifan Song, Jing Tang  

**一句话要点**：提出ViewFusion框架以解决多视图空间推理中跨视图关系利用不足的问题。

**关键词**：多视图推理, 空间对齐, 两阶段框架, 强化学习, 视觉语言模型

## 3 点简述
- 核心问题：当前视觉语言模型在多视图空间推理中常依赖单图像捷径，忽视跨视图对齐。
- 方法要点：采用两阶段框架，先进行空间预对齐，再基于中间工作空间进行问题驱动推理。
- 实验或效果：在MMSI-Bench上准确率提升5.3%，尤其在需要跨视图对齐的案例中表现突出。

## 摘要（原文）

> Multi-view spatial reasoning remains difficult for current vision-language models. Even when multiple viewpoints are available, models often underutilize cross-view relations and instead rely on single-image shortcuts, leading to fragile performance on viewpoint transformation and occlusion-sensitive cases. We present ViewFusion, a two-stage framework that explicitly separates cross-view spatial pre-alignment from question answering. In the first stage, the model performs deliberate spatial pre-thinking to infer viewpoint relations and spatial transformations across views, forming an intermediate workspace that goes beyond a simple re-description. In the second stage, the model conducts question-driven reasoning conditioned on this workspace to produce the final prediction. We train ViewFusion with synthetic reasoning supervision followed by reinforcement learning using GRPO, which improves answer correctness while stabilizing the intended two-stage generation behavior. On MMSI-Bench, ViewFusion improves accuracy by 5.3\% over Qwen3-VL-4B-Instruct, with the largest gains on examples that require genuine cross-view alignment.

