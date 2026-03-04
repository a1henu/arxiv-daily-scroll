---
layout: default
title: Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory
---

# Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory
**arXiv**：[2603.02663v1](https://arxiv.org/abs/2603.02663) · [PDF](https://arxiv.org/pdf/2603.02663.pdf)  
**作者**：Shunki Uebayashi, Kento Masui, Kyohei Atarashi, Han Bao, Hisashi Kashima, Naoto Inoue, Mayu Otani, Koh Takeuchi  

**一句话要点**：提出多模态多维项目反应理论框架以评估跨模态推理能力并优化多模态基准测试

**关键词**：多模态大语言模型, 跨模态推理, 项目反应理论, 基准测试优化, 模型评估

## 3 点简述
- 当前多模态大语言模型基准测试存在单模态捷径问题，导致评估不可靠且计算成本高
- M3IRT框架将模型能力和题目难度分解为图像、文本和跨模态组件，量化跨模态推理
- 在三个基准测试上验证，M3IRT能优先选择真正跨模态题目，减少评估成本并提高可靠性

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently emerged as general architectures capable of reasoning over diverse modalities. Benchmarks for MLLMs should measure their ability for cross-modal integration. However, current benchmarks are filled with shortcut questions, which can be solved using only a single modality, thereby yielding unreliable rankings. For example, in vision-language cases, we can find the correct answer without either the image or the text. These low-quality questions unnecessarily increase the size and computational requirements of benchmarks. We introduce a multi-modal and multidimensional item response theory framework (M3IRT) that extends classical IRT by decomposing both model ability and item difficulty into image-only, text-only, and cross-modal components. M3IRT estimates cross-modal ability of MLLMs and each question's cross-modal difficulty, enabling compact, high-quality subsets that better reflect multimodal reasoning. Across 24 VLMs on three benchmarks, M3IRT prioritizes genuinely cross-modal questions over shortcuts and preserves ranking fidelity even when 50% of items are artificially generated low-quality questions, thereby reducing evaluation cost while improving reliability. M3IRT thus offers a practical tool for assessing cross-modal reasoning and refining multimodal benchmarks.

