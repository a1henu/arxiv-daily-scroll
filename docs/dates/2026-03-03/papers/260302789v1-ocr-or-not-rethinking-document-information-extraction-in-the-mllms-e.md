---
layout: default
title: OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets
---

# OCR or Not? Rethinking Document Information Extraction in the MLLMs Era with Real-World Large-Scale Datasets
**arXiv**：[2603.02789v1](https://arxiv.org/abs/2603.02789) · [PDF](https://arxiv.org/pdf/2603.02789.pdf)  
**作者**：Jiyuan Shen, Peiyue Yuan, Atin Ghosh, Yifan Mai, Daniel Dahlmeier  

**一句话要点**：评估MLLM在文档信息提取中的性能，提出自动化错误分析框架，发现OCR可能非必需。

**关键词**：文档信息提取, 多模态大语言模型, OCR, 错误分析, 基准测试

## 3 点简述
- 核心问题：MLLM在文档信息提取中是否优于传统OCR+MLLM方法，实际影响未知。
- 方法要点：大规模基准测试，提出基于LLM的自动化分层错误分析框架以诊断错误模式。
- 实验或效果：图像输入MLLM性能与OCR增强方法相当，优化提示可提升效果。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) enhance the potential of natural language processing. However, their actual impact on document information extraction remains unclear. In particular, it is unclear whether an MLLM-only pipeline--while simpler--can truly match the performance of traditional OCR+MLLM setups. In this paper, we conduct a large-scale benchmarking study that evaluates various out-of-the-box MLLMs on business-document information extraction. To examine and explore failure modes, we propose an automated hierarchical error analysis framework that leverages large language models (LLMs) to diagnose error patterns systematically. Our findings suggest that OCR may not be necessary for powerful MLLMs, as image-only input can achieve comparable performance to OCR-enhanced approaches. Moreover, we demonstrate that carefully designed schema, exemplars, and instructions can further enhance MLLMs performance. We hope this work can offer practical guidance and valuable insight for advancing document information extraction.

