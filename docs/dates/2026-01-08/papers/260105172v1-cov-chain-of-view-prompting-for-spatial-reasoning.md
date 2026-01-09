---
layout: default
title: CoV: Chain-of-View Prompting for Spatial Reasoning
---

# CoV: Chain-of-View Prompting for Spatial Reasoning
**arXiv**：[2601.05172v1](https://arxiv.org/abs/2601.05172) · [PDF](https://arxiv.org/pdf/2601.05172.pdf)  
**作者**：Haoyu Zhao, Akide Liu, Zeyu Zhang, Weijie Wang, Feng Chen, Ruihan Zhu, Gholamreza Haffari, Bohan Zhuang  

**一句话要点**：提出链式视图提示以解决3D环境中多视角空间推理问题

**关键词**：3D环境问答, 多视角推理, 免训练框架, 空间推理, 视觉语言模型, 视图选择

## 3 点简述
- 核心问题：现有视觉语言模型受限于固定输入视图，难以在推理时获取分散且部分遮挡的上下文信息。
- 方法要点：通过粗到细的探索过程，使用视图选择代理和迭代推理与相机动作交替，实现免训练的多视角主动推理。
- 实验或效果：在OpenEQA上平均提升11.56% LLM-Match，并在ScanQA和SQA3D上取得强性能，如ScanQA的116 CIDEr。

## 摘要（原文）

> Embodied question answering (EQA) in 3D environments often requires collecting context that is distributed across multiple viewpoints and partially occluded. However, most recent vision--language models (VLMs) are constrained to a fixed and finite set of input views, which limits their ability to acquire question-relevant context at inference time and hinders complex spatial reasoning. We propose Chain-of-View (CoV) prompting, a training-free, test-time reasoning framework that transforms a VLM into an active viewpoint reasoner through a coarse-to-fine exploration process. CoV first employs a View Selection agent to filter redundant frames and identify question-aligned anchor views. It then performs fine-grained view adjustment by interleaving iterative reasoning with discrete camera actions, obtaining new observations from the underlying 3D scene representation until sufficient context is gathered or a step budget is reached.
>   We evaluate CoV on OpenEQA across four mainstream VLMs and obtain an average +11.56\% improvement in LLM-Match, with a maximum gain of +13.62\% on Qwen3-VL-Flash. CoV further exhibits test-time scaling: increasing the minimum action budget yields an additional +2.51\% average improvement, peaking at +3.73\% on Gemini-2.5-Flash. On ScanQA and SQA3D, CoV delivers strong performance (e.g., 116 CIDEr / 31.9 EM@1 on ScanQA and 51.1 EM@1 on SQA3D). Overall, these results suggest that question-aligned view selection coupled with open-view search is an effective, model-agnostic strategy for improving spatial reasoning in 3D EQA without additional training.

