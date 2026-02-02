---
layout: default
title: Learning to Build Shapes by Extrusion
---

# Learning to Build Shapes by Extrusion
**arXiv**：[2601.22858v1](https://arxiv.org/abs/2601.22858) · [PDF](https://arxiv.org/pdf/2601.22858.pdf)  
**作者**：Thor Vestergaard Christiansen, Karran Pandey, Alba Reinders, Karan Singh, Morten Rieger Hannemose, J. Andreas Bærentzen  

**一句话要点**：提出文本编码挤出表示，利用大语言模型从文本生成可编辑的3D网格。

**关键词**：3D网格生成, 挤出表示, 大语言模型, 网格编辑, 流形网格

## 3 点简述
- 核心问题：传统基于多边形的3D网格生成方法难以支持任意面数并保证流形性。
- 方法要点：通过分解四边形网格为面环，训练大语言模型学习挤出序列以组装网格。
- 实验或效果：实现网格重建、新形状合成及对现有网格的编辑功能。

## 摘要（原文）

> We introduce Text Encoded Extrusion (TEE), a text-based representation that expresses mesh construction as sequences of face extrusions rather than polygon lists, and a method for generating 3D meshes from TEE using a large language model (LLM). By learning extrusion sequences that assemble a mesh, similar to the way artists create meshes, our approach naturally supports arbitrary output face counts and produces manifold meshes by design, in contrast to recent transformer-based models. The learnt extrusion sequences can also be applied to existing meshes - enabling editing in addition to generation. To train our model, we decompose a library of quadrilateral meshes with non-self-intersecting face loops into constituent loops, which can be viewed as their building blocks, and finetune an LLM on the steps for reassembling the meshes by performing a sequence of extrusions. We demonstrate that our representation enables reconstruction, novel shape synthesis, and the addition of new features to existing meshes.

