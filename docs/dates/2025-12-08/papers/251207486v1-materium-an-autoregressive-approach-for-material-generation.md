---
layout: default
title: Materium: An Autoregressive Approach for Material Generation
---

# Materium: An Autoregressive Approach for Material Generation
**arXiv**：[2512.07486v1](https://arxiv.org/abs/2512.07486) · [PDF](https://arxiv.org/pdf/2512.07486.pdf)  
**作者**：Niklas Dobberstein, Jan Hamaekers  

**一句话要点**：提出Materium自回归变换器以快速生成晶体结构，通过序列化表示实现高效材料设计。

**关键词**：材料生成, 自回归变换器, 晶体结构, 序列化表示, 条件生成, 快速生成

## 3 点简述
- 核心问题：传统扩散方法生成晶体结构需多次迭代去噪，速度慢且计算成本高。
- 方法要点：将3D材料表示转换为包含元素、氧化态、分数坐标和晶格参数的token序列，实现精确原子放置。
- 实验或效果：模型在单GPU上几小时可训练，生成速度快于扩散方法，支持多种属性条件生成，性能稳定。

## 摘要（原文）

> We present Materium: an autoregressive transformer for generating crystal structures that converts 3D material representations into token sequences. These sequences include elements with oxidation states, fractional coordinates and lattice parameters. Unlike diffusion approaches, which refine atomic positions iteratively through many denoising steps, Materium places atoms at precise fractional coordinates, enabling fast, scalable generation. With this design, the model can be trained in a few hours on a single GPU and generate samples much faster on GPUs and CPUs than diffusion-based approaches. The model was trained and evaluated using multiple properties as conditions, including fundamental properties, such as density and space group, as well as more practical targets, such as band gap and magnetic density. In both single and combined conditions, the model performs consistently well, producing candidates that align with the requested inputs.

