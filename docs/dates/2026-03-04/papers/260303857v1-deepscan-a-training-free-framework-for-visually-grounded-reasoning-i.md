---
layout: default
title: DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models
---

# DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models
**arXiv**：[2603.03857v1](https://arxiv.org/abs/2603.03857) · [PDF](https://arxiv.org/pdf/2603.03857.pdf)  
**作者**：Yangfu Li, Hongjian Zhan, Jiawei Chen, Yuning Gong, Qi Liu, Yue Lu  

**一句话要点**：提出DeepScan训练免费框架，通过分层扫描、重聚焦和证据增强推理提升大视觉语言模型的视觉基础推理能力。

**关键词**：视觉基础推理, 大视觉语言模型, 训练免费框架, 分层扫描, 证据增强推理, 多尺度证据提取

## 3 点简述
- 核心问题：现有方法在噪声环境中难以一次性定位完整视觉证据，影响大视觉语言模型的视觉基础推理准确性。
- 方法要点：采用分层扫描进行局部线索探索和多尺度证据提取，结合重聚焦优化证据视图，并通过证据增强推理聚合多粒度视图。
- 实验或效果：在V*数据集上集成Qwen2.5-VL-7B达到90.6%准确率，无需额外适应成本即可提升多种架构和规模的模型性能。

## 摘要（原文）

> Humans can robustly localize visual evidence and provide grounded answers even in noisy environments by identifying critical cues and then relating them to the full context in a bottom-up manner. Inspired by this, we propose DeepScan, a training-free framework that combines Hierarchical Scanning, Refocusing, and Evidence-Enhanced Reasoning for visually grounded reasoning in Large Vision-Language Models (LVLMs). Unlike existing methods that pursue one-shot localization of complete evidence, Hierarchical Scanning performs local cue exploration and multi-scale evidence extraction to recover evidence in a bottom-up manner, effectively mitigating the impacts of distractive context. Refocusing then optimizes the localized evidence view through collaboration of LVLMs and visual experts. Finally, Evidence-Enhanced Reasoning aggregates multi-granular views via a hybrid evidence memory and yields accurate and interpretable answers. Experimental results demonstrate that DeepScan significantly boosts LVLMs in diverse visual tasks, especially in fine-grained visual understanding. It achieves 90.6% overall accuracy on V* when integrated with Qwen2.5-VL-7B. Moreover, DeepScan provides consistent improvements for LVLMs across various architectures and model scales without additional adaptation cost.

