---
layout: default
title: Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs
---

# Gated Relational Alignment via Confidence-based Distillation for Efficient VLMs
**arXiv**：[2601.22709v1](https://arxiv.org/abs/2601.22709) · [PDF](https://arxiv.org/pdf/2601.22709.pdf)  
**作者**：Yanlong Chen, Amirhossein Habibian, Luca Benini, Yawei Li  

**一句话要点**：提出GRACE框架，通过置信度门控蒸馏和关系对齐，实现视觉语言模型的高效量化部署。

**关键词**：视觉语言模型, 量化感知训练, 知识蒸馏, 信息瓶颈, 模型压缩, 高效部署

## 3 点简述
- 核心问题：视觉语言模型量化部署成本高，后训练量化导致精度显著下降。
- 方法要点：基于信息瓶颈原则，结合知识蒸馏与量化感知训练，引入置信度门控和关系对齐机制。
- 实验效果：在LLaVA和Qwen模型上，INT4量化模型性能超越FP16基线，接近教师模型，并提升吞吐量、减少内存。

## 摘要（原文）

> Vision-Language Models (VLMs) achieve strong multimodal performance but are costly to deploy, and post-training quantization often causes significant accuracy loss. Despite its potential, quantization-aware training for VLMs remains underexplored. We propose GRACE, a framework unifying knowledge distillation and QAT under the Information Bottleneck principle: quantization constrains information capacity while distillation guides what to preserve within this budget. Treating the teacher as a proxy for task-relevant information, we introduce confidence-gated decoupled distillation to filter unreliable supervision, relational centered kernel alignment to transfer visual token structures, and an adaptive controller via Lagrangian relaxation to balance fidelity against capacity constraints. Across extensive benchmarks on LLaVA and Qwen families, our INT4 models consistently outperform FP16 baselines (e.g., LLaVA-1.5-7B: 70.1 vs. 66.8 on SQA; Qwen2-VL-2B: 76.9 vs. 72.6 on MMBench), nearly matching teacher performance. Using real INT4 kernel, we achieve 3$\times$ throughput with 54% memory reduction. This principled framework significantly outperforms existing quantization methods, making GRACE a compelling solution for resource-constrained deployment.

