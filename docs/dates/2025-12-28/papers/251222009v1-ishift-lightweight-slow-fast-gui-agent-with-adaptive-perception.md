---
layout: default
title: iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception
---

# iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception
**arXiv**：[2512.22009v1](https://arxiv.org/abs/2512.22009) · [PDF](https://arxiv.org/pdf/2512.22009.pdf)  
**作者**：Sarthak Mehrotra, Sairam V C Rebbapragada, Mani Hemanth Reddy Bonthu, Vineeth N Balasubramanian  

**一句话要点**：提出iSHIFT轻量级GUI代理，通过自适应感知解决多模态大模型在界面交互中效率与精度平衡的挑战。

**关键词**：多模态大语言模型, 图形用户界面代理, 自适应感知, 隐式思维链, 慢快推理, 视觉定位

## 3 点简述
- 核心问题：现有GUI代理难以同时高效执行常规任务和精确处理需要视觉定位的细粒度交互。
- 方法要点：集成隐式思维链与感知控制模块，通过慢快模式切换和感知令牌实现自适应推理与注意力引导。
- 实验或效果：在2.5B紧凑规模下，iSHIFT在多个基准数据集上达到最先进性能。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) show strong potential for interpreting and interacting with complex, pixel-rich Graphical User Interface (GUI) environments. However, building agents that are both efficient for high-level tasks and precise for fine-grained interactions remains challenging. GUI agents must perform routine actions efficiently while also handling tasks that demand exact visual grounding, yet existing approaches struggle when accuracy depends on identifying specific interface elements. These MLLMs also remain large and cannot adapt their reasoning depth to the task at hand. In this work, we introduce iSHIFT: Implicit Slow-fast Hybrid Inference with Flexible Tokens, a lightweight agent that integrates latent thinking (implicit chain-of-thought) with a perception control module. iSHIFT enables an MLLM to switch between a slow mode, which leverages detailed visual grounding for high precision and a fast mode that uses global cues for efficiency. Special perception tokens guide attention to relevant screen regions, allowing the model to decide both how to reason and where to focus. Despite its compact 2.5B size, iSHIFT matches state-of-the-art performance on multiple benchmark datasets.

