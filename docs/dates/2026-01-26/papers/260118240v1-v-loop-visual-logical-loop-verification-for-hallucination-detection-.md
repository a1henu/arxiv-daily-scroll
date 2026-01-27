---
layout: default
title: V-Loop: Visual Logical Loop Verification for Hallucination Detection in Medical Visual Question Answering
---

# V-Loop: Visual Logical Loop Verification for Hallucination Detection in Medical Visual Question Answering
**arXiv**：[2601.18240v1](https://arxiv.org/abs/2601.18240) · [PDF](https://arxiv.org/pdf/2601.18240.pdf)  
**作者**：Mengyuan Jin, Zehui Liao, Yong Xia  

**一句话要点**：提出V-Loop视觉逻辑循环验证框架，以检测医学视觉问答中的幻觉问题。

**关键词**：医学视觉问答, 幻觉检测, 逻辑循环验证, 多模态大语言模型, 视觉注意力一致性

## 3 点简述
- 核心问题：多模态大语言模型在医学视觉问答中易产生与视觉事实矛盾的幻觉响应，存在高风险。
- 方法要点：通过双向推理形成视觉基础逻辑循环，无需训练即可验证答案的事实正确性。
- 实验或效果：在多个医学VQA基准和MLLMs上优于现有内省方法，高效且可提升不确定性方法效果。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown remarkable capability in assisting disease diagnosis in medical visual question answering (VQA). However, their outputs remain vulnerable to hallucinations (i.e., responses that contradict visual facts), posing significant risks in high-stakes medical scenarios. Recent introspective detection methods, particularly uncertainty-based approaches, offer computational efficiency but are fundamentally indirect, as they estimate predictive uncertainty for an image-question pair rather than verifying the factual correctness of a specific answer. To address this limitation, we propose Visual Logical Loop Verification (V-Loop), a training-free and plug-and-play framework for hallucination detection in medical VQA. V-Loop introduces a bidirectional reasoning process that forms a visually grounded logical loop to verify factual correctness. Given an input, the MLLM produces an answer for the primary input pair. V-Loop extracts semantic units from the primary QA pair, generates a verification question by conditioning on the answer unit to re-query the question unit, and enforces visual attention consistency to ensure answering both primary question and verification question rely on the same image evidence. If the verification answer matches the expected semantic content, the logical loop closes, indicating factual grounding; otherwise, the primary answer is flagged as hallucinated. Extensive experiments on multiple medical VQA benchmarks and MLLMs show that V-Loop consistently outperforms existing introspective methods, remains highly efficient, and further boosts uncertainty-based approaches when used in combination.

