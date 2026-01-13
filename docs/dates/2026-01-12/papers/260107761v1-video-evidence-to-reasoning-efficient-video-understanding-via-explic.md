---
layout: default
title: Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding
---

# Video Evidence to Reasoning Efficient Video Understanding via Explicit Evidence Grounding
**arXiv**：[2601.07761v1](https://arxiv.org/abs/2601.07761) · [PDF](https://arxiv.org/pdf/2601.07761.pdf)  
**作者**：Yanxiang Huang, Guohua Gao, Zhaoyang Wei, Jianyuan Ni  

**一句话要点**：提出链式证据框架以解决大视觉语言模型在视频推理中的效率与幻觉问题

**关键词**：视频推理, 证据接地, 幻觉缓解, 强化学习, 大规模数据集, 多模态理解

## 3 点简述
- 核心问题：大视觉语言模型在视频推理中面临计算成本高与幻觉风险的两难困境
- 方法要点：通过证据接地模块和证据锚定协议，解耦并优化感知接地与推理效率
- 实验或效果：在多个基准测试中实现新最优性能，显著提升准确性

## 摘要（原文）

> Large Vision-Language Models (LVLMs) face a fundamental dilemma in video reasoning: they are caught between the prohibitive computational costs of verbose reasoning and the hallucination risks of efficient, ungrounded approaches. To resolve this, we introduce the Chain of Evidence (CoE), a novel framework that architecturally decouples and co-optimizes perceptual grounding and reasoning efficiency. CoE incorporates two core innovations: (1) A lightweight Evidence Grounding Module (EGM) that acts as a query-guided filter, dynamically identifying and extracting a compact set of high-fidelity visual evidence; and (2) An Evidence-Anchoring Protocol optimized via Reinforcement Learning. Crucially, we design a composite reward mechanism that enforces process alignment, compelling the model to strictly reference identified temporal anchors during deduction, thereby mitigating hallucinations. To enable this, we construct CoE-Instruct, a large-scale dataset (164k samples) featuring a novel dual-annotation schema for separate perception and reasoning supervision. Extensive experiments on five benchmarks, including Video-MME, MVBench, and VSI-Bench, demonstrate that CoE-enhanced models establish a new state-of-the-art. They significantly outperform existing methods in accuracy, proving CoE to be a powerful and practical paradigm for reliable video understanding.

