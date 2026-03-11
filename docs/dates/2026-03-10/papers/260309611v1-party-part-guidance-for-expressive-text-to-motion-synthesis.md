---
layout: default
title: ParTY: Part-Guidance for Expressive Text-to-Motion Synthesis
---

# ParTY: Part-Guidance for Expressive Text-to-Motion Synthesis
**arXiv**：[2603.09611v1](https://arxiv.org/abs/2603.09611) · [PDF](https://arxiv.org/pdf/2603.09611.pdf)  
**作者**：KunHo Heo, SuYeon Kim, Yonghyun Gwon, Youngbin Kim, MyeongAh Cho  

**一句话要点**：提出ParTY框架以解决文本到动作合成中部分动作表达与全身动作连贯性的权衡问题

**关键词**：文本到动作合成, 部分动作生成, 动作连贯性, 语义对齐, 多模态融合

## 3 点简述
- 现有方法难以准确生成涉及特定身体部分的动作，且部分动作生成方法缺乏文本语义与身体部分的对齐机制
- ParTY通过部分引导网络、部分感知文本对齐和整体-部分融合，增强部分表达性同时生成连贯全身动作
- 实验在部分级别和连贯性级别评估中显示ParTY相比先前方法有显著改进

## 摘要（原文）

> Text-to-motion synthesis aims to generate natural and expressive human motions from textual descriptions. While existing approaches primarily focus on generating holistic motions from text descriptions, they struggle to accurately reflect actions involving specific body parts. Recent part-wise motion generation methods attempt to resolve this but face two critical limitations: (i) they lack explicit mechanisms for aligning textual semantics with individual body parts, and (ii) they often generate incoherent full-body motions due to integrating independently generated part motions. To overcome these issues and resolve the fundamental trade-off in existing methods, we propose ParTY, a novel framework that enhances part expressiveness while generating coherent full-body motions. ParTY comprises: (1) Part-Guided Network, which first generates part motions to obtain part guidance, then uses it to generate holistic motions; (2) Part-aware Text Grounding, which diversely transforms text embeddings and appropriately aligns them with each body part; and (3) Holistic-Part Fusion, which adaptively fuses holistic motions and part motions. Extensive experiments, including part-level and coherence-level evaluations, demonstrate that ParTY achieves substantial improvements over previous methods.

