---
layout: default
title: Causality-Aware Temporal Projection for Video Understanding in Video-LLMs
---

# Causality-Aware Temporal Projection for Video Understanding in Video-LLMs
**arXiv**：[2601.01804v1](https://arxiv.org/abs/2601.01804) · [PDF](https://arxiv.org/pdf/2601.01804.pdf)  
**作者**：Zhengjian Kang, Qi Chen, Rui Liu, Kangtong Mo, Xingyu Zhang, Xiaoyu Deng, Ye Zhang  

**一句话要点**：提出V-CORE框架以解决视频大语言模型中时序与因果推理的挑战

**关键词**：视频大语言模型, 时序推理, 因果感知, 参数高效微调, 视频理解

## 3 点简述
- 问题：现有视频大语言模型在时序排序和因果一致性任务上表现不佳，双向投影器可能模糊时序信息。
- 方法：V-CORE引入可学习空间聚合和因果感知时序投影器，通过块因果注意力和动态总结令牌强制单向信息流。
- 效果：在NExT-QA基准上达到61.2%准确率，在时序和因果推理子类别上分别提升3.5%和5.2%。

## 摘要（原文）

> Recent Video Large Language Models (Video-LLMs) have shown strong multimodal reasoning capabilities, yet remain challenged by video understanding tasks that require consistent temporal ordering and causal coherence. Many parameter-efficient Video-LLMs rely on unconstrained bidirectional projectors to model inter-frame interactions, which can blur temporal ordering by allowing later frames to influence earlier representations, without explicit architectural mechanisms to respect the directional nature of video reasoning. To address this limitation, we propose V-CORE, a parameter-efficient framework that introduces explicit temporal ordering constraints for video understanding. V-CORE consists of two key components: (1) Learnable Spatial Aggregation (LSA), which adaptively selects salient spatial tokens to reduce redundancy, and (2) a Causality-Aware Temporal Projector (CATP), which enforces structured unidirectional information flow via block-causal attention and a terminal dynamic summary token acting as a causal sink. This design preserves intra-frame spatial interactions while ensuring that temporal information is aggregated in a strictly ordered manner. With 4-bit QLoRA and a frozen LLM backbone, V-CORE can be trained efficiently on a single consumer GPU. Experiments show that V-CORE achieves strong performance on the challenging NExT-QA benchmark, reaching 61.2% accuracy, and remains competitive across MSVD-QA, MSRVTT-QA, and TGIF-QA, with gains concentrated in temporal and causal reasoning subcategories (+3.5% and +5.2% respectively), directly validating the importance of explicit temporal ordering constraints.

