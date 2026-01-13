---
layout: default
title: SceneNAT: Masked Generative Modeling for Language-Guided Indoor Scene Synthesis
---

# SceneNAT: Masked Generative Modeling for Language-Guided Indoor Scene Synthesis
**arXiv**：[2601.07218v1](https://arxiv.org/abs/2601.07218) · [PDF](https://arxiv.org/pdf/2601.07218.pdf)  
**作者**：Jeongjun Choi, Yeonsoo Park, H. Jin Kim  

**一句话要点**：提出SceneNAT，通过掩码生成建模实现语言引导的室内场景合成，提升性能与效率。

**关键词**：室内场景合成, 掩码生成建模, 非自回归Transformer, 语言引导生成, 三元组预测, 3D场景理解

## 3 点简述
- 核心问题：从自然语言指令合成完整3D室内场景，需兼顾语义合规性和空间布局准确性。
- 方法要点：使用单阶段掩码非自回归Transformer，结合属性级和实例级掩码策略，并引入三元组预测器增强关系推理。
- 实验或效果：在3D-FRONT数据集上优于自回归和扩散基线，计算成本显著降低。

## 摘要（原文）

> We present SceneNAT, a single-stage masked non-autoregressive Transformer that synthesizes complete 3D indoor scenes from natural language instructions through only a few parallel decoding passes, offering improved performance and efficiency compared to prior state-of-the-art approaches. SceneNAT is trained via masked modeling over fully discretized representations of both semantic and spatial attributes. By applying a masking strategy at both the attribute level and the instance level, the model can better capture intra-object and inter-object structure. To boost relational reasoning, SceneNAT employs a dedicated triplet predictor for modeling the scene's layout and object relationships by mapping a set of learnable relation queries to a sparse set of symbolic triplets (subject, predicate, object). Extensive experiments on the 3D-FRONT dataset demonstrate that SceneNAT achieves superior performance compared to state-of-the-art autoregressive and diffusion baselines in both semantic compliance and spatial arrangement accuracy, while operating with substantially lower computational cost.

