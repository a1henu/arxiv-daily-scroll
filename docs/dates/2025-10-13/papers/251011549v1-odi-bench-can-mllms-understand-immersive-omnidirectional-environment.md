---
layout: default
title: ODI-Bench: Can MLLMs Understand Immersive Omnidirectional Environments?
---

# ODI-Bench: Can MLLMs Understand Immersive Omnidirectional Environments?
**arXiv**：[2510.11549v1](https://arxiv.org/abs/2510.11549) · [PDF](https://arxiv.org/pdf/2510.11549.pdf)  
**作者**：Liu Yang, Huiyu Duan, Ran Tao, Juntao Cheng, Sijing Wu, Yunhao Li, Jing Liu, Xiongkuo Min, Guangtao Zhai  

**一句话要点**：提出ODI-Bench基准和Omni-CoT方法以评估和增强MLLMs在全景图像理解中的能力

**关键词**：全景图像理解, 多模态大语言模型, 基准评估, 思维链推理, 沉浸式环境, 问答对数据集

## 3 点简述
- 核心问题：多模态大语言模型在全景图像理解中表现不佳，缺乏沉浸式上下文捕捉能力
- 方法要点：引入Omni-CoT，一种无需训练的方法，通过思维链推理结合文本和视觉线索提升理解
- 实验或效果：在ODI-Bench上测试20个MLLMs，显示当前模型仍存在困难，Omni-CoT显著改善性能

## 摘要（原文）

> Omnidirectional images (ODIs) provide full 360x180 view which are widely
> adopted in VR, AR and embodied intelligence applications. While multi-modal
> large language models (MLLMs) have demonstrated remarkable performance on
> conventional 2D image and video understanding benchmarks, their ability to
> comprehend the immersive environments captured by ODIs remains largely
> unexplored. To address this gap, we first present ODI-Bench, a novel
> comprehensive benchmark specifically designed for omnidirectional image
> understanding. ODI-Bench contains 2,000 high-quality omnidirectional images and
> over 4,000 manually annotated question-answering (QA) pairs across 10
> fine-grained tasks, covering both general-level and spatial-level ODI
> understanding. Extensive experiments are conducted to benchmark 20
> representative MLLMs, including proprietary and open-source models, under both
> close-ended and open-ended settings. Experimental results reveal that current
> MLLMs still struggle to capture the immersive context provided by ODIs. To this
> end, we further introduce Omni-CoT, a training-free method which significantly
> enhances MLLMs' comprehension ability in the omnidirectional environment
> through chain-of-thought reasoning across both textual information and visual
> cues. Both the benchmark and the code will be released upon the publication.

