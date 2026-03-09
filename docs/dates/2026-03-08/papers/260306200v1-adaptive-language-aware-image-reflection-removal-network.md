---
layout: default
title: Adaptive Language-Aware Image Reflection Removal Network
---

# Adaptive Language-Aware Image Reflection Removal Network
**arXiv**：[2603.06200v1](https://arxiv.org/abs/2603.06200) · [PDF](https://arxiv.org/pdf/2603.06200.pdf)  
**作者**：Siyan Fang, Yuntao Wang, Jinpu Zhang, Ziwen Li, Yuehuan Wang  

**一句话要点**：提出自适应语言感知网络以处理复杂反射去除中的不准确语言输入问题

**关键词**：图像反射去除, 语言引导视觉, 自适应网络, 复杂反射处理, 数据集构建

## 3 点简述
- 现有方法难以处理复杂反射，语言描述不准确影响性能
- ALANet结合过滤与优化策略，减少语言负面影响并增强对齐
- 引入CRLAV数据集评估性能，实验显示超越现有方法

## 摘要（原文）

> Existing image reflection removal methods struggle to handle complex reflections. Accurate language descriptions can help the model understand the image content to remove complex reflections. However, due to blurred and distorted interferences in reflected images, machine-generated language descriptions of the image content are often inaccurate, which harms the performance of language-guided reflection removal. To address this, we propose the Adaptive Language-Aware Network (ALANet) to remove reflections even with inaccurate language inputs. Specifically, ALANet integrates both filtering and optimization strategies. The filtering strategy reduces the negative effects of language while preserving its benefits, whereas the optimization strategy enhances the alignment between language and visual features. ALANet also utilizes language cues to decouple specific layer content from feature maps, improving its ability to handle complex reflections. To evaluate the model's performance under complex reflections and varying levels of language accuracy, we introduce the Complex Reflection and Language Accuracy Variance (CRLAV) dataset. Experimental results demonstrate that ALANet surpasses state-of-the-art methods for image reflection removal. The code and dataset are available at https://github.com/fashyon/ALANet.

