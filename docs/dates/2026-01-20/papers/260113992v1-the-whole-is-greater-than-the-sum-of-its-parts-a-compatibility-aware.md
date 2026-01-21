---
layout: default
title: "The Whole Is Greater Than the Sum of Its Parts": A Compatibility-Aware Multi-Teacher CoT Distillation Framework
---

# "The Whole Is Greater Than the Sum of Its Parts": A Compatibility-Aware Multi-Teacher CoT Distillation Framework
**arXiv**：[2601.13992v1](https://arxiv.org/abs/2601.13992) · [PDF](https://arxiv.org/pdf/2601.13992.pdf)  
**作者**：Jin Cui, Jiaqi Guo, Jiepeng Zhou, Ruixuan Yang, Jiayi Lu, Jiajun Xu, Jiangcheng Song, Boran Zhao, Pengju Ren  

**一句话要点**：提出兼容性感知多教师CoT蒸馏框架以解决单教师蒸馏能力受限问题

**关键词**：思维链蒸馏, 多教师学习, 兼容性评估, 灾难性遗忘缓解, 自适应监督融合

## 3 点简述
- 核心问题：单教师CoT蒸馏存在能力偏见和灾难性遗忘，多教师融合易导致幻觉。
- 方法要点：基于图共识、互信息适应性和损失难度动态加权教师梯度，实现自适应监督融合。
- 实验或效果：在多个基准测试中达到最先进性能，有效缓解灾难性遗忘并保持知识结构。

## 摘要（原文）

> Chain-of-Thought (CoT) reasoning empowers Large Language Models (LLMs) with remarkable capabilities but typically requires prohibitive parameter scales. CoT distillation has emerged as a promising paradigm to transfer reasoning prowess into compact Student Models (SLMs), but existing approaches often rely on a solitary teacher, capping the student's potential since individual LLMs often exhibit distinct capability biases and may suffer from catastrophic forgetting. While leveraging diverse teachers seems appealing, effectively fusing their supervisions remains challenging: teacher-student incompatibility risks amplifying hallucinations, and passive supervision fails to ensure genuine logic internalization. To address this, we introduce COMPACT, a framework that adaptively fuses supervisions from different teachers by dynamically weighting teacher gradients based on the student's real-time compatibility evaluated by a multi-dimensional metric: (1) Graph-based Consensus to filter misleading rationales by identifying mainstream reasoning paths; (2) Mutual-Information-based Adaptability to detect "epiphany moments" for genuinely understanding the reasoning process rather than merely imitating; and (3) Loss-based Difficulty to assess student receptivity to the teacher's guidance and prevent negative transfer. Extensive experiments and latent space analysis demonstrate that COMPACT effectively integrates diverse reasoning capabilities without damaging the model's original knowledge structure, achieving state-of-the-art performance on various benchmarks while mitigating catastrophic forgetting.

