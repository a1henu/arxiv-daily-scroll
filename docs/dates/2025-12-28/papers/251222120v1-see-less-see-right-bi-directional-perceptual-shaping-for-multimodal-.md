---
layout: default
title: See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning
---

# See Less, See Right: Bi-directional Perceptual Shaping For Multimodal Reasoning
**arXiv**：[2512.22120v1](https://arxiv.org/abs/2512.22120) · [PDF](https://arxiv.org/pdf/2512.22120.pdf)  
**作者**：Shuoshuo Zhang, Yizhen Zhang, Jingjing Fu, Lei Song, Jiang Bian, Yujiu Yang, Rui Wang  

**一句话要点**：提出双向感知塑形方法以提升多模态推理的视觉依赖性和泛化能力

**关键词**：多模态推理, 视觉语言模型, 感知塑形, KL约束, 泛化能力, 细粒度视觉证据

## 3 点简述
- 核心问题：现有视觉语言模型依赖中间视觉线索，但忽略细粒度证据，泛化差且推理成本高。
- 方法要点：通过KL一致性约束和KL分离约束，双向塑形感知，鼓励完整覆盖相关像素并防止文本捷径。
- 实验或效果：在八个基准测试中平均提升Qwen2.5-VL-7B模型8.2%，并展示强跨域泛化能力。

## 摘要（原文）

> Large vision-language models (VLMs) often benefit from intermediate visual cues, either injected via external tools or generated as latent visual tokens during reasoning, but these mechanisms still overlook fine-grained visual evidence (e.g., polylines in charts), generalize poorly across domains, and incur high inference-time cost. In this paper, we propose Bi-directional Perceptual Shaping (BiPS), which transforms question-conditioned masked views into bidirectional where-to-look signals that shape perception during training. BiPS first applies a KL-consistency constraint between the original image and an evidence-preserving view that keeps only question-relevant regions, encouraging coarse but complete coverage of supporting pixels. It then applies a KL-separation constraint between the original and an evidence-ablated view where critical pixels are masked so the image no longer supports the original answer, discouraging text-only shortcuts (i.e., answering from text alone) and enforcing fine-grained visual reliance. Across eight benchmarks, BiPS boosts Qwen2.5-VL-7B by 8.2% on average and shows strong out-of-domain generalization to unseen datasets and image types.

