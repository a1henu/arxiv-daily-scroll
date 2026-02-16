---
layout: default
title: PLLM: Pseudo-Labeling Large Language Models for CAD Program Synthesis
---

# PLLM: Pseudo-Labeling Large Language Models for CAD Program Synthesis
**arXiv**：[2602.12561v1](https://arxiv.org/abs/2602.12561) · [PDF](https://arxiv.org/pdf/2602.12561.pdf)  
**作者**：Yuanbo Li, Dule Shu, Yanying Chen, Matt Klenk, Daniel Ritchie  

**一句话要点**：提出PLLM自训练框架，从无标签3D形状合成CAD程序

**关键词**：CAD程序合成, 自训练, 大语言模型, 无监督学习, 3D形状重建

## 3 点简述
- 核心问题：CAD程序合成依赖配对形状-程序数据，但此类数据常缺失。
- 方法要点：基于预训练LLM，迭代采样候选程序、选择高保真执行并增强程序以构建合成数据。
- 实验或效果：在ABC数据集上实验，几何保真度和程序多样性有持续提升。

## 摘要（原文）

> Recovering Computer-Aided Design (CAD) programs from 3D geometries is a widely studied problem. Recent advances in large language models (LLMs) have enabled progress in CAD program synthesis, but existing methods rely on supervised training with paired shape-program data, which is often unavailable. We introduce PLLM, a self-training framework for CAD program synthesis from unlabeled 3D shapes. Given a pre-trained CAD-capable LLM and a shape dataset, PLLM iteratively samples candidate programs, selects high-fidelity executions, and augments programs to construct synthetic program-shape pairs for fine-tuning. We experiment on adapting CAD-Recode from DeepCAD to the unlabeled ABC dataset show consistent improvements in geometric fidelity and program diversity.

