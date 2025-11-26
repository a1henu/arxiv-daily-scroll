---
layout: default
title: Does Understanding Inform Generation in Unified Multimodal Models? From Analysis to Path Forward
---

# Does Understanding Inform Generation in Unified Multimodal Models? From Analysis to Path Forward
**arXiv**：[2511.20561v1](https://arxiv.org/abs/2511.20561) · [PDF](https://arxiv.org/pdf/2511.20561.pdf)  
**作者**：Yuwei Niu, Weiyang Jin, Jiaqi Liao, Chaoran Feng, Peng Jin, Bin Lin, Zongjian Li, Bin Zhu, Weihao Yu, Li Yuan  

**一句话要点**：提出UniSandbox框架分析统一多模态模型中理解与生成的差距

**关键词**：统一多模态模型, 理解生成差距, 思维链推理, 知识迁移, 解耦评估, 自训练方法

## 3 点简述
- 核心问题：统一多模态模型中理解是否真正指导生成，存在显著差距。
- 方法要点：使用解耦评估框架和合成数据集，避免数据泄露。
- 实验或效果：显式思维链可弥合差距，自训练能内化推理能力。

## 摘要（原文）

> Recent years have witnessed significant progress in Unified Multimodal Models, yet a fundamental question remains: Does understanding truly inform generation? To investigate this, we introduce UniSandbox, a decoupled evaluation framework paired with controlled, synthetic datasets to avoid data leakage and enable detailed analysis. Our findings reveal a significant understanding-generation gap, which is mainly reflected in two key dimensions: reasoning generation and knowledge transfer. Specifically, for reasoning generation tasks, we observe that explicit Chain-of-Thought (CoT) in the understanding module effectively bridges the gap, and further demonstrate that a self-training approach can successfully internalize this ability, enabling implicit reasoning during generation. Additionally, for knowledge transfer tasks, we find that CoT assists the generative process by helping retrieve newly learned knowledge, and also discover that query-based architectures inherently exhibit latent CoT-like properties that affect this transfer. UniSandbox provides preliminary insights for designing future unified architectures and training strategies that truly bridge the gap between understanding and generation. Code and data are available at https://github.com/PKU-YuanGroup/UniSandBox

