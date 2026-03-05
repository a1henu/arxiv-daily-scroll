---
layout: default
title: InEdit-Bench: Benchmarking Intermediate Logical Pathways for Intelligent Image Editing Models
---

# InEdit-Bench: Benchmarking Intermediate Logical Pathways for Intelligent Image Editing Models
**arXiv**：[2603.03657v1](https://arxiv.org/abs/2603.03657) · [PDF](https://arxiv.org/pdf/2603.03657.pdf)  
**作者**：Zhiqiang Sheng, Xumeng Han, Zhiwei Zhang, Zenghui Xiong, Yifan Ding, Aoxiang Ping, Xiang Li, Tong Guo, Yao Mao  

**一句话要点**：提出InEdit-Bench基准以评估图像编辑模型在中间逻辑路径推理中的能力

**关键词**：图像编辑基准, 中间逻辑路径, 多模态生成模型, 动态推理, 评估标准

## 3 点简述
- 核心问题：多模态生成模型在复杂动态推理场景中缺乏中间逻辑路径建模能力
- 方法要点：构建涵盖状态转换、动态过程、时序序列和科学模拟四类任务的测试集
- 实验或效果：评估14个模型显示该领域存在显著不足，旨在推动更智能模型发展

## 摘要（原文）

> Multimodal generative models have made significant strides in image editing, demonstrating impressive performance on a variety of static tasks. However, their proficiency typically does not extend to complex scenarios requiring dynamic reasoning, leaving them ill-equipped to model the coherent, intermediate logical pathways that constitute a multi-step evolution from an initial state to a final one. This capacity is crucial for unlocking a deeper level of procedural and causal understanding in visual manipulation. To systematically measure this critical limitation, we introduce InEdit-Bench, the first evaluation benchmark dedicated to reasoning over intermediate pathways in image editing. InEdit-Bench comprises meticulously annotated test cases covering four fundamental task categories: state transition, dynamic process, temporal sequence, and scientific simulation. Additionally, to enable fine-grained evaluation, we propose a set of assessment criteria to evaluate the logical coherence and visual naturalness of the generated pathways, as well as the model's fidelity to specified path constraints. Our comprehensive evaluation of 14 representative image editing models on InEdit-Bench reveals significant and widespread shortcomings in this domain. By providing a standardized and challenging benchmark, we aim for InEdit-Bench to catalyze research and steer development towards more dynamic, reason-aware, and intelligent multimodal generative models.

