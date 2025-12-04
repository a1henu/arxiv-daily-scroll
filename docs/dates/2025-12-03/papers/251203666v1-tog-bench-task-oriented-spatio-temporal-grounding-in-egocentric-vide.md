---
layout: default
title: ToG-Bench: Task-Oriented Spatio-Temporal Grounding in Egocentric Videos
---

# ToG-Bench: Task-Oriented Spatio-Temporal Grounding in Egocentric Videos
**arXiv**：[2512.03666v1](https://arxiv.org/abs/2512.03666) · [PDF](https://arxiv.org/pdf/2512.03666.pdf)  
**作者**：Qi'ao Xu, Tianwen Qian, Yuqian Fu, Kailing Li, Yang Jiao, Jiacheng Zhang, Xiaoling Wang, Liang He  

**一句话要点**：提出ToG-Bench基准以解决第一人称视频中任务导向的时空定位问题。

**关键词**：时空视频定位, 任务导向基准, 第一人称视频, 多模态大模型评估, 显隐对象推理

## 3 点简述
- 核心问题：现有时空视频定位研究局限于对象中心描述，缺乏任务导向推理，阻碍具身智能交互。
- 方法要点：构建首个任务导向时空定位基准，包含任务导向、显隐双重和一对多定位特征，基于ScanNet视频半自动标注。
- 实验或效果：评估七种先进多模态大模型，揭示任务导向时空定位的挑战及显隐与多对象定位性能差距。

## 摘要（原文）

> A core capability towards general embodied intelligence lies in localizing task-relevant objects from an egocentric perspective, formulated as Spatio-Temporal Video Grounding (STVG). Despite recent progress, existing STVG studies remain largely confined to object-centric and descriptive instructions, neglecting the task-oriented reasoning that is crucial for embodied agents to accomplish goal-directed interactions. To bridge this gap, we introduce \textbf{ToG-Bench}, the first task-oriented spatio-temporal video grounding benchmark for egocentric videos. ToG-Bench is characterized by three key features: (1) \textbf{Task-oriented Grounding}, which requires identifying and localizing objects based on intended tasks rather than straightforward descriptions; (2) \textbf{Explicit-Implicit Dual Grounding}, where target objects can be either explicitly mentioned or implicitly inferred by contextual reasoning; (3) \textbf{One-to-Many Grounding}, where a single instruction may correspond to multiple objects involved in task execution. Built upon videos sourced from ScanNet, ToG-Bench comprises 100 annotated clips with 2,704 task-oriented grounding instructions, constructed via a semi-automated pipeline that combines foundation model annotation and human refinement. In addition, we introduce a set of task-level evaluation metrics tailored for multi-object and explicit-implicit object grounding, and systematically benchmark seven state-of-the-art MLLMs. Extensive experiments reveal the intrinsic challenges of task-oriented STVG and substantial performance gaps across explicit-implicit and multi-object grounding, highlighting the difficulty of bridging perception and interaction in embodied scenarios. Data and code will be released at: \href{https://github.com/qaxuDev/ToG-Bench}{https://github.com/qaxuDev/ToG-Bench}..

