---
layout: default
title: Think Visually, Reason Textually: Vision-Language Synergy in ARC
---

# Think Visually, Reason Textually: Vision-Language Synergy in ARC
**arXiv**：[2511.15703v1](https://arxiv.org/abs/2511.15703) · [PDF](https://arxiv.org/pdf/2511.15703.pdf)  
**作者**：Beichen Zhang, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, Jiaqi Wang  

**一句话要点**：提出视觉-语言协同方法以提升ARC-AGI抽象推理性能

**关键词**：视觉-语言协同, 抽象推理, ARC-AGI, 模态切换, 自校正机制

## 3 点简述
- 核心问题：前沿基础模型在少量示例下难以推断结构化转换规则，如ARC-AGI测试所示。
- 方法要点：引入视觉-语言协同推理和模态切换自校正，利用视觉抽象与语言规则互补。
- 实验或效果：在多种模型和任务上，相比纯文本基线性能提升最高达4.33%。

## 摘要（原文）

> Abstract reasoning from minimal examples remains a core unsolved problem for frontier foundation models such as GPT-5 and Grok 4. These models still fail to infer structured transformation rules from a handful of examples, which is a key hallmark of human intelligence. The Abstraction and Reasoning Corpus for Artificial General Intelligence (ARC-AGI) provides a rigorous testbed for this capability, demanding conceptual rule induction and transfer to novel tasks. Most existing methods treat ARC-AGI as a purely textual reasoning task, overlooking the fact that humans rely heavily on visual abstraction when solving such puzzles. However, our pilot experiments reveal a paradox: naively rendering ARC-AGI grids as images degrades performance due to imprecise rule execution. This leads to our central hypothesis that vision and language possess complementary strengths across distinct reasoning stages: vision supports global pattern abstraction and verification, whereas language specializes in symbolic rule formulation and precise execution. Building on this insight, we introduce two synergistic strategies: (1) Vision-Language Synergy Reasoning (VLSR), which decomposes ARC-AGI into modality-aligned subtasks; and (2) Modality-Switch Self-Correction (MSSC), which leverages vision to verify text-based reasoning for intrinsic error correction. Extensive experiments demonstrate that our approach yields up to a 4.33% improvement over text-only baselines across diverse flagship models and multiple ARC-AGI tasks. Our findings suggest that unifying visual abstraction with linguistic reasoning is a crucial step toward achieving generalizable, human-like intelligence in future foundation models. Source code will be released soon.

