---
layout: default
title: JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence
---

# JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence
**arXiv**：[2510.23538v1](https://arxiv.org/abs/2510.23538) · [PDF](https://arxiv.org/pdf/2510.23538.pdf)  
**作者**：Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Lei Li, Kai Chen, Qipeng Guo, Ben Kao, Fei Yuan  

**一句话要点**：提出JanusCoder系列模型，构建视觉-程序接口以解决多模态代码数据稀缺问题

**关键词**：多模态代码智能, 视觉-程序接口, 代码生成, 数据合成, 统一模型, 代码语料库

## 3 点简述
- 核心问题：高质量多模态代码数据稀缺，阻碍视觉化代码智能应用发展
- 方法要点：开发合成工具包构建JanusCode-800K语料库，训练统一模型处理文本和视觉输入
- 实验或效果：7B至14B模型在文本和视觉编码任务中表现优异，接近或超越商业模型

## 摘要（原文）

> The scope of neural code intelligence is rapidly expanding beyond text-based
> source code to encompass the rich visual outputs that programs generate. This
> visual dimension is critical for advanced applications like flexible content
> generation and precise, program-driven editing of visualizations. However,
> progress has been impeded by the scarcity of high-quality multimodal code data,
> a bottleneck stemming from challenges in synthesis and quality assessment. To
> address these challenges, we make contributions from both a data and modeling
> perspective. We first introduce a complete synthesis toolkit that leverages
> reciprocal synergies between data modalities to efficiently produce a
> large-scale, high-quality corpus spanning from standard charts to complex
> interactive web UIs and code-driven animations. Leveraging this toolkit, we
> construct JanusCode-800K, the largest multimodal code corpus to date. This
> powers the training of our models, JanusCoder and JanusCoderV, which establish
> a visual-programmatic interface for generating code from textual instructions,
> visual inputs, or a combination of both. Our unified model is a departure from
> existing approaches that build specialized models for isolated tasks. Extensive
> experiments on both text-centric and vision-centric coding tasks demonstrate
> the superior performance of the JanusCoder series, with our 7B to 14B scale
> models approaching or even exceeding the performance of commercial models.
> Furthermore, extensive analysis provides key insights into harmonizing
> programmatic logic with its visual expression. Our code and checkpoints will
> are available at https://github.com/InternLM/JanusCoder.

