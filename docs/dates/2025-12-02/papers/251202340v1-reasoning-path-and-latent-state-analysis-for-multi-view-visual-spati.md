---
layout: default
title: Reasoning Path and Latent State Analysis for Multi-view Visual Spatial Reasoning: A Cognitive Science Perspective
---

# Reasoning Path and Latent State Analysis for Multi-view Visual Spatial Reasoning: A Cognitive Science Perspective
**arXiv**：[2512.02340v1](https://arxiv.org/abs/2512.02340) · [PDF](https://arxiv.org/pdf/2512.02340.pdf)  
**作者**：Qiyao Xue, Weichen Liu, Shiqi Wang, Haoming Wang, Yuyang Wu, Wei Gao  

**一句话要点**：提出ReMindView-Bench基准以评估多视图视觉空间推理中视觉语言模型的认知能力

**关键词**：多视图空间推理, 视觉语言模型, 认知基准, 跨视图一致性, 推理路径分析, 熵动态

## 3 点简述
- 核心问题：当前视觉语言模型在多视图空间推理中缺乏几何一致性和跨视图一致性。
- 方法要点：构建认知基础基准，系统变化视图空间模式和查询类型以探测空间认知关键因素。
- 实验或效果：评估15个模型，揭示跨视图对齐和视角采样的失败，并通过显隐分析诊断推理过程退化。

## 摘要（原文）

> Spatial reasoning is a core aspect of human intelligence that allows perception, inference and planning in 3D environments. However, current vision-language models (VLMs) struggle to maintain geometric coherence and cross-view consistency for spatial reasoning in multi-view settings. We attribute this gap to the lack of fine-grained benchmarks that isolate multi-view reasoning from single-view perception and temporal factors. To address this, we present ReMindView-Bench, a cognitively grounded benchmark for evaluating how VLMs construct, align and maintain spatial mental models across complementary viewpoints. ReMindView-Bench systematically varies viewpoint spatial pattern and query type to probe key factors of spatial cognition. Evaluations of 15 current VLMs reveals consistent failures in cross-view alignment and perspective-taking in multi-view spatial reasoning, motivating deeper analysis on the reasoning process. Explicit phase-wise analysis using LLM-as-a-judge and self-consistency prompting shows that VLMs perform well on in-frame perception but degrade sharply when integrating information across views. Implicit analysis, including linear probing and entropy dynamics, further show progressive loss of task-relevant information and uncertainty separation between correct and incorrect trajectories. These results provide a cognitively grounded diagnosis of VLM spatial reasoning and reveal how multi-view spatial mental models are formed, degraded and destabilized across reasoning phases. The ReMindView-Bench benchmark is available at https://huggingface.co/datasets/Xue0823/ReMindView-Bench, and the source codes of benchmark construction and VLM reasoning analysis are available at https://github.com/pittisl/ReMindView-Bench.

