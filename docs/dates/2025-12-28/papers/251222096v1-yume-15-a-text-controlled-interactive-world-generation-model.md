---
layout: default
title: Yume-1.5: A Text-Controlled Interactive World Generation Model
---

# Yume-1.5: A Text-Controlled Interactive World Generation Model
**arXiv**：[2512.22096v1](https://arxiv.org/abs/2512.22096) · [PDF](https://arxiv.org/pdf/2512.22096.pdf)  
**作者**：Xiaofeng Mao, Zhen Li, Chuanhao Li, Xiaojie Xu, Kaining Ying, Tong He, Jiangmiao Pang, Yu Qiao, Kaipeng Zhang  

**一句话要点**：提出Yume-1.5框架，通过文本控制生成交互式连续世界，解决实时性和参数规模问题。

**关键词**：交互世界生成, 扩散模型, 实时流加速, 文本控制生成, 上下文压缩, 注意力蒸馏

## 3 点简述
- 核心问题：现有扩散模型生成交互世界时参数过大、推理步骤长、历史上下文增长快，限制实时性和文本控制能力。
- 方法要点：设计三组件框架，包括统一上下文压缩与线性注意力的长视频生成、双向注意力蒸馏与增强文本嵌入的实时流加速、文本控制世界事件生成。
- 实验或效果：支持基于键盘探索生成世界，代码已开源，具体性能指标未知。

## 摘要（原文）

> Recent approaches have demonstrated the promise of using diffusion models to generate interactive and explorable worlds. However, most of these methods face critical challenges such as excessively large parameter sizes, reliance on lengthy inference steps, and rapidly growing historical context, which severely limit real-time performance and lack text-controlled generation capabilities. To address these challenges, we propose \method, a novel framework designed to generate realistic, interactive, and continuous worlds from a single image or text prompt. \method achieves this through a carefully designed framework that supports keyboard-based exploration of the generated worlds. The framework comprises three core components: (1) a long-video generation framework integrating unified context compression with linear attention; (2) a real-time streaming acceleration strategy powered by bidirectional attention distillation and an enhanced text embedding scheme; (3) a text-controlled method for generating world events. We have provided the codebase in the supplementary material.

