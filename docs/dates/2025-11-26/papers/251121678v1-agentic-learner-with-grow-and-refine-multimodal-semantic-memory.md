---
layout: default
title: Agentic Learner with Grow-and-Refine Multimodal Semantic Memory
---

# Agentic Learner with Grow-and-Refine Multimodal Semantic Memory
**arXiv**：[2511.21678v1](https://arxiv.org/abs/2511.21678) · [PDF](https://arxiv.org/pdf/2511.21678.pdf)  
**作者**：Weihao Bo, Shan Zhang, Yanpeng Sun, Jingjing Wu, Qunyi Xie, Xiao Tan, Kunbin Chen, Wei He, Xiaofan Li, Na Zhao, Jingdong Wang, Zechao Li  

**一句话要点**：提出ViLoMem双流记忆框架以解决多模态代理重复错误问题

**关键词**：多模态语义记忆, 双流记忆框架, 代理学习, 视觉分心模式, 逻辑推理错误, 增长式更新

## 3 点简述
- 多模态大模型独立处理查询，重复视觉和逻辑错误，缺乏多模态语义记忆
- 采用双流记忆分别编码视觉分心模式和逻辑推理错误，支持增长式更新
- 在六个多模态基准上提升准确率，减少重复错误，验证双流必要性

## 摘要（原文）

> MLLMs exhibit strong reasoning on isolated queries, yet they operate de novo -- solving each problem independently and often repeating the same mistakes. Existing memory-augmented agents mainly store past trajectories for reuse. However, trajectory-based memory suffers from brevity bias, gradually losing essential domain knowledge. More critically, even in truly multimodal problem-solving settings, it records only a single-modality trace of past behavior, failing to preserve how visual attention and logical reasoning jointly contributed to the solution. This is fundamentally misaligned with human cognition: semantic memory is both multimodal and integrated, preserving visual and abstract knowledge through coordinated but distinct representational streams. We thus introduce ViLoMem, a dual-stream memory framework that constructs compact, schema-based memory. It separately encodes visual distraction patterns and logical reasoning errors, enabling MLLMs to learn from their successful and failed experiences. Following a grow-and-refine principle, the system incrementally accumulates and updates multimodal semantic knowledge -- preserving stable, generalizable strategies while avoiding catastrophic forgetting. Across six multimodal benchmarks, ViLoMem consistently improves pass@1 accuracy and substantially reduces repeated visual and logical errors. Ablations confirm the necessity of dual-stream memory with explicit distraction--hallucination separation, demonstrating the value of error-aware multimodal memory for lifelong and cross-domain agentic learning. Our project page will be available at https://weihao-bo.github.io/ViLoMeo-page.

