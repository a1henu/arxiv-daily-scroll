---
layout: default
title: MobileFineTuner: A Unified End-to-End Framework for Fine-Tuning LLMs on Mobile Phones
---

# MobileFineTuner: A Unified End-to-End Framework for Fine-Tuning LLMs on Mobile Phones
**arXiv**：[2512.08211v1](https://arxiv.org/abs/2512.08211) · [PDF](https://arxiv.org/pdf/2512.08211.pdf)  
**作者**：Jiaxiang Geng, Lunyu Zhao, Yiyi Lu, Bing Luo  

**一句话要点**：提出MobileFineTuner框架以在移动设备上实现端到端大语言模型微调

**关键词**：移动设备微调, 大语言模型, 参数高效微调, 系统优化, 隐私保护, 开源框架

## 3 点简述
- 核心问题：移动设备缺乏开源框架支持大语言模型微调，现有方法多基于模拟或非移动设备
- 方法要点：引入参数分片、梯度累积和能量感知调度等系统级优化，支持全参数和参数高效微调
- 实验或效果：在真实手机上微调GPT-2、Gemma 3和Qwen 2.5，验证优化有效性并确立框架可行性

## 摘要（原文）

> Mobile phones are the most ubiquitous end devices, generating vast amounts of human-authored data and serving as the primary platform for end-side applications. As high-quality public data for large language models (LLMs) approaches exhaustion, on-device fine-tuning provides an opportunity to leverage private user data while preserving privacy. However, existing approaches are predominantly simulation-based or rely on IoT devices and PCs, leaving commodity mobile phones largely unexplored. A key gap is the absence of an open-source framework that enables practical LLM fine-tuning on mobile phones. We present MobileFineTuner, a unified open-source framework that enables end-to-end LLM fine-tuning directly on commodity mobile phones. MobileFineTuner is designed for efficiency, scalability, and usability, supporting full-parameters fine-tuning (Full-FT) and parameter-efficient fine-tuning (PEFT). To address the memory and energy limitations inherent to mobile phones, we introduce system-level optimizations including parameter sharding, gradient accumulation, and energy-aware computation scheduling. We demonstrate the practicality of MobileFineTuner by fine-tuning GPT-2, Gemma 3, and Qwen 2.5 on real mobile phones. Extensive experiments and ablation studies validate the effectiveness of the proposed optimizations and establish MobileFineTuner as a viable foundation for future research on on-device LLM training.

