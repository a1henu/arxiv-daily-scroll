---
layout: default
title: GLaD: Geometric Latent Distillation for Vision-Language-Action Models
---

# GLaD: Geometric Latent Distillation for Vision-Language-Action Models
**arXiv**：[2512.09619v1](https://arxiv.org/abs/2512.09619) · [PDF](https://arxiv.org/pdf/2512.09619.pdf)  
**作者**：Minghao Guo, Meng Cao, Jiachen Tao, Rongtao Xu, Yan Yan, Xiaodan Liang, Ivan Laptev, Xiaojun Chang  

**一句话要点**：提出GLaD框架，通过几何潜在蒸馏增强视觉-语言-动作模型的空间推理能力。

**关键词**：视觉-语言-动作模型, 几何蒸馏, 空间推理, 知识对齐, 多模态表示

## 3 点简述
- 现有VLA模型依赖RGB信息，忽略几何线索，影响空间推理和操作。
- GLaD在预训练中通过知识蒸馏整合3D几何先验，对齐LLM隐藏状态与几何感知视觉特征。
- 在Bridge数据集预训练后，GLaD在LIBERO任务中平均成功率94.1%，优于UniVLA。

## 摘要（原文）

> Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

