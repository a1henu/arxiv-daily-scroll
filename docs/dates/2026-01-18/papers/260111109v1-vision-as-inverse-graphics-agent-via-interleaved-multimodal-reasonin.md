---
layout: default
title: Vision-as-Inverse-Graphics Agent via Interleaved Multimodal Reasoning
---

# Vision-as-Inverse-Graphics Agent via Interleaved Multimodal Reasoning
**arXiv**：[2601.11109v1](https://arxiv.org/abs/2601.11109) · [PDF](https://arxiv.org/pdf/2601.11109.pdf)  
**作者**：Shaofeng Yin, Jiaxin Ge, Zora Zhiruo Wang, Xiuyu Li, Michael J. Black, Trevor Darrell, Angjoo Kanazawa, Haiwen Feng  

**一句话要点**：提出VIGA代理通过交错多模态推理实现视觉作为逆图形任务

**关键词**：逆图形视觉, 交错多模态推理, 闭环代理, 长程推理, 图形引擎基准

## 3 点简述
- 核心问题：现有视觉语言模型缺乏细粒度空间和物理基础能力，无法单次实现图像到可编辑图形程序的重构。
- 方法要点：VIGA采用闭环写-运行-渲染-比较-修订流程，结合技能库和演化上下文记忆，支持长程推理。
- 实验或效果：在BlenderGym和SlideBench上显著提升基线性能，并引入BlenderBench基准验证改进效果。

## 摘要（原文）

> Vision-as-inverse-graphics, the concept of reconstructing an image as an editable graphics program is a long-standing goal of computer vision. Yet even strong VLMs aren't able to achieve this in one-shot as they lack fine-grained spatial and physical grounding capability. Our key insight is that closing this gap requires interleaved multimodal reasoning through iterative execution and verification. Stemming from this, we present VIGA (Vision-as-Inverse-Graphic Agent) that starts from an empty world and reconstructs or edits scenes through a closed-loop write-run-render-compare-revise procedure. To support long-horizon reasoning, VIGA combines (i) a skill library that alternates generator and verifier roles and (ii) an evolving context memory that contains plans, code diffs, and render history. VIGA is task-agnostic as it doesn't require auxiliary modules, covering a wide range of tasks such as 3D reconstruction, multi-step scene editing, 4D physical interaction, and 2D document editing, etc. Empirically, we found VIGA substantially improves one-shot baselines on BlenderGym (35.32%) and SlideBench (117.17%). Moreover, VIGA is also model-agnostic as it doesn't require finetuning, enabling a unified protocol to evaluate heterogeneous foundation VLMs. To better support this protocol, we introduce BlenderBench, a challenging benchmark that stress-tests interleaved multimodal reasoning with graphics engine, where VIGA improves by 124.70%.

