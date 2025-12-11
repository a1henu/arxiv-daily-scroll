---
layout: default
title: IF-Bench: Benchmarking and Enhancing MLLMs for Infrared Images with Generative Visual Prompting
---

# IF-Bench: Benchmarking and Enhancing MLLMs for Infrared Images with Generative Visual Prompting
**arXiv**：[2512.09663v1](https://arxiv.org/abs/2512.09663) · [PDF](https://arxiv.org/pdf/2512.09663.pdf)  
**作者**：Tao Zhang, Yuyang Hong, Yang Xia, Kun Ding, Zeyu Zhang, Ying Wang, Shiming Xiang, Chunhong Pan  

**一句话要点**：提出IF-Bench基准与GenViP方法，以评估和提升多模态大模型在红外图像理解中的性能。

**关键词**：红外图像理解, 多模态大模型, 基准评估, 生成视觉提示, 领域适应

## 3 点简述
- 核心问题：多模态大模型在红外图像理解能力尚未被系统评估，存在领域分布偏移。
- 方法要点：构建首个高质量红外图像基准IF-Bench，并提出无需训练的生成视觉提示方法GenViP，通过图像编辑转换红外图像为RGB。
- 实验或效果：评估40多个模型，分析模型规模等因素的影响，GenViP方法在广泛模型中带来显著性能提升。

## 摘要（原文）

> Recent advances in multimodal large language models (MLLMs) have led to impressive progress across various benchmarks. However, their capability in understanding infrared images remains unexplored. To address this gap, we introduce IF-Bench, the first high-quality benchmark designed for evaluating multimodal understanding of infrared images. IF-Bench consists of 499 images sourced from 23 infrared datasets and 680 carefully curated visual question-answer pairs, covering 10 essential dimensions of image understanding. Based on this benchmark, we systematically evaluate over 40 open-source and closed-source MLLMs, employing cyclic evaluation, bilingual assessment, and hybrid judgment strategies to enhance the reliability of the results. Our analysis reveals how model scale, architecture, and inference paradigms affect infrared image comprehension, providing valuable insights for this area. Furthermore, we propose a training-free generative visual prompting (GenViP) method, which leverages advanced image editing models to translate infrared images into semantically and spatially aligned RGB counterparts, thereby mitigating domain distribution shifts. Extensive experiments demonstrate that our method consistently yields significant performance improvements across a wide range of MLLMs. The benchmark and code are available at https://github.com/casiatao/IF-Bench.

