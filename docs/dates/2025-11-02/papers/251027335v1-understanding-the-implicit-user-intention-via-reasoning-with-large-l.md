---
layout: default
title: Understanding the Implicit User Intention via Reasoning with Large Language Model for Image Editing
---

# Understanding the Implicit User Intention via Reasoning with Large Language Model for Image Editing
**arXiv**：[2510.27335v1](https://arxiv.org/abs/2510.27335) · [PDF](https://arxiv.org/pdf/2510.27335.pdf)  
**作者**：Yijia Wang, Yiqing Shen, Weiming Chen, Zhihai He  

**一句话要点**：提出CIELR方法，通过LLM推理将复杂指令分解为简单编辑动作，避免联合微调LLM与扩散模型。

**关键词**：复杂图像编辑, 大语言模型推理, 扩散模型, 语义表示, 迭代更新, 基准构建

## 3 点简述
- 核心问题：现有方法处理复杂图像编辑指令需联合微调LLM与扩散模型，计算成本高。
- 方法要点：构建图像结构化语义表示，迭代更新以细化场景，实现灵活编辑。
- 实验或效果：在SmartEdit数据集上PSNR提升9.955 dB，并在自建CIEBench基准中表现优异。

## 摘要（原文）

> Existing image editing methods can handle simple editing instructions very
> well. To deal with complex editing instructions, they often need to jointly
> fine-tune the large language models (LLMs) and diffusion models (DMs), which
> involves very high computational complexity and training cost. To address this
> issue, we propose a new method, called \textbf{C}omplex \textbf{I}mage
> \textbf{E}diting via \textbf{L}LM \textbf{R}easoning (CIELR), which converts a
> complex user instruction into a set of simple and explicit editing actions,
> eliminating the need for jointly fine-tuning the large language models and
> diffusion models. Specifically, we first construct a structured semantic
> representation of the input image using foundation models. Then, we introduce
> an iterative update mechanism that can progressively refine this
> representation, obtaining a fine-grained visual representation of the image
> scene. This allows us to perform complex and flexible image editing tasks.
> Extensive experiments on the SmartEdit Reasoning Scenario Set show that our
> method surpasses the previous state-of-the-art by 9.955 dB in PSNR, indicating
> its superior preservation of regions that should remain consistent. Due to the
> limited number of samples of public datasets of complex image editing with
> reasoning, we construct a benchmark named CIEBench, containing 86 image
> samples, together with a metric specifically for reasoning-based image editing.
> CIELR also outperforms previous methods on this benchmark. The code and dataset
> are available at
> \href{https://github.com/Jia-shao/Reasoning-Editing}{https://github.com/Jia-shao/Reasoning-Editing}.

