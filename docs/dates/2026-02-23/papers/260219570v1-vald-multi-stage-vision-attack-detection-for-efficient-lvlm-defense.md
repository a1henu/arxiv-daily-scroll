---
layout: default
title: VALD: Multi-Stage Vision Attack Detection for Efficient LVLM Defense
---

# VALD: Multi-Stage Vision Attack Detection for Efficient LVLM Defense
**arXiv**：[2602.19570v1](https://arxiv.org/abs/2602.19570) · [PDF](https://arxiv.org/pdf/2602.19570.pdf)  
**作者**：Nadav Kadvil, Ayellet Tal  

**一句话要点**：提出VALD多阶段视觉攻击检测方法，以高效防御大型视觉语言模型对抗性图像攻击。

**关键词**：视觉语言模型防御, 对抗性攻击检测, 多阶段检测, 图像变换, 数据整合, 高效计算

## 3 点简述
- 核心问题：大型视觉语言模型易受对抗性图像攻击，导致输出偏向合理但错误的响应。
- 方法要点：结合图像变换与代理数据整合，采用两阶段检测机制快速过滤干净输入，仅在必要时调用大型语言模型。
- 实验或效果：在保持高准确率的同时显著提升效率，多数干净图像跳过昂贵处理，攻击场景下开销最小。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) can be vulnerable to adversarial images that subtly bias their outputs toward plausible yet incorrect responses. We introduce a general, efficient, and training-free defense that combines image transformations with agentic data consolidation to recover correct model behavior. A key component of our approach is a two-stage detection mechanism that quickly filters out the majority of clean inputs. We first assess image consistency under content-preserving transformations at negligible computational cost. For more challenging cases, we examine discrepancies in a text-embedding space. Only when necessary do we invoke a powerful LLM to resolve attack-induced divergences. A key idea is to consolidate multiple responses, leveraging both their similarities and their differences. We show that our method achieves state-of-the-art accuracy while maintaining notable efficiency: most clean images skip costly processing, and even in the presence of numerous adversarial examples, the overhead remains minimal.

