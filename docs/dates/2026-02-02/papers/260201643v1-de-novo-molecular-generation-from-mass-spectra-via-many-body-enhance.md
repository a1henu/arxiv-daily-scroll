---
layout: default
title: De Novo Molecular Generation from Mass Spectra via Many-Body Enhanced Diffusion
---

# De Novo Molecular Generation from Mass Spectra via Many-Body Enhanced Diffusion
**arXiv**：[2602.01643v1](https://arxiv.org/abs/2602.01643) · [PDF](https://arxiv.org/pdf/2602.01643.pdf)  
**作者**：Xichen Sun, Wentao Wei, Jiahua Rao, Jiancong Xie, Yuedong Yang  

**一句话要点**：提出MBGen扩散框架，通过多体增强建模从质谱生成分子结构

**关键词**：质谱分子生成, 多体建模, 扩散模型, 异构体解析, 高阶相互作用

## 3 点简述
- 核心问题：现有方法忽略质谱中的高阶相互作用，难以解析复杂异构体和非局部碎裂机制
- 方法要点：集成多体注意力机制和高阶边建模，全面利用质谱结构信息
- 实验或效果：在NPLIB1和MassSpecGym基准上性能提升高达230%，有效捕获高阶相互作用

## 摘要（原文）

> Molecular structure generation from mass spectrometry is fundamental for understanding cellular metabolism and discovering novel compounds. Although tandem mass spectrometry (MS/MS) enables the high-throughput acquisition of fragment fingerprints, these spectra often reflect higher-order interactions involving the concerted cleavage of multiple atoms and bonds-crucial for resolving complex isomers and non-local fragmentation mechanisms. However, most existing methods adopt atom-centric and pairwise interaction modeling, overlooking higher-order edge interactions and lacking the capacity to systematically capture essential many-body characteristics for structure generation. To overcome these limitations, we present MBGen, a Many-Body enhanced diffusion framework for de novo molecular structure Generation from mass spectra. By integrating a many-body attention mechanism and higher-order edge modeling, MBGen comprehensively leverages the rich structural information encoded in MS/MS spectra, enabling accurate de novo generation and isomer differentiation for novel molecules. Experimental results on the NPLIB1 and MassSpecGym benchmarks demonstrate that MBGen achieves superior performance, with improvements of up to 230% over state-of-the-art methods, highlighting the scientific value and practical utility of many-body modeling for mass spectrometry-based molecular generation. Further analysis and ablation studies show that our approach effectively captures higher-order interactions and exhibits enhanced sensitivity to complex isomeric and non-local fragmentation information.

