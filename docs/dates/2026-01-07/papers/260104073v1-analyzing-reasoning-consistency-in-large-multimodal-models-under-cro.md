---
layout: default
title: Analyzing Reasoning Consistency in Large Multimodal Models under Cross-Modal Conflicts
---

# Analyzing Reasoning Consistency in Large Multimodal Models under Cross-Modal Conflicts
**arXiv**：[2601.04073v1](https://arxiv.org/abs/2601.04073) · [PDF](https://arxiv.org/pdf/2601.04073.pdf)  
**作者**：Zhihao Zhu, Jiafeng Liang, Shixin Jiang, Jinlan Fu, Ming Liu, Guanglu Sun, See-Kiong Ng, Bing Qin  

**一句话要点**：提出主动视觉上下文精炼以缓解大模型在跨模态冲突下的推理幻觉传播

**关键词**：大模型推理, 跨模态冲突, 文本惯性, 主动视觉重定位, 推理鲁棒性

## 3 点简述
- 核心问题：大模型在视频推理中易出现文本惯性，即错误文本主导推理链而忽视视觉证据
- 方法要点：设计逻辑图扰动协议评估模型自反思能力，并引入训练无关的主动视觉重定位机制
- 实验或效果：模型自纠正率低于10%，新方法显著抑制幻觉传播并增强推理鲁棒性

## 摘要（原文）

> Large Multimodal Models (LMMs) have demonstrated impressive capabilities in video reasoning via Chain-of-Thought (CoT). However, the robustness of their reasoning chains remains questionable. In this paper, we identify a critical failure mode termed textual inertia, where once a textual hallucination occurs in the thinking process, models tend to blindly adhere to the erroneous text while neglecting conflicting visual evidence. To systematically investigate this, we propose the LogicGraph Perturbation Protocol that structurally injects perturbations into the reasoning chains of diverse LMMs spanning both native reasoning architectures and prompt-driven paradigms to evaluate their self-reflection capabilities. The results reveal that models successfully self-correct in less than 10% of cases and predominantly succumb to blind textual error propagation. To mitigate this, we introduce Active Visual-Context Refinement, a training-free inference paradigm which orchestrates an active visual re-grounding mechanism to enforce fine-grained verification coupled with an adaptive context refinement strategy to summarize and denoise the reasoning history. Experiments demonstrate that our approach significantly stifles hallucination propagation and enhances reasoning robustness.

