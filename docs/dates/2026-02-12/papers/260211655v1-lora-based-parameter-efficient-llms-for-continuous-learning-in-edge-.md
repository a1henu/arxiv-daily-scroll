---
layout: default
title: LoRA-based Parameter-Efficient LLMs for Continuous Learning in Edge-based Malware Detection
---

# LoRA-based Parameter-Efficient LLMs for Continuous Learning in Edge-based Malware Detection
**arXiv**：[2602.11655v1](https://arxiv.org/abs/2602.11655) · [PDF](https://arxiv.org/pdf/2602.11655.pdf)  
**作者**：Christian Rondanini, Barbara Carminati, Elena Ferrari, Niccolò Lardo, Ashish Kundu  

**一句话要点**：提出基于LoRA的参数高效LLM架构，用于边缘设备恶意软件检测的持续学习

**关键词**：边缘计算, 恶意软件检测, 持续学习, LoRA适配器, 参数高效微调, IoT安全

## 3 点简述
- 边缘设备恶意软件检测面临资源限制和威胁演化挑战，静态或孤立模型效果不佳
- 采用LoRA适配器实现本地微调与全局知识共享，仅交换轻量参数模块以提升泛化能力
- 在公开IoT数据集上评估，LoRA交换使跨域攻击检测准确率提升20-25%，模型增量小于1%

## 摘要（原文）

> The proliferation of edge devices has created an urgent need for security solutions capable of detecting malware in real time while operating under strict computational and memory constraints. Recently, Large Language Models (LLMs) have demonstrated remarkable capabilities in recognizing complex patterns, yet their deployment on edge devices remains impractical due to their resource demands. However, in edge malware detection, static or centrally retrained models degrade under evolving threats and heterogeneous traffic; locally trained models become siloed and fail to transfer across domains. To overcome these limitations, in this paper, we present a continuous learning architecture for edge-based malware detection that combines local adaptation on each device with global knowledge sharing through parameter-efficient LoRA adapters. Lightweight transformer models (DistilBERT, DistilGPT-2, TinyT5) run on edge nodes and are incrementally fine-tuned on device-specific traffic; only the resulting LoRA modules are aggregated by a lightweight coordinator and redistributed, enabling cross-device generalization without exchanging raw data. We evaluate on two public IoT security datasets, Edge-IIoTset and TON-IoT, under multi-round learning to simulate evolving threats. Compared to isolated fine-tuning, the LoRA-based exchange yields up to 20-25% accuracy gains when models encounter previously unseen attacks from another domain, while maintaining stable loss and F1 across rounds. LoRA adds less than 1% to model size (~0.6-1.8 MB), making updates practical for constrained edge hardware.

