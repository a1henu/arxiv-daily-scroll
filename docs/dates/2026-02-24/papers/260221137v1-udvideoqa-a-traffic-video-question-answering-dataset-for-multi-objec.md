---
layout: default
title: UDVideoQA: A Traffic Video Question Answering Dataset for Multi-Object Spatio-Temporal Reasoning in Urban Dynamics
---

# UDVideoQA: A Traffic Video Question Answering Dataset for Multi-Object Spatio-Temporal Reasoning in Urban Dynamics
**arXiv**：[2602.21137v1](https://arxiv.org/abs/2602.21137) · [PDF](https://arxiv.org/pdf/2602.21137.pdf)  
**作者**：Joseph Raj Vishal, Nagasiri Poluri, Katha Naik, Rutuja Patil, Kashyap Hegde Kota, Krishna Vinod, Prithvi Jai Ramesh, Mohammad Farhadi, Yezhou Yang, Bharatesh Chakravarthi  

**一句话要点**：提出UDVideoQA数据集以解决城市交通视频中多目标时空推理的挑战

**关键词**：视频问答数据集, 城市交通动态, 时空推理, 隐私保护, 视觉语言模型, 基准测试

## 3 点简述
- 核心问题：理解城市交通多智能体动态是视频语言模型的基础挑战，需系统评估视觉定位与因果推理
- 方法要点：基于16小时真实交通视频，采用事件驱动动态模糊技术保护隐私，通过统一标注流程生成28K问答对
- 实验或效果：基准测试显示感知-推理差距，微调Qwen2.5-VL 7B可媲美专有系统，VideoQGen中模型生成问题相关但语言多样性有限

## 摘要（原文）

> Understanding the complex, multi-agent dynamics of urban traffic remains a fundamental challenge for video language models. This paper introduces Urban Dynamics VideoQA, a benchmark dataset that captures the unscripted real-world behavior of dynamic urban scenes. UDVideoQA is curated from 16 hours of traffic footage recorded at multiple city intersections under diverse traffic, weather, and lighting conditions. It employs an event-driven dynamic blur technique to ensure privacy preservation without compromising scene fidelity. Using a unified annotation pipeline, the dataset contains 28K question-answer pairs generated across 8 hours of densely annotated video, averaging one question per second. Its taxonomy follows a hierarchical reasoning level, spanning basic understanding and attribution to event reasoning, reverse reasoning, and counterfactual inference, enabling systematic evaluation of both visual grounding and causal reasoning. Comprehensive experiments benchmark 10 SOTA VideoLMs on UDVideoQA and 8 models on a complementary video question generation benchmark. Results reveal a persistent perception-reasoning gap, showing models that excel in abstract inference often fail with fundamental visual grounding. While models like Gemini Pro achieve the highest zero-shot accuracy, fine-tuning the smaller Qwen2.5-VL 7B model on UDVideoQA bridges this gap, achieving performance comparable to proprietary systems. In VideoQGen, Gemini 2.5 Pro, and Qwen3 Max generate the most relevant and complex questions, though all models exhibit limited linguistic diversity, underscoring the need for human-centric evaluation. The UDVideoQA suite, including the dataset, annotation tools, and benchmarks for both VideoQA and VideoQGen, provides a foundation for advancing robust, privacy-aware, and real-world multimodal reasoning. UDVideoQA is available at https://ud-videoqa.github.io/UD-VideoQA/UD-VideoQA/.

