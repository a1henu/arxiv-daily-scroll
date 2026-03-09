---
layout: default
title: Cut to the Chase: Training-free Multimodal Summarization via Chain-of-Events
---

# Cut to the Chase: Training-free Multimodal Summarization via Chain-of-Events
**arXiv**：[2603.06213v1](https://arxiv.org/abs/2603.06213) · [PDF](https://arxiv.org/pdf/2603.06213.pdf)  
**作者**：Xiaoxing You, Qiang Huang, Lingyu Li, Xiaojun Chang, Jun Yu  

**一句话要点**：提出训练无关的多模态摘要框架CoE，通过事件链解决跨模态融合与时间建模问题。

**关键词**：多模态摘要, 训练无关方法, 事件链推理, 分层事件图, 跨模态定位, 时间建模

## 3 点简述
- 核心问题：现有方法依赖领域监督、跨模态融合弱、时间建模扁平。
- 方法要点：基于分层事件图构建事件链，实现结构化推理与跨模态定位。
- 实验效果：在八个数据集上超越基线，平均提升ROUGE 3.04、CIDEr 9.51、BERTScore 1.88。

## 摘要（原文）

> Multimodal Summarization (MMS) aims to generate concise textual summaries by understanding and integrating information across videos, transcripts, and images. However, existing approaches still suffer from three main challenges: (1) reliance on domain-specific supervision, (2) implicit fusion with weak cross-modal grounding, and (3) flat temporal modeling without event transitions. To address these issues, we introduce **CoE**, a training-free MMS framework that performs structured reasoning through a **Chain-of-Events** guided by a Hierarchical Event Graph (HEG). The HEG encodes textual semantics into an explicit event hierarchy that scaffolds cross-modal grounding and temporal reasoning. Guided by this structure, **CoE** localizes key visual cues, models event evolution and causal transitions, and refines outputs via lightweight style adaptation for domain alignment. Extensive experiments on eight diverse datasets demonstrate that **CoE** consistently outperforms state-of-the-art video CoT baselines, achieving average gains of **+3.04 ROUGE**, **+9.51 CIDEr**, and **+1.88 BERTScore**, highlighting its robustness, interpretability, and cross-domain generalization. Our code is available at https://github.com/youxiaoxing/CoE.

