---
layout: default
title: Unleashing MLLMs on the Edge: A Unified Framework for Cross-Modal ReID via Adaptive SVD Distillation
---

# Unleashing MLLMs on the Edge: A Unified Framework for Cross-Modal ReID via Adaptive SVD Distillation
**arXiv**：[2602.12936v1](https://arxiv.org/abs/2602.12936) · [PDF](https://arxiv.org/pdf/2602.12936.pdf)  
**作者**：Hongbo Jiang, Jie Li, Xinqi Cai, Tianyu Xie, Yunhang Shen, Pingyang Dai, Liujuan Cao  

**一句话要点**：提出MLLMEmbed-ReID框架，通过自适应SVD蒸馏实现跨模态ReID在边缘设备的统一部署

**关键词**：跨模态重识别, 多模态大语言模型, 知识蒸馏, 边缘计算, 低秩适应, 统一嵌入空间

## 3 点简述
- 核心问题：云边部署中跨模态ReID模型碎片化，现有方法难以统一MLLM并有效蒸馏至边缘
- 方法要点：基于指令提示和LoRA-SFT微调MLLM生成统一嵌入空间，采用主成分映射和特征关系损失进行蒸馏
- 实验或效果：边缘模型在多个视觉CM-ReID基准上达到SOTA，云端模型在所有基准上表现优异

## 摘要（原文）

> Practical cloud-edge deployment of Cross-Modal Re-identification (CM-ReID) faces challenges due to maintaining a fragmented ecosystem of specialized cloud models for diverse modalities. While Multi-Modal Large Language Models (MLLMs) offer strong unification potential, existing approaches fail to adapt them into a single end-to-end backbone and lack effective knowledge distillation strategies for edge deployment. To address these limitations, we propose MLLMEmbed-ReID, a unified framework based on a powerful cloud-edge architecture. First, we adapt a foundational MLLM into a state-of-the-art cloud model. We leverage instruction-based prompting to guide the MLLM in generating a unified embedding space across RGB, infrared, sketch, and text modalities. This model is then trained efficiently with a hierarchical Low-Rank Adaptation finetuning (LoRA-SFT) strategy, optimized under a holistic cross-modal alignment objective. Second, to deploy its knowledge onto an edge-native student, we introduce a novel distillation strategy motivated by the low-rank property in the teacher's feature space. To prioritize essential information, this method employs a Principal Component Mapping loss, while relational structures are preserved via a Feature Relation loss. Our lightweight edge-based model achieves state-of-the-art performance on multiple visual CM-ReID benchmarks, while its cloud-based counterpart excels across all CM-ReID benchmarks. The MLLMEmbed-ReID framework thus presents a complete and effective solution for deploying unified MLLM-level intelligence on resource-constrained devices. The code and models will be open-sourced soon.

