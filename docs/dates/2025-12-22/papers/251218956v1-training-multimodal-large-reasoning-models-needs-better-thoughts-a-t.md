---
layout: default
title: Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection
---

# Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection
**arXiv**：[2512.18956v1](https://arxiv.org/abs/2512.18956) · [PDF](https://arxiv.org/pdf/2512.18956.pdf)  
**作者**：Yizhi Wang, Linan Yue, Min-Ling Zhang  

**一句话要点**：提出SynSelect三阶段框架以解决多模态大推理模型长思维链数据生成与选择问题

**关键词**：多模态推理, 长思维链合成, 数据选择, 大推理模型, 监督微调, 强化学习

## 3 点简述
- 核心问题：多模态推理中长思维链数据稀缺，现有方法存在推理深度不足和模态转换错误。
- 方法要点：利用异构多模态大推理模型生成候选思维链，通过实例和批次级选择筛选高质量数据。
- 实验或效果：在多个多模态基准上，基于SynSelect数据微调的模型显著优于基线，强化学习后进一步提升。

## 摘要（原文）

> Large Reasoning Models (LRMs) have demonstrated remarkable performance on complex reasoning tasks through long Chain-of-Thought (CoT) reasoning. Extending these successes to multimodal reasoning remains challenging due to the increased complexity of integrating diverse input modalities and the scarcity of high-quality long CoT training data. Existing multimodal datasets and CoT synthesis methods still suffer from limited reasoning depth, modality conversion errors, and rigid generation pipelines, hindering model performance and stability. To this end, in this paper, we propose SynSelect, a novel three-stage Synthesis-Selection framework for generating high-quality long CoT data tailored to multimodal reasoning tasks. Specifically, SynSelect first leverages multiple heterogeneous multimodal LRMs to produce diverse candidate CoTs, and then applies both instance and batch level selection to filter high-quality CoTs that can effectively enhance the model's reasoning capabilities. Extensive experiments on multiple multimodal benchmarks demonstrate that models supervised fine-tuned on SynSelect-generated data significantly outperform baselines and achieve further improvements after reinforcement learning post-training. Our results validate SynSelect as an effective approach for advancing multimodal LRMs reasoning capabilities.

