---
layout: default
title: Counting Hallucinations in Diffusion Models
---

# Counting Hallucinations in Diffusion Models
**arXiv**：[2510.13080v1](https://arxiv.org/abs/2510.13080) · [PDF](https://arxiv.org/pdf/2510.13080.pdf)  
**作者**：Shuai Fu, Jian Zhou, Qi Chen, Huang Jing, Huy Anh Nguyen, Xiaohan Liu, Zhixiong Zeng, Lin Ma, Quanshi Zhang, Qi Wu  

**一句话要点**：提出计数幻觉量化方法以解决扩散模型生成错误对象数量问题

**关键词**：扩散模型, 计数幻觉, 评估协议, 数据集构建, 图像生成, 采样条件分析

## 3 点简述
- 核心问题：扩散模型常生成与真实知识冲突的计数幻觉，如错误对象数量
- 方法要点：构建CountHalluSet数据集，开发标准化评估协议量化计数幻觉
- 实验或效果：分析采样条件影响，揭示FID等指标无法捕捉计数幻觉

## 摘要（原文）

> Diffusion probabilistic models (DPMs) have demonstrated remarkable progress
> in generative tasks, such as image and video synthesis. However, they still
> often produce hallucinated samples (hallucinations) that conflict with
> real-world knowledge, such as generating an implausible duplicate cup floating
> beside another cup. Despite their prevalence, the lack of feasible
> methodologies for systematically quantifying such hallucinations hinders
> progress in addressing this challenge and obscures potential pathways for
> designing next-generation generative models under factual constraints. In this
> work, we bridge this gap by focusing on a specific form of hallucination, which
> we term counting hallucination, referring to the generation of an incorrect
> number of instances or structured objects, such as a hand image with six
> fingers, despite such patterns being absent from the training data. To this
> end, we construct a dataset suite CountHalluSet, with well-defined counting
> criteria, comprising ToyShape, SimObject, and RealHand. Using these datasets,
> we develop a standardized evaluation protocol for quantifying counting
> hallucinations, and systematically examine how different sampling conditions in
> DPMs, including solver type, ODE solver order, sampling steps, and initial
> noise, affect counting hallucination levels. Furthermore, we analyze their
> correlation with common evaluation metrics such as FID, revealing that this
> widely used image quality metric fails to capture counting hallucinations
> consistently. This work aims to take the first step toward systematically
> quantifying hallucinations in diffusion models and offer new insights into the
> investigation of hallucination phenomena in image generation.

