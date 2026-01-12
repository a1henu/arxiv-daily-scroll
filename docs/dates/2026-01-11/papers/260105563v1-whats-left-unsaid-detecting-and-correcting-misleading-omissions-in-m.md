---
layout: default
title: What's Left Unsaid? Detecting and Correcting Misleading Omissions in Multimodal News Previews
---

# What's Left Unsaid? Detecting and Correcting Misleading Omissions in Multimodal News Previews
**arXiv**：[2601.05563v1](https://arxiv.org/abs/2601.05563) · [PDF](https://arxiv.org/pdf/2601.05563.pdf)  
**作者**：Fanxiao Li, Jiaying Wu, Tingchao Fu, Dayang Li, Herun Wan, Wei Zhou, Min-Yen Kan  

**一句话要点**：提出OMGuard以检测和纠正多模态新闻预览中的误导性省略

**关键词**：多模态新闻预览, 误导性省略检测, 基准构建, 解释感知微调, 标题重写, 视觉干预

## 3 点简述
- 核心问题：社交媒体新闻预览（图像-标题对）通过选择性省略关键上下文，导致读者理解与全文内容偏离，这种隐性危害未被充分研究。
- 方法要点：开发多阶段管道构建MM-Misleading基准，并设计OMGuard，结合解释感知微调和基于理由的标题重写，提升检测与纠正能力。
- 实验或效果：OMGuard使8B模型检测准确率匹配235B LVLM，并在端到端纠正中表现更强，分析显示误导性多源于局部叙事偏移，需视觉干预。

## 摘要（原文）

> Even when factually correct, social-media news previews (image-headline pairs) can induce interpretation drift: by selectively omitting crucial context, they lead readers to form judgments that diverge from what the full article conveys. This covert harm is harder to detect than explicit misinformation yet remains underexplored. To address this gap, we develop a multi-stage pipeline that disentangles and simulates preview-based versus context-based understanding, enabling construction of the MM-Misleading benchmark. Using this benchmark, we systematically evaluate open-source LVLMs and uncover pronounced blind spots to omission-based misleadingness detection. We further propose OMGuard, which integrates (1) Interpretation-Aware Fine-Tuning, which used to improve multimodal misleadingness detection and (2) Rationale-Guided Misleading Content Correction, which uses explicit rationales to guide headline rewriting and reduce misleading impressions. Experiments show that OMGuard lifts an 8B model's detection accuracy to match a 235B LVLM and delivers markedly stronger end-to-end correction. Further analysis reveals that misleadingness typically stems from local narrative shifts (e.g., missing background) rather than global frame changes, and identifies image-driven scenarios where text-only correction fails, highlighting the necessity of visual interventions.

