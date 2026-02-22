---
layout: default
title: LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights
---

# LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights
**arXiv**：[2602.17510v1](https://arxiv.org/abs/2602.17510) · [PDF](https://arxiv.org/pdf/2602.17510.pdf)  
**作者**：Kasun Dewage, Marianna Pensky, Suranadi De Silva, Shankadeep Mondal  

**一句话要点**：提出CRAFT方法，通过跨层冻结Tucker分解实现参数高效微调

**关键词**：参数高效微调, Tucker分解, 跨层张量, 注意力权重, 冻结因子, 轻量适配

## 3 点简述
- 核心问题：现有张量分解方法在参数高效微调中未充分结合跨层权重与冻结策略
- 方法要点：对预训练注意力权重进行跨层Tucker分解，冻结因子并训练轻量适配矩阵
- 实验或效果：在GLUE基准上，仅需41K参数即达到竞争性能，参数数与模型维度深度无关

## 摘要（原文）

> We introduce CRAFT (Cross-layer Rank Adaptation via Frozen Tucker), a parameter-efficient fine-tuning (PEFT) method that applies Tucker tensor decomposition to pre-trained attention weight matrices stacked across transformer layers and trains only small square adaptation matrices on the resulting frozen Tucker factors. Existing tensor-based PEFT methods decompose gradient updates: LoTR applies Tucker decomposition with shared factor matrices, while SuperLoRA groups and reshapes $ΔW$ across layers before applying Tucker decomposition. Separately, methods like PiSSA apply SVD to pre-trained weights but operate independently per layer. CRAFT bridges these two lines of work: it performs full Tucker decomposition via Higher-Order SVD (HOSVD) directly on pre-trained weights organized as cross-layer 3D tensors, freezes all resulting factors, and adapts the model through lightweight trainable transformations applied to each factor matrix. Experiments on the GLUE benchmark using RoBERTa-base and RoBERTa-large demonstrate that CRAFT achieves competitive performance with existing methods while requiring only 41K Tucker adaptation parameters--a count independent of model dimension and depth at fixed Tucker ranks.

