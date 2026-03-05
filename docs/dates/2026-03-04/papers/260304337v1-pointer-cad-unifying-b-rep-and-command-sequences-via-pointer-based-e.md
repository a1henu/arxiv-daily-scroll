---
layout: default
title: Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection
---

# Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection
**arXiv**：[2603.04337v1](https://arxiv.org/abs/2603.04337) · [PDF](https://arxiv.org/pdf/2603.04337.pdf)  
**作者**：Dacheng Qi, Chenyu Wang, Jingwei Xu, Tianzhe Chu, Zibo Zhao, Wen Liu, Wenrui Ding, Yi Ma, Shenghua Gao  

**一句话要点**：提出Pointer-CAD框架，通过指针选择统一B-Rep与命令序列以解决CAD生成中的实体选择与量化误差问题

**关键词**：CAD生成, 指针机制, B-Rep表示, 命令序列, 量化误差, 几何实体选择

## 3 点简述
- 核心问题：现有基于命令序列的CAD生成方法不支持几何实体选择，导致复杂编辑操作受限，且量化误差引发拓扑错误
- 方法要点：引入指针机制，在LLM生成过程中预测并选择B-Rep模型中的几何实体，结合文本描述与历史B-Rep进行逐步生成
- 实验或效果：在约57.5万CAD模型数据集上验证，显著降低分割错误，提升复杂结构生成能力，优于先前命令序列方法

## 摘要（原文）

> Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error.

