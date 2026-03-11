---
layout: default
title: InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing
---

# InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing
**arXiv**：[2603.09877v1](https://arxiv.org/abs/2603.09877) · [PDF](https://arxiv.org/pdf/2603.09877.pdf)  
**作者**：Changyao Tian, Danni Yang, Guanzhou Chen, Erfei Cui, Zhaokai Wang, Yuchen Duan, Penghao Yin, Sitao Chen, Ganlin Yang, Mingxin Liu, Zirun Zhu, Ziqian Fan, Leyao Gu, Haomin Wang, Qi Wei, Jinhui Yin, Xue Yang, Zhihang Zhong, Qi Qin, Yi Xin, Bin Fu, Yihao Liu, Jiaye Ge, Qipeng Guo, Gen Luo, Hongsheng Li, Yu Qiao, Kai Chen, Hongjie Zhang  

**一句话要点**：提出InternVL-U统一多模态模型，以轻量化设计平衡理解与生成能力

**关键词**：统一多模态模型, 轻量化设计, 视觉生成, 语义理解, 推理对齐

## 3 点简述
- 核心问题：统一多模态模型在语义理解与生成能力间存在固有权衡
- 方法要点：采用解耦视觉表示与模块化设计，集成MLLM与MMDiT生成头
- 实验效果：4B参数模型在多项任务上超越更大规模基线，保持高效能平衡

## 摘要（原文）

> Unified multimodal models (UMMs) that integrate understanding, reasoning, generation, and editing face inherent trade-offs between maintaining strong semantic comprehension and acquiring powerful generation capabilities. In this report, we present InternVL-U, a lightweight 4B-parameter UMM that democratizes these capabilities within a unified framework. Guided by the principles of unified contextual modeling and modality-specific modular design with decoupled visual representations, InternVL-U integrates a state-of-the-art Multimodal Large Language Model (MLLM) with a specialized MMDiT-based visual generation head. To further bridge the gap between aesthetic generation and high-level intelligence, we construct a comprehensive data synthesis pipeline targeting high-semantic-density tasks, such as text rendering and scientific reasoning, under a reasoning-centric paradigm that leverages Chain-of-Thought (CoT) to better align abstract user intent with fine-grained visual generation details. Extensive experiments demonstrate that InternVL-U achieves a superior performance - efficiency balance. Despite using only 4B parameters, it consistently outperforms unified baseline models with over 3x larger scales such as BAGEL (14B) on various generation and editing tasks, while retaining strong multimodal understanding and reasoning capabilities.

