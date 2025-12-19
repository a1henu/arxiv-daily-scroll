---
layout: default
title: TOGGLE: Temporal Logic-Guided Large Language Model Compression for Edge
---

# TOGGLE: Temporal Logic-Guided Large Language Model Compression for Edge
**arXiv**：[2512.16855v1](https://arxiv.org/abs/2512.16855) · [PDF](https://arxiv.org/pdf/2512.16855.pdf)  
**作者**：Khurram Khalil, Khaza Anuarul Hoque  

**一句话要点**：提出TOGGLE框架，利用时序逻辑指导大语言模型压缩，以在边缘设备上实现高效可验证部署。

**关键词**：大语言模型压缩, 时序逻辑指导, 边缘计算部署, 形式化方法, 贝叶斯优化

## 3 点简述
- 现有压缩技术如量化和剪枝常损害语言属性且缺乏形式化保证，限制大语言模型在资源受限边缘设备的部署。
- TOGGLE采用信号时序逻辑形式化指定语言属性，并通过稳健性引导的贝叶斯优化系统探索层间压缩配置，无需重训练或微调。
- 在四种大语言模型架构上评估，TOGGLE实现计算成本最高3.3倍降低和模型大小最高68.8%减少，同时满足所有语言属性。

## 摘要（原文）

> Large Language Models (LLMs) deliver exceptional performance across natural language tasks but demand substantial computational resources, limiting their deployment on resource-constrained edge devices. Existing compression techniques, such as quantization and pruning, often degrade critical linguistic properties and lack formal guarantees for preserving model behavior. We propose Temporal Logic-Guided Large Language Model Compression (TOGGLE), a novel framework that leverages Signal Temporal Logic (STL) to formally specify and enforce linguistic properties during compression. TOGGLE employs an STL robustness-guided Bayesian optimization to systematically explore layer-wise quantization and pruning configurations, generating compressed models that formally satisfy specified linguistic constraints without retraining or fine-tuning. Evaluating TOGGLE on four LLM architectures (GPT-2, DeepSeek-V2 7B, LLaMA 3 8B, and Mistral 7B), we achieve up to 3.3x reduction in computational costs (FLOPs) and up to a 68.8% reduction in model size while satisfying all linguistic properties. TOGGLE represents the first integration of formal methods into LLM compression, enabling efficient, verifiable deployment of LLMs on edge hardware.

