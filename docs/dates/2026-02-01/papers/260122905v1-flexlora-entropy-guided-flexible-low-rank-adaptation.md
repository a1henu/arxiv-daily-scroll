---
layout: default
title: FlexLoRA: Entropy-Guided Flexible Low-Rank Adaptation
---

# FlexLoRA: Entropy-Guided Flexible Low-Rank Adaptation
**arXiv**：[2601.22905v1](https://arxiv.org/abs/2601.22905) · [PDF](https://arxiv.org/pdf/2601.22905.pdf)  
**作者**：Muqing Liu, Chongjie Si, Yuheng Jia  

**一句话要点**：提出FlexLoRA以解决LoRA固定秩限制问题，通过熵引导实现灵活低秩适应。

**关键词**：参数高效微调, 低秩适应, 动态秩分配, 谱能量熵, 模型压缩

## 3 点简述
- 核心问题：LoRA固定秩设计缺乏灵活性，动态方法依赖启发式指标且无扩展机制。
- 方法要点：基于谱能量熵评估矩阵重要性，支持全局预算下的秩剪枝与扩展，使用零影响初始化。
- 实验或效果：在多个基准测试中一致优于现有方法，代码已开源。

## 摘要（原文）

> Large pre-trained models achieve remarkable success across diverse domains, yet fully fine-tuning incurs prohibitive computational and memory costs. Parameter-efficient fine-tuning (PEFT) has thus become a mainstream paradigm. Among them, Low-Rank Adaptation (LoRA) introduces trainable low-rank matrices and shows strong performance, nevertheless, its fixed-rank design limits flexibility. Dynamic rank allocation methods mitigate this issue by pruning redundant directions; however, they often rely on heuristic, element-level metrics that globally sort rank directions without matrix-wise distinction, and they lack mechanisms to expand capacity in layers requiring additional adaptation. To overcome these limitations, we propose FlexLoRA, an entropy-guided flexible low-rank adaptation framework that (i) evaluates matrix importance via spectral energy entropy, (ii) supports rank pruning and expansion under a global budget, and (iii) employs zero-impact initialization for newly added singular directions to ensure stability. By addressing granularity, flexibility, and stability limitations, FlexLoRA provides a more principled solution for PEFT. Extensive experiments show that FlexLoRA consistently outperforms state-of-the-art baselines across benchmarks. Codes are available at https://github.com/Chongjie-Si/Subspace-Tuning.

