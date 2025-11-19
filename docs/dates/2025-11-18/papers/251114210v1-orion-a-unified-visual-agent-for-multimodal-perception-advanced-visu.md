---
layout: default
title: Orion: A Unified Visual Agent for Multimodal Perception, Advanced Visual Reasoning and Execution
---

# Orion: A Unified Visual Agent for Multimodal Perception, Advanced Visual Reasoning and Execution
**arXiv**：[2511.14210v1](https://arxiv.org/abs/2511.14210) · [PDF](https://arxiv.org/pdf/2511.14210.pdf)  
**作者**：N Dinesh Reddy, Sudeep Pillai  

**一句话要点**：提出Orion视觉代理框架，通过工具调用实现多模态感知与推理，解决复杂视觉任务。

**关键词**：视觉代理框架, 多模态感知, 工具调用, 视觉推理, 符号执行, 生产级智能

## 3 点简述
- 核心问题：传统视觉语言模型仅生成描述性输出，难以执行多步骤视觉工作流。
- 方法要点：结合神经感知与符号执行，调用对象检测、OCR等工具进行自主推理。
- 实验或效果：在MMMU、MMBench等基准上达到竞争性性能，扩展至生产级视觉智能。

## 摘要（原文）

> We introduce Orion, a visual agent framework that can take in any modality and generate any modality. Using an agentic framework with multiple tool-calling capabilities, Orion is designed for visual AI tasks and achieves state-of-the-art results. Unlike traditional vision-language models that produce descriptive outputs, Orion orchestrates a suite of specialized computer vision tools, including object detection, keypoint localization, panoptic segmentation, Optical Character Recognition, and geometric analysis, to execute complex multi-step visual workflows. The system achieves competitive performance on MMMU, MMBench, DocVQA, and MMLongBench while extending monolithic vision-language models to production-grade visual intelligence. By combining neural perception with symbolic execution, Orion enables autonomous visual reasoning, marking a transition from passive visual understanding to active, tool-driven visual intelligence.

