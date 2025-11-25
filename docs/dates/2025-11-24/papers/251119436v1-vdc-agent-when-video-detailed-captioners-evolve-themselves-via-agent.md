---
layout: default
title: VDC-Agent: When Video Detailed Captioners Evolve Themselves via Agentic Self-Reflection
---

# VDC-Agent: When Video Detailed Captioners Evolve Themselves via Agentic Self-Reflection
**arXiv**：[2511.19436v1](https://arxiv.org/abs/2511.19436) · [PDF](https://arxiv.org/pdf/2511.19436.pdf)  
**作者**：Qiang Wang, Xinyuan Gao, SongLin Dong, Jizhou Han, Jiangyang Li, Yuhang He, Yihong Gong  

**一句话要点**：提出VDC-Agent自进化框架，实现无需人工标注的视频详细描述生成。

**关键词**：视频详细描述, 自进化框架, 无监督学习, 直接偏好优化, 多模态大语言模型

## 3 点简述
- 核心问题：视频详细描述任务依赖人工标注或大模型，成本高且效率低。
- 方法要点：构建闭环系统，包括描述生成、原则评分、提示优化和自我反思。
- 实验效果：在VDC基准上达到SOTA，准确率49.08%，超越基模型5.13%。

## 摘要（原文）

> We present VDC-Agent, a self-evolving framework for Video Detailed Captioning that requires neither human annotations nor larger teacher models. The agent forms a closed loop of caption generation, principle-guided scoring (score and textual suggestions), and prompt refinement. When caption quality regresses, a self-reflection path leverages the previous chain-of-thought to amend the update. Running this process on unlabeled videos produces trajectories of (caption, score) pairs. We convert the trajectories into preference tuples and filter out samples with JSON parsing errors, resulting in VDC-Agent-19K, which contains 18,886 automatically constructed pairs. We then fine-tune the base MLLM on this dataset using an easy-to-hard curriculum direct preference optimization. Built on Qwen2.5-VL-7B-Instruct, our VDC-Agent-7B attains state-of-the-art performance on the VDC benchmark with 49.08% average accuracy and 2.50 score, surpassing specialized video captioners and improving over the base model by +5.13% accuracy and +0.27 score at similar inference cost.

