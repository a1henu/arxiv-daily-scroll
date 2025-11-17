---
layout: default
title: WEAVE: Unleashing and Benchmarking the In-context Interleaved Comprehension and Generation
---

# WEAVE: Unleashing and Benchmarking the In-context Interleaved Comprehension and Generation
**arXiv**：[2511.11434v1](https://arxiv.org/abs/2511.11434) · [PDF](https://arxiv.org/pdf/2511.11434.pdf)  
**作者**：Wei Chow, Jiachun Pan, Yongyuan Liang, Mingze Zhou, Xue Song, Liyu Jia, Saining Zhang, Siliang Tang, Juncheng Li, Fengda Zhang, Weijia Wu, Hanwang Zhang, Tat-Seng Chua  

**一句话要点**：提出WEAVE套件以解决多模态模型中多轮上下文理解与生成的基准缺失问题

**关键词**：多模态模型, 多轮对话, 图像生成, 视觉记忆, 基准评估, 上下文理解

## 3 点简述
- 现有数据集聚焦单轮交互，无法捕捉真实世界图像创作的多轮上下文依赖
- 构建WEAVE-100k大规模数据集和WEAVEBench基准，支持多轮理解、编辑和生成任务
- 实验显示训练提升模型视觉记忆和生成能力，但多轮上下文感知仍存挑战

## 摘要（原文）

> Recent advances in unified multimodal models (UMMs) have enabled impressive progress in visual comprehension and generation. However, existing datasets and benchmarks focus primarily on single-turn interactions, failing to capture the multi-turn, context-dependent nature of real-world image creation and editing. To address this gap, we present WEAVE, the first suite for in-context interleaved cross-modality comprehension and generation. Our suite consists of two complementary parts. WEAVE-100k is a large-scale dataset of 100K interleaved samples spanning over 370K dialogue turns and 500K images, covering comprehension, editing, and generation tasks that require reasoning over historical context. WEAVEBench is a human-annotated benchmark with 100 tasks based on 480 images, featuring a hybrid VLM judger evaluation framework based on both the reference image and the combination of the original image with editing instructions that assesses models' abilities in multi-turn generation, visual memory, and world-knowledge reasoning across diverse domains. Experiments demonstrate that training on WEAVE-100k enables vision comprehension, image editing, and comprehension-generation collaboration capabilities. Furthermore, it facilitates UMMs to develop emergent visual-memory capabilities, while extensive evaluations on WEAVEBench expose the persistent limitations and challenges of current approaches in multi-turn, context-aware image generation and editing. We believe WEAVE provides a view and foundation for studying in-context interleaved comprehension and generation for multi-modal community.

