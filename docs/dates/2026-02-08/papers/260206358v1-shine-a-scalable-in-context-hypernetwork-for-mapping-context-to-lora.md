---
layout: default
title: SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass
---

# SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass
**arXiv**：[2602.06358v1](https://arxiv.org/abs/2602.06358) · [PDF](https://arxiv.org/pdf/2602.06358.pdf)  
**作者**：Yewei Liu, Xiyuan Wang, Yansheng Mao, Yoav Gelbery, Haggai Maron, Muhan Zhang  

**一句话要点**：提出SHINE，一种可扩展的上下文超网络，用于单次映射上下文到LoRA适配器。

**关键词**：超网络, LoRA适配器, 上下文学习, 参数高效微调, 大语言模型适应

## 3 点简述
- 核心问题：现有超网络在映射多样上下文到高质量LoRA适配器时存在表达能力和参数效率限制。
- 方法要点：通过重用冻结LLM参数和架构创新，设计上下文超网络，实现单次前向生成适配器。
- 实验或效果：在多种任务上取得优异结果，相比基于SFT的LLM适应节省时间、计算和内存成本。

## 摘要（原文）

> We propose SHINE (Scalable Hyper In-context NEtwork), a scalable hypernetwork that can map diverse meaningful contexts into high-quality LoRA adapters for large language models (LLM). By reusing the frozen LLM's own parameters in an in-context hypernetwork design and introducing architectural innovations, SHINE overcomes key limitations of prior hypernetworks and achieves strong expressive power with a relatively small number of parameters. We introduce a pretraining and instruction fine-tuning pipeline, and train our hypernetwork to generate high quality LoRA adapters from diverse meaningful contexts in a single forward pass. It updates LLM parameters without any fine-tuning, and immediately enables complex question answering tasks related to the context without directly accessing the context, effectively transforming in-context knowledge to in-parameter knowledge in one pass. Our work achieves outstanding results on various tasks, greatly saves time, computation and memory costs compared to SFT-based LLM adaptation, and shows great potential for scaling. Our code is available at https://github.com/Yewei-Liu/SHINE

