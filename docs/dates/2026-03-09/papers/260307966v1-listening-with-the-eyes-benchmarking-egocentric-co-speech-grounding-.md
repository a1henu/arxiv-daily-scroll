---
layout: default
title: Listening with the Eyes: Benchmarking Egocentric Co-Speech Grounding across Space and Time
---

# Listening with the Eyes: Benchmarking Egocentric Co-Speech Grounding across Space and Time
**arXiv**：[2603.07966v1](https://arxiv.org/abs/2603.07966) · [PDF](https://arxiv.org/pdf/2603.07966.pdf)  
**作者**：Weijie Zhou, Xuantang Xiong, Zhenlin Hu, Xiaomeng Zhu, Chaoyang Zhao, Honghui Dong, Zhengyou Zhang, Ming Tang, Jinqiao Wang  

**一句话要点**：提出EcoG-Bench基准以严格评估具身智能中的指代性语音-手势时空对齐能力

**关键词**：指代性交互, 多模态对齐, 第一人称视频, 时空定位, 诊断基准, 可执行性评估

## 3 点简述
- 核心问题：现有基准存在语言捷径，无法评估指代性交互所需的音频-视觉对齐能力
- 方法要点：构建包含811个第一人称视频片段的双语诊断基准，要求联合预测内容、空间位置和时间
- 实验效果：人类表现接近完美，而最佳多模态大模型性能低下，揭示严重的可执行性差距

## 摘要（原文）

> In situated collaboration, speakers often use intentionally underspecified deictic commands (e.g., ``pass me \textit{that}''), whose referent becomes identifiable only by aligning speech with a brief co-speech pointing \emph{stroke}. However, many embodied benchmarks admit language-only shortcuts, allowing MLLMs to perform well without learning the \emph{audio--visual alignment} required by deictic interaction. To bridge this gap, we introduce \textbf{Egocentric Co-Speech Grounding (EcoG)}, where grounding is executable only if an agent jointly predicts \textit{What}, \textit{Where}, and \textit{When}. To operationalize this, we present \textbf{EcoG-Bench}, an evaluation-only bilingual (EN/ZH) diagnostic benchmark of \textbf{811} egocentric clips with dense spatial annotations and millisecond-level stroke supervision. It is organized under a \textbf{Progressive Cognitive Evaluation} protocol. Benchmarking state-of-the-art MLLMs reveals a severe executability gap: while human subjects achieve near-ceiling performance on EcoG-Bench (\textbf{96.9\%} strict Eco-Accuracy), the best native video-audio setting remains low (Gemini-3-Pro: \textbf{17.0\%}). Moreover, in a diagnostic ablation, replacing the native video--audio interface with timestamped frame samples and externally verified ASR (with word-level timing) substantially improves the same model (\textbf{17.0\%}$\to$\textbf{42.9\%}). Overall, EcoG-Bench provides a strict, executable testbed for event-level speech--gesture binding, and suggests that multimodal interfaces may bottleneck the observability of temporal alignment cues, independently of model reasoning.

