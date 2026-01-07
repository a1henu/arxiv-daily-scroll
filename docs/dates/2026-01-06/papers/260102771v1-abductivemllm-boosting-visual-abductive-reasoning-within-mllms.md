---
layout: default
title: AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs
---

# AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs
**arXiv**：[2601.02771v1](https://arxiv.org/abs/2601.02771) · [PDF](https://arxiv.org/pdf/2601.02771.pdf)  
**作者**：Boyu Chang, Qi Wang, Xi Guo, Zhixiong Nan, Yazhou Yao, Tianfei Zhou  

**一句话要点**：提出AbductiveMLLM以增强多模态大语言模型的视觉溯因推理能力

**关键词**：视觉溯因推理, 多模态大语言模型, 因果对齐, 文本到图像扩散模型, 端到端训练

## 3 点简述
- 核心问题：现有MLLMs在视觉溯因推理上表现不足，需提升因果推断能力
- 方法要点：结合REASONER进行语言域假设筛选和IMAGINER进行视觉想象，模拟人类双模态推理
- 实验或效果：在标准VAR基准测试中实现最优性能，超越传统方法和先进MLLMs

## 摘要（原文）

> Visual abductive reasoning (VAR) is a challenging task that requires AI systems to infer the most likely explanation for incomplete visual observations. While recent MLLMs develop strong general-purpose multimodal reasoning capabilities, they fall short in abductive inference, as compared to human beings. To bridge this gap, we draw inspiration from the interplay between verbal and pictorial abduction in human cognition, and propose to strengthen abduction of MLLMs by mimicking such dual-mode behavior. Concretely, we introduce AbductiveMLLM comprising of two synergistic components: REASONER and IMAGINER. The REASONER operates in the verbal domain. It first explores a broad space of possible explanations using a blind LLM and then prunes visually incongruent hypotheses based on cross-modal causal alignment. The remaining hypotheses are introduced into the MLLM as targeted priors, steering its reasoning toward causally coherent explanations. The IMAGINER, on the other hand, further guides MLLMs by emulating human-like pictorial thinking. It conditions a text-to-image diffusion model on both the input video and the REASONER's output embeddings to "imagine" plausible visual scenes that correspond to verbal explanation, thereby enriching MLLMs' contextual grounding. The two components are trained jointly in an end-to-end manner. Experiments on standard VAR benchmarks show that AbductiveMLLM achieves state-of-the-art performance, consistently outperforming traditional solutions and advanced MLLMs.

