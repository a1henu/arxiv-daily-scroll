---
layout: default
title: ThinkGen: Generalized Thinking for Visual Generation
---

# ThinkGen: Generalized Thinking for Visual Generation
**arXiv**：[2512.23568v1](https://arxiv.org/abs/2512.23568) · [PDF](https://arxiv.org/pdf/2512.23568.pdf)  
**作者**：Siyu Jiao, Yiheng Lin, Yujie Zhong, Qi She, Wei Zhou, Xiaohan Lan, Zilong Huang, Fei Yu, Yingchen Yu, Yunqing Zhao, Yao Zhao, Yunchao Wei  

**一句话要点**：提出ThinkGen框架，利用MLLM的思维链推理实现通用视觉生成

**关键词**：视觉生成, 思维链推理, 多模态大语言模型, 扩散变换器, 强化学习

## 3 点简述
- 核心问题：思维链推理在生成任务中扩展受限，缺乏通用性
- 方法要点：采用解耦架构，MLLM生成指令，DiT生成图像，结合SepGRPO训练
- 实验或效果：在多个生成基准上实现稳健的先进性能

## 摘要（原文）

> Recent progress in Multimodal Large Language Models (MLLMs) demonstrates that Chain-of-Thought (CoT) reasoning enables systematic solutions to complex understanding tasks. However, its extension to generation tasks remains nascent and limited by scenario-specific mechanisms that hinder generalization and adaptation. In this work, we present ThinkGen, the first think-driven visual generation framework that explicitly leverages MLLM's CoT reasoning in various generation scenarios. ThinkGen employs a decoupled architecture comprising a pretrained MLLM and a Diffusion Transformer (DiT), wherein the MLLM generates tailored instructions based on user intent, and DiT produces high-quality images guided by these instructions. We further propose a separable GRPO-based training paradigm (SepGRPO), alternating reinforcement learning between the MLLM and DiT modules. This flexible design enables joint training across diverse datasets, facilitating effective CoT reasoning for a wide range of generative scenarios. Extensive experiments demonstrate that ThinkGen achieves robust, state-of-the-art performance across multiple generation benchmarks. Code is available: https://github.com/jiaosiyuu/ThinkGen

