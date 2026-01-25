---
layout: default
title: Assessing Situational and Spatial Awareness of VLMs with Synthetically Generated Video
---

# Assessing Situational and Spatial Awareness of VLMs with Synthetically Generated Video
**arXiv**：[2601.15780v1](https://arxiv.org/abs/2601.15780) · [PDF](https://arxiv.org/pdf/2601.15780.pdf)  
**作者**：Pascal Benschop, Justin Dauwels, Jan van Gemert  

**一句话要点**：提出合成视频基准以评估视觉语言模型的情境与空间感知能力

**关键词**：视觉语言模型, 空间推理, 合成基准, 视频分类, 情境感知, 空间感知

## 3 点简述
- 核心问题：视觉语言模型在依赖细微时空线索的空间推理上表现脆弱
- 方法要点：通过最小化视频对测试情境感知和空间感知的互补技能
- 实验或效果：评估显示模型性能仅略高于随机水平，稳定颜色线索部分缓解角色混淆

## 摘要（原文）

> Spatial reasoning in vision language models (VLMs) remains fragile when semantics hinge on subtle temporal or geometric cues. We introduce a synthetic benchmark that probes two complementary skills: situational awareness (recognizing whether an interaction is harmful or benign) and spatial awareness (tracking who does what to whom, and reasoning about relative positions and motion). Through minimal video pairs, we test three challenges: distinguishing violence from benign activity, binding assailant roles across viewpoints, and judging fine-grained trajectory alignment. While we evaluate recent VLMs in a training-free setting, the benchmark is applicable to any video classification model. Results show performance only slightly above chance across tasks. A simple aid, stable color cues, partly reduces assailant role confusions but does not resolve the underlying weakness. By releasing data and code, we aim to provide reproducible diagnostics and seed exploration of lightweight spatial priors to complement large-scale pretraining.

