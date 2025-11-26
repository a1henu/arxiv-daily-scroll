---
layout: default
title: VICoT-Agent: A Vision-Interleaved Chain-of-Thought Framework for Interpretable Multimodal Reasoning and Scalable Remote Sensing Analysis
---

# VICoT-Agent: A Vision-Interleaved Chain-of-Thought Framework for Interpretable Multimodal Reasoning and Scalable Remote Sensing Analysis
**arXiv**：[2511.20085v1](https://arxiv.org/abs/2511.20085) · [PDF](https://arxiv.org/pdf/2511.20085.pdf)  
**作者**：Chujie Wang, Zhiyuan Luo, Ruiqi Liu, Can Ran, Shenghua Fan, Xi Chen, Chu He  

**一句话要点**：提出VICoT框架以解决遥感图像复杂推理任务

**关键词**：多模态推理, 遥感图像分析, 链式思维, 工具调用, 蒸馏训练

## 3 点简述
- 遥感分析从对象识别转向复杂推理，需模型推理能力和工具调用灵活性
- VICoT通过堆栈推理结构和模块化工具，实现多轮视觉语言推理
- 在多个基准测试中，VICoT在透明度、效率和生成质量上优于现有方法

## 摘要（原文）

> The current remote sensing image analysis task is increasingly evolving from traditional object recognition to complex intelligence reasoning, which places higher requirements on the model's reasoning ability and the flexibility of tool invocation. To this end, we propose a new multimodal agent framework, Vision-Interleaved Chain-of-Thought Framework (VICoT), which implements explicit multi-round reasoning by dynamically incorporating visual tools into the chain of thought. Through a stack-based reasoning structure and a modular MCP-compatible tool suite, VICoT enables LLMs to efficiently perform multi-round, interleaved vision-language reasoning tasks with strong generalization and flexibility.We also propose the Reasoning Stack distillation method to migrate complex Agent behaviors to small, lightweight models, which ensures the reasoning capability while significantly reducing complexity. Experiments on multiple remote sensing benchmarks demonstrate that VICoT significantly outperforms existing SOTA frameworks in reasoning transparency, execution efficiency, and generation quality.

