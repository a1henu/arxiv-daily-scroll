---
layout: default
title: Enabling Stroke-Level Structural Analysis of Hieroglyphic Scripts without Language-Specific Priors
---

# Enabling Stroke-Level Structural Analysis of Hieroglyphic Scripts without Language-Specific Priors
**arXiv**：[2601.05508v1](https://arxiv.org/abs/2601.05508) · [PDF](https://arxiv.org/pdf/2601.05508.pdf)  
**作者**：Fuwen Luo, Zihao Wan, Ziyue Wang, Yaluo Liu, Pau Tong Lin Xu, Xuanjia Qiao, Xiaolong Wang, Peng Li, Yang Liu  

**一句话要点**：提出HieroSA框架，使多模态大语言模型能自动从字符位图提取笔画级结构，无需语言特定先验。

**关键词**：笔画级结构分析, 多模态大语言模型, 字符图像处理, 跨语言泛化, 字形学分析

## 3 点简述
- 问题：现有大语言模型和多模态大语言模型难以建模字符笔画逻辑，且结构分析方法常依赖语言特定先验。
- 方法：HieroSA将字符图像转换为归一化坐标空间中的显式线段表示，实现跨语言泛化。
- 效果：实验表明HieroSA有效捕获字符内部结构和语义，可作为字形分析工具。

## 摘要（原文）

> Hieroglyphs, as logographic writing systems, encode rich semantic and cultural information within their internal structural composition. Yet, current advanced Large Language Models (LLMs) and Multimodal LLMs (MLLMs) usually remain structurally blind to this information. LLMs process characters as textual tokens, while MLLMs additionally view them as raw pixel grids. Both fall short to model the underlying logic of character strokes. Furthermore, existing structural analysis methods are often script-specific and labor-intensive. In this paper, we propose Hieroglyphic Stroke Analyzer (HieroSA), a novel and generalizable framework that enables MLLMs to automatically derive stroke-level structures from character bitmaps without handcrafted data. It transforms modern logographic and ancient hieroglyphs character images into explicit, interpretable line-segment representations in a normalized coordinate space, allowing for cross-lingual generalization. Extensive experiments demonstrate that HieroSA effectively captures character-internal structures and semantics, bypassing the need for language-specific priors. Experimental results highlight the potential of our work as a graphematics analysis tool for a deeper understanding of hieroglyphic scripts. View our code at https://github.com/THUNLP-MT/HieroSA.

