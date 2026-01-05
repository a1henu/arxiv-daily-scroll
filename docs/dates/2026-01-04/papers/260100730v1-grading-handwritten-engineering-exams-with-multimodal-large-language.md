---
layout: default
title: Grading Handwritten Engineering Exams with Multimodal Large Language Models
---

# Grading Handwritten Engineering Exams with Multimodal Large Language Models
**arXiv**：[2601.00730v1](https://arxiv.org/abs/2601.00730) · [PDF](https://arxiv.org/pdf/2601.00730.pdf)  
**作者**：Janez Perš, Jon Muhovič, Andrej Košir, Boštjan Murovec  

**一句话要点**：提出基于多模态大语言模型的端到端工作流，用于自动评分手写工程考试，保留标准考试流程。

**关键词**：手写考试评分, 多模态大语言模型, 工程教育, 自动评分系统, 参考方案摘要, 可靠性设计

## 3 点简述
- 核心问题：手写STEM考试评分耗时且难以扩展，需处理开放推理和图表。
- 方法要点：使用多模态LLMs，基于手写参考方案和评分规则，通过多阶段设计确保可靠性。
- 实验或效果：在真实课程测验中评估，平均绝对差异约8分，手动审查触发率约17%。

## 摘要（原文）

> Handwritten STEM exams capture open-ended reasoning and diagrams, but manual grading is slow and difficult to scale. We present an end-to-end workflow for grading scanned handwritten engineering quizzes with multimodal large language models (LLMs) that preserves the standard exam process (A4 paper, unconstrained student handwriting). The lecturer provides only a handwritten reference solution (100%) and a short set of grading rules; the reference is converted into a text-only summary that conditions grading without exposing the reference scan. Reliability is achieved through a multi-stage design with a format/presence check to prevent grading blank answers, an ensemble of independent graders, supervisor aggregation, and rigid templates with deterministic validation to produce auditable, machine-parseable reports. We evaluate the frozen pipeline in a clean-room protocol on a held-out real course quiz in Slovenian, including hand-drawn circuit schematics. With state-of-the-art backends (GPT-5.2 and Gemini-3 Pro), the full pipeline achieves $\approx$8-point mean absolute difference to lecturer grades with low bias and an estimated manual-review trigger rate of $\approx$17% at $D_{\max}=40$. Ablations show that trivial prompting and removing the reference solution substantially degrade accuracy and introduce systematic over-grading, confirming that structured prompting and reference grounding are essential.

