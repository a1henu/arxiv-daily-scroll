---
layout: default
title: CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images
---

# CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images
**arXiv**：[2510.11718v1](https://arxiv.org/abs/2510.11718) · [PDF](https://arxiv.org/pdf/2510.11718.pdf)  
**作者**：Chengqi Duan, Kaiyue Sun, Rongyao Fang, Manyuan Zhang, Yan Feng, Ying Luo, Yufang Liu, Ke Wang, Peng Pei, Xunliang Cai, Hongsheng Li, Yi Ma, Xihui Liu  

**一句话要点**：提出CodePlot-CoT方法，通过代码驱动图像解决数学视觉推理问题

**关键词**：数学视觉推理, 代码驱动推理, 多模态学习, 数据集构建, 图像到代码转换

## 3 点简述
- 核心问题：LLMs和VLMs在需要视觉辅助的数学推理中缺乏精确性和可控性。
- 方法要点：利用VLM生成文本推理和可执行绘图代码，渲染图像作为视觉思维。
- 实验或效果：在Math-VR基准上，模型性能比基线提升高达21%。

## 摘要（原文）

> Recent advances in Large Language Models (LLMs) and Vision Language Models
> (VLMs) have shown significant progress in mathematical reasoning, yet they
> still face a critical bottleneck with problems requiring visual assistance,
> such as drawing auxiliary lines or plotting functions to solve the problems.
> Most LLMs and VLMs are constrained to text-only reasoning chains, while
> multimodal unified models that can generate interleaved text and images lack
> the necessary precision and controllability for such tasks. To address this, we
> propose CodePlot-CoT, a code-driven Chain-of-Thought paradigm for "thinking
> with images" in mathematics. Our approach leverages the VLM to generate text
> reasoning as well as executable plotting code, which is then rendered into
> images as "visual thought", to solve mathematical problems. To achieve this, we
> first construct Math-VR, the first large-scale, bilingual dataset and benchmark
> for Mathematics problems with Visual Reasoning, comprising 178K samples.
> Second, to create high-quality training data, we develop a state-of-the-art
> image-to-code converter specialized for parsing complex mathematical figures
> into codes. Finally, using these training data, we train the CodePlot-CoT model
> for solving mathematical problems. Experimental results show that our model
> achieves up to 21% increase over base model on our new benchmark, fully
> validating the efficacy of our proposed code-driven reasoning paradigm. Our
> work opens a new direction for multimodal mathematical reasoning and provides
> the community with the first large-scale dataset, comprehensive benchmark, and
> strong approach for such problems. To facilitate future research, we make our
> datasets, code, and pretrained models publicly available at
> https://github.com/HKU-MMLab/Math-VR-CodePlot-CoT.

