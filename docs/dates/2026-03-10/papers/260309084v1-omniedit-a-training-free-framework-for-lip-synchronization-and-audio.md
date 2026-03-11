---
layout: default
title: OmniEdit: A Training-free framework for Lip Synchronization and Audio-Visual Editing
---

# OmniEdit: A Training-free framework for Lip Synchronization and Audio-Visual Editing
**arXiv**：[2603.09084v1](https://arxiv.org/abs/2603.09084) · [PDF](https://arxiv.org/pdf/2603.09084.pdf)  
**作者**：Lixiang Lin, Siyuan Jin, Jinshan Zhang  

**一句话要点**：提出OmniEdit训练免调框架，用于唇音同步与音视频编辑，降低计算与数据需求。

**关键词**：唇音同步, 音视频编辑, 训练免调框架, 无偏估计, 稳定编辑轨迹

## 3 点简述
- 核心问题：现有唇音同步与音视频编辑方法依赖监督微调，计算开销大且需大量数据。
- 方法要点：通过替换FlowEdit中的编辑序列为目标序列，实现无偏估计输出，并移除生成过程的随机性以稳定编辑轨迹。
- 实验或效果：广泛实验验证了框架的有效性和鲁棒性，代码已开源。

## 摘要（原文）

> Lip synchronization and audio-visual editing have emerged as fundamental challenges in multimodal learning, underpinning a wide range of applications, including film production, virtual avatars, and telepresence. Despite recent progress, most existing methods for lip synchronization and audio-visual editing depend on supervised fine-tuning of pre-trained models, leading to considerable computational overhead and data requirements. In this paper, we present OmniEdit, a training-free framework designed for both lip synchronization and audio-visual editing. Our approach reformulates the editing paradigm by substituting the edit sequence in FlowEdit with the target sequence, yielding an unbiased estimation of the desired output. Moreover, by removing stochastic elements from the generation process, we establish a smooth and stable editing trajectory. Extensive experimental results validate the effectiveness and robustness of the proposed framework. Code is available at https://github.com/l1346792580123/OmniEdit.

