---
layout: default
title: OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens
---

# OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens
**arXiv**：[2603.02138v1](https://arxiv.org/abs/2603.02138) · [PDF](https://arxiv.org/pdf/2603.02138.pdf)  
**作者**：Yiying Yang, Wei Cheng, Sijin Chen, Honghao Fu, Xianfang Zeng, Yujun Cai, Gang Yu, Xingjun Ma  

**一句话要点**：提出OmniLottie框架，通过参数化Lottie令牌从多模态指令生成高质量矢量动画

**关键词**：矢量动画生成, Lottie令牌化, 多模态指令, 预训练模型, JSON格式化, 动画数据集

## 3 点简述
- 核心问题：原始Lottie JSON文件包含大量不变结构元数据和格式化令牌，学习矢量动画生成困难
- 方法要点：设计Lottie令牌化器，将JSON转换为结构化序列，基于预训练视觉语言模型生成动画
- 实验或效果：在MMLottie-2M数据集上验证，能生成生动且语义对齐的矢量动画，遵循多模态指令

## 摘要（原文）

> OmniLottie is a versatile framework that generates high quality vector animations from multi-modal instructions. For flexible motion and visual content control, we focus on Lottie, a light weight JSON formatting for both shapes and animation behaviors representation. However, the raw Lottie JSON files contain extensive invariant structural metadata and formatting tokens, posing significant challenges for learning vector animation generation. Therefore, we introduce a well designed Lottie tokenizer that transforms JSON files into structured sequences of commands and parameters representing shapes, animation functions and control parameters. Such tokenizer enables us to build OmniLottie upon pretrained vision language models to follow multi-modal interleaved instructions and generate high quality vector animations. To further advance research in vector animation generation, we curate MMLottie-2M, a large scale dataset of professionally designed vector animations paired with textual and visual annotations. With extensive experiments, we validate that OmniLottie can produce vivid and semantically aligned vector animations that adhere closely to multi modal human instructions.

