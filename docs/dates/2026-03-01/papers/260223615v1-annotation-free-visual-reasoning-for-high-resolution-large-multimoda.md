---
layout: default
title: Annotation-Free Visual Reasoning for High-Resolution Large Multimodal Models via Reinforcement Learning
---

# Annotation-Free Visual Reasoning for High-Resolution Large Multimodal Models via Reinforcement Learning
**arXiv**：[2602.23615v1](https://arxiv.org/abs/2602.23615) · [PDF](https://arxiv.org/pdf/2602.23615.pdf)  
**作者**：Jiacheng Yang, Anqi Chen, Yunkai Dang, Qi Fan, Cong Wang, Wenbin Li, Feng Miao, Yang Gao  

**一句话要点**：提出HART框架，通过强化学习实现高分辨率大模型的无标注视觉推理

**关键词**：高分辨率视觉推理, 无标注学习, 强化学习, 大模型优化, 视觉定位, 后训练范式

## 3 点简述
- 核心问题：高分辨率视觉输入导致图像令牌冗余，影响大模型推理效率与准确性
- 方法要点：设计AP-GRPO强化学习算法，使模型自聚焦关键区域并自我验证
- 实验或效果：在多种高分辨率任务中超越基线，甚至优于更大规模模型

## 摘要（原文）

> Current Large Multimodal Models (LMMs) struggle with high-resolution visual inputs during the reasoning process, as the number of image tokens increases quadratically with resolution, introducing substantial redundancy and irrelevant information. A common practice is to identify key image regions and refer to their high-resolution counterparts during reasoning, typically trained with external visual supervision. However, such visual supervision cues require costly grounding labels from human annotators. Meanwhile, it remains an open question how to enhance a model's grounding abilities to support reasoning without relying on additional annotations. In this paper, we propose High-resolution Annotation-free Reasoning Technique (HART), a closed-loop framework that enables LMMs to focus on and self-verify key regions of high-resolution visual inputs. HART incorporates a post-training paradigm in which we design Advantage Preference Group Relative Policy Optimization (AP-GRPO) to encourage accurate localization of key regions. Notably, HART provides explainable reasoning pathways and enables efficient optimization of localization. Extensive experiments demonstrate that HART improves performance across a wide range of high-resolution visual tasks, consistently outperforming strong baselines. When applied to post-train Qwen2.5-VL-7B, HART even surpasses larger-scale models such as Qwen2.5-VL-72B and LLaVA-OneVision-72B on high-resolution, vision-centric benchmarks.

