---
layout: default
title: DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning
---

# DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning
**arXiv**：[2510.13375v1](https://arxiv.org/abs/2510.13375) · [PDF](https://arxiv.org/pdf/2510.13375.pdf)  
**作者**：Tianyuan Yuan, Yicheng Liu, Chenhao Lu, Zhuoguang Chen, Tao Jiang, Hang Zhao  

**一句话要点**：提出DepthVLA以增强视觉-语言-动作模型的空间推理能力

**关键词**：视觉-语言-动作模型, 深度感知, 空间推理, 混合Transformer, 端到端学习

## 3 点简述
- 核心问题：现有VLA模型在需要精确空间推理的任务中性能下降，源于视觉-语言模型的空间推理能力有限。
- 方法要点：引入预训练深度预测模块，采用混合Transformer设计统一VLM、深度Transformer和动作专家。
- 实验或效果：在真实世界和模拟环境中评估，DepthVLA在多个基准上优于现有方法，提升任务完成率。

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently shown impressive
> generalization and language-guided manipulation capabilities. However, their
> performance degrades on tasks requiring precise spatial reasoning due to
> limited spatial reasoning inherited from Vision-Language Models (VLMs).
> Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D
> space, which reduces training efficiency and is still insufficient for accurate
> spatial understanding. In this work, we present DepthVLA, a simple yet
> effective VLA architecture that explicitly incorporates spatial awareness
> through a pretrained depth prediction module. DepthVLA adopts a
> mixture-of-transformers design that unifies a VLM, a depth transformer, and an
> action expert with fully shared attentions, forming an end-to-end model with
> enhanced spatial reasoning. Extensive evaluations in both real-world and
> simulated environments show that DepthVLA outperforms state-of-the-art
> approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs.
> 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator.
> Our code will be made publicly available.

