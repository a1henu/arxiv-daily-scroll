---
layout: default
title: VTimeCoT: Thinking by Drawing for Video Temporal Grounding and Reasoning
---

# VTimeCoT: Thinking by Drawing for Video Temporal Grounding and Reasoning
**arXiv**：[2510.14672v1](https://arxiv.org/abs/2510.14672) · [PDF](https://arxiv.org/pdf/2510.14672.pdf)  
**作者**：Jinglei Zhang, Yuanfan Guo, Rolandos Alexandros Potamias, Jiankang Deng, Hang Xu, Chao Ma  

**一句话要点**：提出VTimeCoT框架以解决视频时序定位与推理问题

**关键词**：视频时序定位, 多模态推理, 进度条工具, 链式思维, 视频问答, 零训练框架

## 3 点简述
- 多模态大语言模型在视频时序定位与推理方面存在不足
- 引入进度条工具和视觉时序链式思维过程，无需训练
- 在Qwen2VL-7B和GPT4o基准上性能显著提升，推理过程可解释

## 摘要（原文）

> In recent years, video question answering based on multimodal large language
> models (MLLM) has garnered considerable attention, due to the benefits from the
> substantial advancements in LLMs. However, these models have a notable
> deficiency in the domains of video temporal grounding and reasoning, posing
> challenges to the development of effective real-world video understanding
> systems. Inspired by how humans use video players to interact with the progress
> bar for video comprehension, we introduce VTimeCoT, a simple yet effective
> training-free framework, designed for high-performance video grounding and
> reasoning. The proposed framework incorporates two novel visual tools of the
> progress bar: a plug-and-play progress bar integration tool and a
> high-efficiency highlighting tool. In addition, to address the limitations of
> conventional text-based chain-of-thought (CoT) approaches, we introduce a
> visuotemporal CoT process that integrates cross-modality reasoning across both
> video and text. Our approach demonstrates significant performance improvements
> on both Qwen2VL-7B and GPT4o baselines in tasks of video temporal grounding and
> reasoning-based question answering. Finally, we showcase that the proposed
> framework achieves a compositional and interpretable reasoning process. Project
> page: https://vtimecot.github.io

