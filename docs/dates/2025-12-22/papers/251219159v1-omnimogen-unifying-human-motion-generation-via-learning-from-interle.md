---
layout: default
title: OmniMoGen: Unifying Human Motion Generation via Learning from Interleaved Text-Motion Instructions
---

# OmniMoGen: Unifying Human Motion Generation via Learning from Interleaved Text-Motion Instructions
**arXiv**：[2512.19159v1](https://arxiv.org/abs/2512.19159) · [PDF](https://arxiv.org/pdf/2512.19159.pdf)  
**作者**：Wendong Bu, Kaihang Pan, Yuze Lin, Jiacheng Li, Kai Shen, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang  

**一句话要点**：提出OmniMoGen框架，通过交错文本-运动指令统一人类运动生成任务

**关键词**：人类运动生成, 交错指令学习, 统一框架, Transformer架构, RVQ-VAE, 多任务评估

## 3 点简述
- 核心问题：现有方法局限于孤立任务，缺乏自由形式和全目标生成的灵活性
- 方法要点：基于RVQ-VAE和Transformer架构，支持端到端指令驱动运动生成
- 实验或效果：在文本到运动、运动编辑和AnyContext基准上实现最先进性能

## 摘要（原文）

> Large language models (LLMs) have unified diverse linguistic tasks within a single framework, yet such unification remains unexplored in human motion generation. Existing methods are confined to isolated tasks, limiting flexibility for free-form and omni-objective generation. To address this, we propose OmniMoGen, a unified framework that enables versatile motion generation through interleaved text-motion instructions. Built upon a concise RVQ-VAE and transformer architecture, OmniMoGen supports end-to-end instruction-driven motion generation. We construct X2Mo, a large-scale dataset of over 137K interleaved text-motion instructions, and introduce AnyContext, a benchmark for evaluating interleaved motion generation. Experiments show that OmniMoGen achieves state-of-the-art performance on text-to-motion, motion editing, and AnyContext, exhibiting emerging capabilities such as compositional editing, self-reflective generation, and knowledge-informed generation. These results mark a step toward the next intelligent motion generation. Project Page: https://OmniMoGen.github.io/.

