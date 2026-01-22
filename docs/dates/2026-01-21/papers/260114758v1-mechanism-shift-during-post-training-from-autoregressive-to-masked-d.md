---
layout: default
title: Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models
---

# Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models
**arXiv**：[2601.14758v1](https://arxiv.org/abs/2601.14758) · [PDF](https://arxiv.org/pdf/2601.14758.pdf)  
**作者**：Injin Kong, Hyoungjoon Lee, Yohan Jo  

**一句话要点**：揭示后训练中自回归模型向掩码扩散模型的机制转变，支持非序列全局规划

**关键词**：后训练机制转变, 自回归模型, 掩码扩散模型, 电路分析, 全局规划, 双向推理

## 3 点简述
- 核心问题：后训练是否赋予掩码扩散模型真实双向推理能力，还是仅重包装自回归启发式方法
- 方法要点：通过比较电路分析，发现任务结构依赖的机制转变，包括结构重连和语义分布变化
- 实验或效果：掩码扩散模型在局部因果依赖任务中保留自回归电路，在全局规划任务中放弃初始路径，增强早期层处理

## 摘要（原文）

> Post-training pretrained Autoregressive models (ARMs) into Masked Diffusion models (MDMs) has emerged as a cost-effective strategy to overcome the limitations of sequential generation. However, the internal algorithmic transformations induced by this paradigm shift remain unexplored, leaving it unclear whether post-trained MDMs acquire genuine bidirectional reasoning capabilities or merely repackage autoregressive heuristics. In this work, we address this question by conducting a comparative circuit analysis of ARMs and their MDM counterparts. Our analysis reveals a systematic "mechanism shift" dependent on the structural nature of the task. Structurally, we observe a distinct divergence: while MDMs largely retain autoregressive circuitry for tasks dominated by local causal dependencies, they abandon initialized pathways for global planning tasks, exhibiting distinct rewiring characterized by increased early-layer processing. Semantically, we identify a transition from sharp, localized specialization in ARMs to distributed integration in MDMs. Through these findings, we conclude that diffusion post-training does not merely adapt model parameters but fundamentally reorganizes internal computation to support non-sequential global planning.

