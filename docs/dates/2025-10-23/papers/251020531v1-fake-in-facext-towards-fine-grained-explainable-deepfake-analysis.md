---
layout: default
title: Fake-in-Facext: Towards Fine-Grained Explainable DeepFake Analysis
---

# Fake-in-Facext: Towards Fine-Grained Explainable DeepFake Analysis
**arXiv**：[2510.20531v1](https://arxiv.org/abs/2510.20531) · [PDF](https://arxiv.org/pdf/2510.20531.pdf)  
**作者**：Lixiong Qin, Yang Zhang, Mei Wang, Jiani Hu, Weihong Deng, Weiran Xu  

**一句话要点**：提出Fake-in-Facext框架以解决细粒度可解释DeepFake分析问题

**关键词**：可解释DeepFake分析, 细粒度注释, 多模态大语言模型, 伪造解释, 面部视觉上下文, 多任务学习

## 3 点简述
- 当前可解释DeepFake分析方法缺乏细粒度感知，数据注释不可靠且粗粒度
- 引入Facial Image Concept Tree和FiFa-Annotator，实现细粒度区域概念划分与可靠注释
- FiFa-MLLM模型在AGE任务上超越基线，并在现有数据集上达到SOTA性能

## 摘要（原文）

> The advancement of Multimodal Large Language Models (MLLMs) has bridged the
> gap between vision and language tasks, enabling the implementation of
> Explainable DeepFake Analysis (XDFA). However, current methods suffer from a
> lack of fine-grained awareness: the description of artifacts in data annotation
> is unreliable and coarse-grained, and the models fail to support the output of
> connections between textual forgery explanations and the visual evidence of
> artifacts, as well as the input of queries for arbitrary facial regions. As a
> result, their responses are not sufficiently grounded in Face Visual Context
> (Facext). To address this limitation, we propose the Fake-in-Facext (FiFa)
> framework, with contributions focusing on data annotation and model
> construction. We first define a Facial Image Concept Tree (FICT) to divide
> facial images into fine-grained regional concepts, thereby obtaining a more
> reliable data annotation pipeline, FiFa-Annotator, for forgery explanation.
> Based on this dedicated data annotation, we introduce a novel
> Artifact-Grounding Explanation (AGE) task, which generates textual forgery
> explanations interleaved with segmentation masks of manipulated artifacts. We
> propose a unified multi-task learning architecture, FiFa-MLLM, to
> simultaneously support abundant multimodal inputs and outputs for fine-grained
> Explainable DeepFake Analysis. With multiple auxiliary supervision tasks,
> FiFa-MLLM can outperform strong baselines on the AGE task and achieve SOTA
> performance on existing XDFA datasets. The code and data will be made
> open-source at https://github.com/lxq1000/Fake-in-Facext.

