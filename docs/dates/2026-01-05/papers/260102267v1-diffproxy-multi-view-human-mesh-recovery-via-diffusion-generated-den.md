---
layout: default
title: DiffProxy: Multi-View Human Mesh Recovery via Diffusion-Generated Dense Proxies
---

# DiffProxy: Multi-View Human Mesh Recovery via Diffusion-Generated Dense Proxies
**arXiv**：[2601.02267v1](https://arxiv.org/abs/2601.02267) · [PDF](https://arxiv.org/pdf/2601.02267.pdf)  
**作者**：Renke Wang, Zhenyu Zhang, Ying Tai, Jian Yang  

**一句话要点**：提出DiffProxy框架，通过扩散生成密集代理解决多视角人体网格恢复中的标注偏差与域差距问题。

**关键词**：多视角人体网格恢复, 扩散生成模型, 合成数据训练, 零样本泛化, 不确定性优化

## 3 点简述
- 核心问题：真实数据集标注不完美导致训练偏差，合成数据存在域差距影响泛化。
- 方法要点：利用扩散先验生成多视角一致代理，结合手部细化模块和不确定性感知测试时缩放。
- 实验或效果：在合成数据上训练，在五个真实基准上实现零样本泛化，尤其在遮挡和部分视角场景表现优异。

## 摘要（原文）

> Human mesh recovery from multi-view images faces a fundamental challenge: real-world datasets contain imperfect ground-truth annotations that bias the models' training, while synthetic data with precise supervision suffers from domain gap. In this paper, we propose DiffProxy, a novel framework that generates multi-view consistent human proxies for mesh recovery. Central to DiffProxy is leveraging the diffusion-based generative priors to bridge the synthetic training and real-world generalization. Its key innovations include: (1) a multi-conditional mechanism for generating multi-view consistent, pixel-aligned human proxies; (2) a hand refinement module that incorporates flexible visual prompts to enhance local details; and (3) an uncertainty-aware test-time scaling method that increases robustness to challenging cases during optimization. These designs ensure that the mesh recovery process effectively benefits from the precise synthetic ground truth and generative advantages of the diffusion-based pipeline. Trained entirely on synthetic data, DiffProxy achieves state-of-the-art performance across five real-world benchmarks, demonstrating strong zero-shot generalization particularly on challenging scenarios with occlusions and partial views. Project page: https://wrk226.github.io/DiffProxy.html

