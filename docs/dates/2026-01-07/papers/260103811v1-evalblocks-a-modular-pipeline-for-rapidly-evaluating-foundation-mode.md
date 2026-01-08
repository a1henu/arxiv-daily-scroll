---
layout: default
title: EvalBlocks: A Modular Pipeline for Rapidly Evaluating Foundation Models in Medical Imaging
---

# EvalBlocks: A Modular Pipeline for Rapidly Evaluating Foundation Models in Medical Imaging
**arXiv**：[2601.03811v1](https://arxiv.org/abs/2601.03811) · [PDF](https://arxiv.org/pdf/2601.03811.pdf)  
**作者**：Jan Tagscherer, Sarah de Boer, Lena Philipp, Fennie van der Graaf, Dré Peeters, Joeran Bosma, Lars Leijten, Bogdan Obreja, Ewoud Smit, Alessa Hering  

**一句话要点**：提出EvalBlocks模块化框架以解决医学影像基础模型开发中评估效率低下的问题

**关键词**：医学影像, 基础模型评估, 模块化框架, 可复现性, 并行计算, 开源软件

## 3 点简述
- 医学影像基础模型开发中，下游性能监控依赖手动、易错的工作流，导致评估缓慢
- EvalBlocks基于Snakemake，支持数据集、模型、聚合方法和评估策略的模块化集成，实现可复现和并行执行
- 在五个先进基础模型和三个分类任务上验证，框架开源，加速模型迭代和创新

## 摘要（原文）

> Developing foundation models in medical imaging requires continuous monitoring of downstream performance. Researchers are burdened with tracking numerous experiments, design choices, and their effects on performance, often relying on ad-hoc, manual workflows that are inherently slow and error-prone. We introduce EvalBlocks, a modular, plug-and-play framework for efficient evaluation of foundation models during development. Built on Snakemake, EvalBlocks supports seamless integration of new datasets, foundation models, aggregation methods, and evaluation strategies. All experiments and results are tracked centrally and are reproducible with a single command, while efficient caching and parallel execution enable scalable use on shared compute infrastructure. Demonstrated on five state-of-the-art foundation models and three medical imaging classification tasks, EvalBlocks streamlines model evaluation, enabling researchers to iterate faster and focus on model innovation rather than evaluation logistics. The framework is released as open source software at https://github.com/DIAGNijmegen/eval-blocks.

