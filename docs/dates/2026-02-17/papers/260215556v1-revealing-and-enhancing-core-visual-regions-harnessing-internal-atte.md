---
layout: default
title: Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs
---

# Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs
**arXiv**：[2602.15556v1](https://arxiv.org/abs/2602.15556) · [PDF](https://arxiv.org/pdf/2602.15556.pdf)  
**作者**：Guangtao Lyu, Qi Liu, Chenghao Xu, Jiexi Yan, Muli Yang, Xueting Li, Fen Fang, Cheng Deng  

**一句话要点**：提出PADE方法，利用内部注意力动态增强核心视觉区域以减轻LVLM幻觉

**关键词**：大型视觉语言模型, 幻觉缓解, 注意力机制, 免训练方法, 视觉基础, 多模态推理

## 3 点简述
- LVLM易产生幻觉，现有免训练方法受注意力沉没现象影响且计算开销大
- PADE通过正注意力动态图识别核心视觉区域，自适应控制干预强度并补偿系统令牌
- 实验表明PADE在多LVLM和基准上提升视觉基础并减少幻觉，验证其有效性

## 摘要（原文）

> LVLMs have achieved strong multimodal reasoning capabilities but remain prone to hallucinations, producing outputs inconsistent with visual inputs or user instructions. Existing training-free methods, including contrastive decoding and auxiliary expert models, which incur several times more computational overhead and may introduce potential interference, as well as static internal signal enhancement, are often vulnerable to the attention sink phenomenon. We find that internal Positive Attention Dynamics (PAD) in LVLMs naturally reveal semantically core visual regions under the distortions of attention sinks. Based on this, we propose Positive Attention Dynamics Enhancement (PADE), a training-free attention intervention that constructs a PAD map to identify semantically core visual regions, applies per-head Median Absolute Deviation Scaling to adaptively control the intervention strength, and leverages System-Token Compensation to maintain attention to complex user instructions and support long-term output consistency. Experiments on multiple LVLMs and benchmarks show that PADE improves visual grounding and reduces hallucinations, validating the effectiveness of leveraging internal attention dynamics for reliable multimodal reasoning.

