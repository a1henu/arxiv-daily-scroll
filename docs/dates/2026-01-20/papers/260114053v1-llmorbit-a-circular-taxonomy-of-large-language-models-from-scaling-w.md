---
layout: default
title: LLMOrbit: A Circular Taxonomy of Large Language Models -From Scaling Walls to Agentic AI Systems
---

# LLMOrbit: A Circular Taxonomy of Large Language Models -From Scaling Walls to Agentic AI Systems
**arXiv**：[2601.14053v1](https://arxiv.org/abs/2601.14053) · [PDF](https://arxiv.org/pdf/2601.14053.pdf)  
**作者**：Badri N. Patro, Vijay S. Agneeswaran  

**一句话要点**：提出LLMOrbit循环分类法，系统梳理大语言模型发展并分析规模化瓶颈与突破范式

**关键词**：大语言模型分类法, 规模化瓶颈分析, 模型效率优化, 后训练技术, 智能体系统, 开源模型发展

## 3 点简述
- 核心问题：识别数据枯竭、成本激增、能耗剧增三大危机构成的规模化壁垒
- 方法要点：通过八维轨道框架分析50余个模型，涵盖架构创新与训练方法
- 实验或效果：总结测试时计算、量化压缩等六种突破壁垒的范式与三大范式转变

## 摘要（原文）

> The field of artificial intelligence has undergone a revolution from foundational Transformer architectures to reasoning-capable systems approaching human-level performance. We present LLMOrbit, a comprehensive circular taxonomy navigating the landscape of large language models spanning 2019-2025. This survey examines over 50 models across 15 organizations through eight interconnected orbital dimensions, documenting architectural innovations, training methodologies, and efficiency patterns defining modern LLMs, generative AI, and agentic systems. We identify three critical crises: (1) data scarcity (9-27T tokens depleted by 2026-2028), (2) exponential cost growth ($3M to $300M+ in 5 years), and (3) unsustainable energy consumption (22x increase), establishing the scaling wall limiting brute-force approaches. Our analysis reveals six paradigms breaking this wall: (1) test-time compute (o1, DeepSeek-R1 achieve GPT-4 performance with 10x inference compute), (2) quantization (4-8x compression), (3) distributed edge computing (10x cost reduction), (4) model merging, (5) efficient training (ORPO reduces memory 50%), and (6) small specialized models (Phi-4 14B matches larger models). Three paradigm shifts emerge: (1) post-training gains (RLHF, GRPO, pure RL contribute substantially, DeepSeek-R1 achieving 79.8% MATH), (2) efficiency revolution (MoE routing 18x efficiency, Multi-head Latent Attention 8x KV cache compression enables GPT-4-level performance at <$0.30/M tokens), and (3) democratization (open-source Llama 3 88.6% MMLU surpasses GPT-4 86.4%). We provide insights into techniques (RLHF, PPO, DPO, GRPO, ORPO), trace evolution from passive generation to tool-using agents (ReAct, RAG, multi-agent systems), and analyze post-training innovations.

