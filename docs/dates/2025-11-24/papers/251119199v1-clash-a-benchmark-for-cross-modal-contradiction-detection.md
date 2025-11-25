---
layout: default
title: CLASH: A Benchmark for Cross-Modal Contradiction Detection
---

# CLASH: A Benchmark for Cross-Modal Contradiction Detection
**arXiv**：[2511.19199v1](https://arxiv.org/abs/2511.19199) · [PDF](https://arxiv.org/pdf/2511.19199.pdf)  
**作者**：Teodora Popordanoska, Jiameng Li, Matthew B. Blaschko  

**一句话要点**：提出CLASH基准以解决多模态输入中矛盾检测的评估问题

**关键词**：多模态基准, 矛盾检测, 图像字幕, 模型评估, 微调优化

## 3 点简述
- 现实多模态输入常含矛盾，现有基准假设一致性，无法评估矛盾检测能力
- CLASH基准使用COCO图像与矛盾字幕，包含对象或属性级矛盾，提供多格式问题
- 分析显示先进模型存在模态偏见，针对性微调可显著提升矛盾检测性能

## 摘要（原文）

> Contradictory multimodal inputs are common in real-world settings, yet existing benchmarks typically assume input consistency and fail to evaluate cross-modal contradiction detection - a fundamental capability for preventing hallucinations and ensuring reliability. We introduce CLASH, a novel benchmark for multimodal contradiction detection, featuring COCO images paired with contradictory captions containing controlled object-level or attribute-level contradictions. The samples include targeted questions evaluated in both multiple-choice and open-ended formats. The benchmark provides an extensive fine-tuning set filtered through automated quality checks, alongside a smaller human-verified diagnostic set. Our analysis of state-of-the-art models reveals substantial limitations in recognizing cross-modal conflicts, exposing systematic modality biases and category-specific weaknesses. Furthermore, we empirically demonstrate that targeted fine-tuning on CLASH substantially enhances conflict detection capabilities.

