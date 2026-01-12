---
layout: default
title: Open-Vocabulary 3D Instruction Ambiguity Detection
---

# Open-Vocabulary 3D Instruction Ambiguity Detection
**arXiv**：[2601.05991v1](https://arxiv.org/abs/2601.05991) · [PDF](https://arxiv.org/pdf/2601.05991.pdf)  
**作者**：Jiayu Ding, Haoran Tang, Ge Li  

**一句话要点**：提出AmbiVer框架以解决3D场景中开放词汇指令歧义检测的安全问题

**关键词**：开放词汇指令歧义检测, 3D场景理解, 视觉语言模型, 安全关键AI, 多视角证据收集, 基准数据集

## 3 点简述
- 核心问题：现有具身AI研究忽视指令歧义，可能导致安全关键领域严重错误
- 方法要点：AmbiVer通过多视角视觉证据收集引导视觉语言模型判断指令歧义
- 实验或效果：在Ambi3D基准上验证任务挑战性及AmbiVer有效性，促进更安全AI

## 摘要（原文）

> In safety-critical domains, linguistic ambiguity can have severe consequences; a vague command like "Pass me the vial" in a surgical setting could lead to catastrophic errors. Yet, most embodied AI research overlooks this, assuming instructions are clear and focusing on execution rather than confirmation. To address this critical safety gap, we are the first to define Open-Vocabulary 3D Instruction Ambiguity Detection, a fundamental new task where a model must determine if a command has a single, unambiguous meaning within a given 3D scene. To support this research, we build Ambi3D, the large-scale benchmark for this task, featuring over 700 diverse 3D scenes and around 22k instructions. Our analysis reveals a surprising limitation: state-of-the-art 3D Large Language Models (LLMs) struggle to reliably determine if an instruction is ambiguous. To address this challenge, we propose AmbiVer, a two-stage framework that collects explicit visual evidence from multiple views and uses it to guide an vision-language model (VLM) in judging instruction ambiguity. Extensive experiments demonstrate the challenge of our task and the effectiveness of AmbiVer, paving the way for safer and more trustworthy embodied AI. Code and dataset available at https://jiayuding031020.github.io/ambi3d/.

