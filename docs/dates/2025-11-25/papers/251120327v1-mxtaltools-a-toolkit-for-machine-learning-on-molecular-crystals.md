---
layout: default
title: MXtalTools: A Toolkit for Machine Learning on Molecular Crystals
---

# MXtalTools: A Toolkit for Machine Learning on Molecular Crystals
**arXiv**：[2511.20327v1](https://arxiv.org/abs/2511.20327) · [PDF](https://arxiv.org/pdf/2511.20327.pdf)  
**作者**：Michael Kilgour, Mark E. Tuckerman, Jutta Rogal  

**一句话要点**：提出MXtalTools工具包，用于分子晶体的机器学习建模。

**关键词**：分子晶体建模, 机器学习工具包, CUDA加速, 晶体参数化, 开源软件

## 3 点简述
- 核心问题：分子晶体数据建模缺乏灵活工具，阻碍机器学习研究。
- 方法要点：提供数据集合成、模型训练、晶体参数化等模块化功能。
- 实验或效果：利用CUDA加速实现高通量建模，代码开源并提供文档。

## 摘要（原文）

> We present MXtalTools, a flexible Python package for the data-driven modelling of molecular crystals, facilitating machine learning studies of the molecular solid state. MXtalTools comprises several classes of utilities: (1) synthesis, collation, and curation of molecule and crystal datasets, (2) integrated workflows for model training and inference, (3) crystal parameterization and representation, (4) crystal structure sampling and optimization, (5) end-to-end differentiable crystal sampling, construction and analysis. Our modular functions can be integrated into existing workflows or combined and used to build novel modelling pipelines. MXtalTools leverages CUDA acceleration to enable high-throughput crystal modelling. The Python code is available open-source on our GitHub page, with detailed documentation on ReadTheDocs.

