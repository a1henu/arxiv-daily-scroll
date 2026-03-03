---
layout: default
title: CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework
---

# CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework
**arXiv**：[2603.01607v1](https://arxiv.org/abs/2603.01607) · [PDF](https://arxiv.org/pdf/2603.01607.pdf)  
**作者**：Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu  

**一句话要点**：提出CARE框架以提升多模态医疗推理的临床可问责性，通过证据驱动的代理架构模拟临床工作流。

**关键词**：多模态医疗推理, 临床可问责性, 证据驱动框架, 代理架构, 视觉语言模型, 强化学习

## 3 点简述
- 核心问题：现有视觉语言模型作为黑箱运行，偏离临床证据化、分阶段工作流，影响可问责性。
- 方法要点：分解任务为协调子模块，包括实体提议、分割证据和基于证据的推理，结合强化学习和代理协调器。
- 实验或效果：在标准医疗VQA基准上，CARE-Flow提升准确率10.9%，CARE-Coord进一步增益5.2%，超越SOTA。

## 摘要（原文）

> Large visual language models (VLMs) have shown strong multi-modal medical reasoning ability, but most operate as end-to-end black boxes, diverging from clinicians' evidence-based, staged workflows and hindering clinical accountability. Complementarily, expert visual grounding models can accurately localize regions of interest (ROIs), providing explicit, reliable evidence that improves both reasoning accuracy and trust. In this paper, we introduce CARE, advancing Clinical Accountability in multi-modal medical Reasoning with an Evidence-grounded agentic framework. Unlike existing approaches that couple grounding and reasoning within a single generalist model, CARE decomposes the task into coordinated sub-modules to reduce shortcut learning and hallucination: a compact VLM proposes relevant medical entities; an expert entity-referring segmentation model produces pixel-level ROI evidence; and a grounded VLM reasons over the full image augmented by ROI hints. The VLMs are optimized with reinforcement learning with verifiable rewards to align answers with supporting evidence. Furthermore, a VLM coordinator plans tool invocation and reviews evidence-answer consistency, providing agentic control and final verification. Evaluated on standard medical VQA benchmarks, our CARE-Flow (coordinator-free) improves average accuracy by 10.9% over the same size (10B) state-of-the-art (SOTA). With dynamic planning and answer review, our CARE-Coord yields a further gain, outperforming the heavily pre-trained SOTA by 5.2%. Our experiments demonstrate that an agentic framework that emulates clinical workflows, incorporating decoupled specialized models and explicit evidence, yields more accurate and accountable medical AI.

