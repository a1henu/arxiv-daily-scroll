---
layout: default
title: Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection
---

# Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection
**arXiv**：[2512.16300v1](https://arxiv.org/abs/2512.16300) · [PDF](https://arxiv.org/pdf/2512.16300.pdf)  
**作者**：Fanrui Zhang, Qiang Zhang, Sizhuo Zhou, Jianwen Sun, Chuanhao Li, Jiaxin Ai, Yukang Feng, Yujie Zhang, Wenjie Li, Zizhen Li, Yifan Chang, Jiawei Liu, Kaipeng Zhang  

**一句话要点**：提出ForenAgent框架，通过多轮交互与工具使用解决图像伪造检测中高低级信息融合难题。

**关键词**：图像伪造检测, 多模态大语言模型, 工具使用, 动态推理, 强化学习, 数据集构建

## 3 点简述
- 核心问题：现有方法难以统一低级别伪影与高级别语义知识，导致检测效果受限。
- 方法要点：设计动态推理循环，结合冷启动与强化微调训练，使MLLM自主生成和执行Python工具。
- 实验或效果：在FABench数据集上验证，ForenAgent展现工具使用能力和反思推理，提升检测性能。

## 摘要（原文）

> Existing image forgery detection (IFD) methods either exploit low-level, semantics-agnostic artifacts or rely on multimodal large language models (MLLMs) with high-level semantic knowledge. Although naturally complementary, these two information streams are highly heterogeneous in both paradigm and reasoning, making it difficult for existing methods to unify them or effectively model their cross-level interactions. To address this gap, we propose ForenAgent, a multi-round interactive IFD framework that enables MLLMs to autonomously generate, execute, and iteratively refine Python-based low-level tools around the detection objective, thereby achieving more flexible and interpretable forgery analysis. ForenAgent follows a two-stage training pipeline combining Cold Start and Reinforcement Fine-Tuning to enhance its tool interaction capability and reasoning adaptability progressively. Inspired by human reasoning, we design a dynamic reasoning loop comprising global perception, local focusing, iterative probing, and holistic adjudication, and instantiate it as both a data-sampling strategy and a task-aligned process reward. For systematic training and evaluation, we construct FABench, a heterogeneous, high-quality agent-forensics dataset comprising 100k images and approximately 200k agent-interaction question-answer pairs. Experiments show that ForenAgent exhibits emergent tool-use competence and reflective reasoning on challenging IFD tasks when assisted by low-level tools, charting a promising route toward general-purpose IFD. The code will be released after the review process is completed.

