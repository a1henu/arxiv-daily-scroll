---
layout: default
title: Kaleido: Open-Sourced Multi-Subject Reference Video Generation Model
---

# Kaleido: Open-Sourced Multi-Subject Reference Video Generation Model
**arXiv**：[2510.18573v1](https://arxiv.org/abs/2510.18573) · [PDF](https://arxiv.org/pdf/2510.18573.pdf)  
**作者**：Zhenxing Zhang, Jiayan Teng, Zhuoyi Yang, Tiankun Cao, Cheng Wang, Xiaotao Gu, Jie Tang, Dan Guo, Meng Wang  

**一句话要点**：提出Kaleido框架以解决多主体参考视频生成中的一致性和背景分离问题

**关键词**：主题到视频生成, 多主体一致性, 参考图像集成, 数据合成, 位置编码, 视频合成

## 3 点简述
- 核心问题：现有方法在多图像条件下难以保持多主体一致性和背景分离，导致参考保真度低和语义漂移
- 方法要点：引入数据构建管道和参考旋转位置编码，优化多参考图像集成和训练数据质量
- 实验或效果：在多个基准测试中，Kaleido在一致性、保真度和泛化性上显著优于先前方法

## 摘要（原文）

> We present Kaleido, a subject-to-video~(S2V) generation framework, which aims
> to synthesize subject-consistent videos conditioned on multiple reference
> images of target subjects. Despite recent progress in S2V generation models,
> existing approaches remain inadequate at maintaining multi-subject consistency
> and at handling background disentanglement, often resulting in lower reference
> fidelity and semantic drift under multi-image conditioning. These shortcomings
> can be attributed to several factors. Primarily, the training dataset suffers
> from a lack of diversity and high-quality samples, as well as cross-paired
> data, i.e., paired samples whose components originate from different instances.
> In addition, the current mechanism for integrating multiple reference images is
> suboptimal, potentially resulting in the confusion of multiple subjects. To
> overcome these limitations, we propose a dedicated data construction pipeline,
> incorporating low-quality sample filtering and diverse data synthesis, to
> produce consistency-preserving training data. Moreover, we introduce Reference
> Rotary Positional Encoding (R-RoPE) to process reference images, enabling
> stable and precise multi-image integration. Extensive experiments across
> numerous benchmarks demonstrate that Kaleido significantly outperforms previous
> methods in consistency, fidelity, and generalization, marking an advance in S2V
> generation.

