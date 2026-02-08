---
layout: default
title: SwimBird: Eliciting Switchable Reasoning Mode in Hybrid Autoregressive MLLMs
---

# SwimBird: Eliciting Switchable Reasoning Mode in Hybrid Autoregressive MLLMs
**arXiv**：[2602.06040v1](https://arxiv.org/abs/2602.06040) · [PDF](https://arxiv.org/pdf/2602.06040.pdf)  
**作者**：Jintao Tong, Shilin Yan, Hongwei Xue, Xiaojun Tang, Kunyu Shi, Guannan Zhang, Ruixuan Li, Yixiong Zou  

**一句话要点**：提出SwimBird模型，通过动态切换推理模式解决多模态大语言模型在视觉密集任务中的性能限制。

**关键词**：多模态大语言模型, 动态推理模式, 视觉密集任务, 混合自回归, 监督微调数据集, 视觉理解基准

## 3 点简述
- 核心问题：现有MLLMs推理模式固定，无法自适应选择文本或视觉推理，导致视觉任务性能受限。
- 方法要点：采用混合自回归框架，统一文本和视觉思维预测，并构建多样化数据集以支持三种推理模式。
- 实验或效果：在文本推理和视觉理解基准测试中实现最优结果，提升视觉密集任务性能同时保持文本逻辑。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have made remarkable progress in multimodal perception and reasoning by bridging vision and language. However, most existing MLLMs perform reasoning primarily with textual CoT, which limits their effectiveness on vision-intensive tasks. Recent approaches inject a fixed number of continuous hidden states as "visual thoughts" into the reasoning process and improve visual performance, but often at the cost of degraded text-based logical reasoning. We argue that the core limitation lies in a rigid, pre-defined reasoning pattern that cannot adaptively choose the most suitable thinking modality for different user queries. We introduce SwimBird, a reasoning-switchable MLLM that dynamically switches among three reasoning modes conditioned on the input: (1) text-only reasoning, (2) vision-only reasoning (continuous hidden states as visual thoughts), and (3) interleaved vision-text reasoning. To enable this capability, we adopt a hybrid autoregressive formulation that unifies next-token prediction for textual thoughts with next-embedding prediction for visual thoughts, and design a systematic reasoning-mode curation strategy to construct SwimBird-SFT-92K, a diverse supervised fine-tuning dataset covering all three reasoning patterns. By enabling flexible, query-adaptive mode selection, SwimBird preserves strong textual logic while substantially improving performance on vision-dense tasks. Experiments across diverse benchmarks covering textual reasoning and challenging visual understanding demonstrate that SwimBird achieves state-of-the-art results and robust gains over prior fixed-pattern multimodal reasoning methods.

