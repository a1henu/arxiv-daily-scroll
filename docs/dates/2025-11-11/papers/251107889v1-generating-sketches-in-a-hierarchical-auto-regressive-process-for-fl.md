---
layout: default
title: Generating Sketches in a Hierarchical Auto-Regressive Process for Flexible Sketch Drawing Manipulation at Stroke-Level
---

# Generating Sketches in a Hierarchical Auto-Regressive Process for Flexible Sketch Drawing Manipulation at Stroke-Level
**arXiv**：[2511.07889v1](https://arxiv.org/abs/2511.07889) · [PDF](https://arxiv.org/pdf/2511.07889.pdf)  
**作者**：Sicong Zang, Shuhui Gao, Zhijun Fang  

**一句话要点**：提出分层自回归过程以实现笔画级灵活草图绘制操控

**关键词**：草图生成, 自回归模型, 笔画级操控, 分层过程, 可控生成

## 3 点简述
- 现有方法需在生成前固定所有笔画条件，无法在过程中灵活操控
- 采用三阶段分层自回归过程：预测笔画嵌入、锚定位置、转换为绘制动作
- 实验表明模型能实时调整笔画嵌入，提升草图生成的灵活性和可控性

## 摘要（原文）

> Generating sketches with specific patterns as expected, i.e., manipulating sketches in a controllable way, is a popular task. Recent studies control sketch features at stroke-level by editing values of stroke embeddings as conditions. However, in order to provide generator a global view about what a sketch is going to be drawn, all these edited conditions should be collected and fed into generator simultaneously before generation starts, i.e., no further manipulation is allowed during sketch generating process. In order to realize sketch drawing manipulation more flexibly, we propose a hierarchical auto-regressive sketch generating process. Instead of generating an entire sketch at once, each stroke in a sketch is generated in a three-staged hierarchy: 1) predicting a stroke embedding to represent which stroke is going to be drawn, and 2) anchoring the predicted stroke on the canvas, and 3) translating the embedding to a sequence of drawing actions to form the full sketch. Moreover, the stroke prediction, anchoring and translation are proceeded auto-regressively, i.e., both the recently generated strokes and their positions are considered to predict the current one, guiding model to produce an appropriate stroke at a suitable position to benefit the full sketch generation. It is flexible to manipulate stroke-level sketch drawing at any time during generation by adjusting the exposed editable stroke embeddings.

