---
layout: default
title: PrismVAU: Prompt-Refined Inference System for Multimodal Video Anomaly Understanding
---

# PrismVAU: Prompt-Refined Inference System for Multimodal Video Anomaly Understanding
**arXiv**：[2601.02927v1](https://arxiv.org/abs/2601.02927) · [PDF](https://arxiv.org/pdf/2601.02927.pdf)  
**作者**：Iñaki Erregue, Kamal Nasrollahi, Sergio Escalera  

**一句话要点**：提出PrismVAU系统，通过提示优化实现轻量级实时视频异常理解

**关键词**：视频异常理解, 多模态大语言模型, 提示工程, 实时系统, 弱监督学习

## 3 点简述
- 视频异常理解需定位、描述和推理异常，现有方法依赖微调或外部模块，成本高且复杂
- PrismVAU使用单一现成多模态大语言模型，结合粗粒度评分和提示优化模块，无需指令调优或密集处理
- 在标准基准测试中，系统实现竞争性检测性能和可解释异常解释，适用于实际应用

## 摘要（原文）

> Video Anomaly Understanding (VAU) extends traditional Video Anomaly Detection (VAD) by not only localizing anomalies but also describing and reasoning about their context. Existing VAU approaches often rely on fine-tuned multimodal large language models (MLLMs) or external modules such as video captioners, which introduce costly annotations, complex training pipelines, and high inference overhead. In this work, we introduce PrismVAU, a lightweight yet effective system for real-time VAU that leverages a single off-the-shelf MLLM for anomaly scoring, explanation, and prompt optimization. PrismVAU operates in two complementary stages: (1) a coarse anomaly scoring module that computes frame-level anomaly scores via similarity to textual anchors, and (2) an MLLM-based refinement module that contextualizes anomalies through system and user prompts. Both textual anchors and prompts are optimized with a weakly supervised Automatic Prompt Engineering (APE) framework. Extensive experiments on standard VAD benchmarks demonstrate that PrismVAU delivers competitive detection performance and interpretable anomaly explanations -- without relying on instruction tuning, frame-level annotations, and external modules or dense processing -- making it an efficient and practical solution for real-world applications.

