---
layout: default
title: CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model
---

# CoC-VLA: Delving into Adversarial Domain Transfer for Explainable Autonomous Driving via Chain-of-Causality Visual-Language-Action Model
**arXiv**：[2511.19914v1](https://arxiv.org/abs/2511.19914) · [PDF](https://arxiv.org/pdf/2511.19914.pdf)  
**作者**：Dapeng Zhang, Fei Shen, Rui Zhao, Yinda Chen, Peng Zhi, Chenyang Li, Rui Zhou, Qingguo Zhou  

**一句话要点**：提出CoC-VLA框架，通过对抗域迁移解决自动驾驶长尾场景处理问题

**关键词**：自动驾驶, 对抗域迁移, 视觉语言模型, 长尾场景处理, 链式因果推理

## 3 点简述
- 核心问题：现有方法难以整合仿真与真实世界数据的长尾场景处理优势
- 方法要点：使用教师-学生VLM模型和判别器，实现仿真到真实世界的对抗迁移
- 实验或效果：未知，但框架旨在提升自动驾驶在复杂场景中的推理和可解释性

## 摘要（原文）

> Autonomous driving represents a prominent application of artificial intelligence. Recent approaches have shifted from focusing solely on common scenarios to addressing complex, long-tail situations such as subtle human behaviors, traffic accidents, and non-compliant driving patterns. Given the demonstrated capabilities of large language models (LLMs) in understanding visual and natural language inputs and following instructions, recent methods have integrated LLMs into autonomous driving systems to enhance reasoning, interpretability, and performance across diverse scenarios. However, existing methods typically rely either on real-world data, which is suitable for industrial deployment, or on simulation data tailored to rare or hard case scenarios. Few approaches effectively integrate the complementary advantages of both data sources. To address this limitation, we propose a novel VLM-guided, end-to-end adversarial transfer framework for autonomous driving that transfers long-tail handling capabilities from simulation to real-world deployment, named CoC-VLA. The framework comprises a teacher VLM model, a student VLM model, and a discriminator. Both the teacher and student VLM models utilize a shared base architecture, termed the Chain-of-Causality Visual-Language Model (CoC VLM), which integrates temporal information via an end-to-end text adapter. This architecture supports chain-of-thought reasoning to infer complex driving logic. The teacher and student VLM models are pre-trained separately on simulated and real-world datasets. The discriminator is trained adversarially to facilitate the transfer of long-tail handling capabilities from simulated to real-world environments by the student VLM model, using a novel backpropagation strategy.

