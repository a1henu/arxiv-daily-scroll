---
layout: default
title: IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck
---

# IBCircuit: Towards Holistic Circuit Discovery with Information Bottleneck
**arXiv**：[2602.22581v1](https://arxiv.org/abs/2602.22581) · [PDF](https://arxiv.org/pdf/2602.22581.pdf)  
**作者**：Tian Bian, Yifan Niu, Chaohao Yuan, Chengzhi Piao, Bingzhe Wu, Long-Kai Huang, Yu Rong, Tingyang Xu, Hong Cheng, Jia Li  

**一句话要点**：提出IBCircuit以基于信息瓶颈原则进行整体电路发现，无需设计损坏激活

**关键词**：电路发现, 信息瓶颈, 语言模型解释, 整体优化, 任务无关性

## 3 点简述
- 现有电路发现方法忽视电路整体性，需为不同任务设计损坏激活，不准确且低效
- IBCircuit基于信息瓶颈原则，通过优化框架整体识别信息性电路，适用于任意任务
- 在IOI和Greater-Than任务中，IBCircuit识别出更忠实和最小化的电路，优于相关方法

## 摘要（原文）

> Circuit discovery has recently attracted attention as a potential research direction to explain the non-trivial behaviors of language models. It aims to find the computational subgraphs, also known as circuits, within the model that are responsible for solving specific tasks. However, most existing studies overlook the holistic nature of these circuits and require designing specific corrupted activations for different tasks, which is inaccurate and inefficient. In this work, we propose an end-to-end approach based on the principle of Information Bottleneck, called IBCircuit, to identify informative circuits holistically. IBCircuit is an optimization framework for holistic circuit discovery and can be applied to any given task without tediously corrupted activation design. In both the Indirect Object Identification (IOI) and Greater-Than tasks, IBCircuit identifies more faithful and minimal circuits in terms of critical node components and edge components compared to recent related work.

